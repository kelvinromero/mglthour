from elasticsearch import Elasticsearch
from starships.search import count_all_starships
import requests
import swapi

es_host = {"host": "es", "port": 9200}
es = Elasticsearch(hosts=[es_host])


def index_has_update(index_name, url='https://swapi.co/api/starships'):
    es_count = count_all_starships(index_name)
    api_count = requests.get(url=url).json().get('count')
    return es_count != api_count


def create_index(index_name):
    es_settings = {
        "settings": {
            "number_of_shards": 5,
            "number_of_replicas": 5
        }
    }

    if es.indices.exists(index_name):
            es.indices.delete(index=index_name)
    es_response = es.indices.create(index=index_name, body=es_settings)

    return es_response


def fetch_from_api(url='https://swapi.co/api/starships'):
    starships = requests.get(url=url)
    starships = starships.json().get('results')
    return starships


def fetch_from_lib(entity="starships"):
    starships = swapi.get_all(entity)
    starships = [startship.__dict__ for startship in starships.items]
    return starships


def save_to_es(index_name, data):
    starships = data

    oper_dict = {
        "index": {
            "_index": index_name,
            "_type": "_doc",
        }
    }

    bulk_data = []
    for startship in starships:
        bulk_data.append(oper_dict)
        bulk_data.append(startship)

    es_response = es.bulk(index=index_name, body=bulk_data, request_timeout=30)

    return es_response
