import logging
import os
import pymongo
from bson.json_util import dumps

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        url = os.environ['ex8_cosmos_db']
        print('url: {}'.format(url))
        client = pymongo.MongoClient(url)
        database = client['ex8']
        collection = database['notes']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad Request.", status_code=400)
