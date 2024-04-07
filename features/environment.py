import requests
from utilities.config import getConfig
from utilities.resorces import ApiResources


def after_scenario(context, scenario):
    if 'library' in scenario.tags:
        url2 = getConfig()['API']['endpoint'] + ApiResources.deletebook
        add_book_response = requests.delete(url2, json={'ID': context.book_id}, headers=context.headers)
        print(add_book_response.status_code)
        info2 = add_book_response.json()
        print(info2)