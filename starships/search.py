from elasticsearch import Elasticsearch

es = Elasticsearch(hosts=[{"host": "es", "port": 9200}], verify_certs=True)


def count_all_starships(index_name="starships"):
    res = es.search(
        index=index_name,
        body={"query": {"match_all": {}}}
    )

    return res['hits']['total']


def all_starships(index_name="starships"):
    es_response = es.search(
        index=index_name,
        body={"query": {"match_all": {}}},
        size=count_all_starships(),
    )

    return to_dict(es_response)


def to_dict(es_response):
    startships = []

    es_hits = es_response['hits']['hits']
    for es_hit in es_hits:
        startships.append(es_hit['_source'])

    return startships
