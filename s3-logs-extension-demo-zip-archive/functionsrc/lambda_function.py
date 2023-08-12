# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import requests
from datetime import datetime


def lambda_handler(event, context):
    # print(f"Function: Logging something which logging extension will send to S3")
    # log = {
    #     "timestamp": datetime.now().isoformat(),
    #     "message": "Logging something which logging extension will send to S3",
    #     "functionName": os.getenv("AWS_LAMBDA_FUNCTION_NAME"),
    #     "type": "LambdFunction",
    # }
    # print(json.dumps(log))
    print("Logging something which logging extension will send to S3")
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
