# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import requests
from datetime import datetime


def lambda_handler(event, context):
    print(f"Function: Logging something which logging extension will send to S3")
    # log = {"log": "Logging something which logging extension will send to S3"}
    # print(log)
    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
