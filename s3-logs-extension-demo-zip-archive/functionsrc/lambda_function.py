# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import requests
from datetime import datetime


def lambda_handler(event, context):
    # print(f"Function: Logging something which logging extension will send to S3")
    json_log = {
        "log": "Logging something which logging extension will send to 'S3'",
        "logTime": datetime.now().isoformat(),
        "fruits": ["apple", "orange"],
    }
    print(json.dumps(json_log))
    non_json_log = "This is some random text that is not json - emitted using json.dumps() method"
    print(json.dumps(non_json_log))
    non_json_log_2 = "This is some random text that is not json - emitted raw"
    print(non_json_log_2)
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
