from django.apps import AppConfig
from starships.fetch import fetch_from_lib, save_to_es, index_has_update, create_index
import requests
from time import sleep
from elasticsearch import NotFoundError


class StarshipsConfig(AppConfig):
    name = 'starships'

    def ready(self):
        index_name = 'starships'
        es_health = "http://es:9200/_cluster/health?wait_for_status=yellow&timeout=20s"
        ready = False

        # Wait for Elastic Search
        while not ready:
            try:
                response = requests.get(es_health)
                if response.status_code == 200:
                    ready = True
            except requests.exceptions.ConnectionError as e:
                print("Elastic Search not running yet. Connection Error Message:", e)
                sleep(10)

        # Index data if necessary
        try:
            index_has_update(index_name)

        except NotFoundError as e:
            create_index(index_name)

        finally:
            if index_has_update(index_name):
                create_index(index_name)
                data = fetch_from_lib("starships")
                save_to_es(index_name, data)
            else:
                print("API has no updates")
