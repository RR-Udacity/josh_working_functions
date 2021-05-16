import azure.functions as func
import pymongo
import os

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()
    print('request: {}'.format(request))
    if request:
        try:
            # add your connection string here
            url = os.environ['ex8_cosmos_db']
            client = pymongo.MongoClient(url)

            # you will need this fill in
            database = client['ex8']
            collection = database['notes']

            # replace the insert_one variable with what you think should be in the bracket
            collection.insert_one(request)

            # we are returning the request body so you can take a look at the results
            return func.HttpResponse(req.get_body())

        except ValueError:
            return func.HttpResponse('Database connection error.', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass the correct JSON format in the body of the request object",
            status_code=400
        )
