import json

# print("function initialization")


def lambda_handler(event, context):
    print("inside the handler")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello lambda extensions",
            }
        ),
    }
