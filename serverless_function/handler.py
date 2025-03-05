import json

def hello(event, context):
    name = event.get('name', 'World')  
    body = {
        "message": f"Hello, BRYAN AND JUAN MANUEL",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response