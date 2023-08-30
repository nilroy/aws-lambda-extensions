# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import json
import os
import requests
from datetime import datetime


def lambda_handler(event, context):
    # print(f"Function: Logging something which logging extension will send to S3")
    # json_log = {
    #     "log": "Logging something which logging extension will send to 'S3'",
    #     "logTime": datetime.now().isoformat(),
    #     "fruits": ["apple", "orange"],
    # }
    # print(json.dumps(json_log))
    non_json_log = "This is some random text that is not json - emitted using json.dumps() method"
    print(json.dumps(non_json_log))
    # non_json_log_2 = "This is some random text that is not json - emitted raw"
    # print(non_json_log_2)

    # snsEventMsg = {
    #     "message": "CloudWatch alarm event, new state value: CloudWatchAlarmState.ALARM sent to slack. Status: 200",
    #     "team": "CREAINT",
    #     "timestamp": "2023-08-22T22:11:46.579660+0000",
    #     "name": "slacksender.app.main",
    #     "module": "main",
    #     "project": "ci-infra-cw-alerts-to-slack",
    #     "file": "main.py",
    #     "thread": "140179405915968",
    #     "level": "INFO",
    #     "line": "129",
    #     "process": "16",
    # }

    # checkCutoffDateAndProcessMsgs = {
    #     "timestamp": "2023-08-18T19:37:48.955309+0000",
    #     "level": "INFO",
    #     "message": {
    #         "description": "checkCutoffDateAndProcessMsgs",
    #         "trace_context": {
    #             "callerId": "aws-e9d7965d-e611-5e39-977f-cb042cd5625c",
    #             "executionId": "ci-e9d7965d-e611-5e39-977f-cb042cd5625c",
    #             "transactionId": "ci-e9d7965d-e611-5e39-977f-cb042cd5625c",
    #         },
    #     },
    #     "process": "8",
    #     "thread": "140531354658624",
    #     "module": "main",
    #     "file": "main.py",
    #     "name": "ingestor_filter.app.main",
    #     "line": "161",
    # }

    # cutoffDate = {
    #     "timestamp": "2023-07-20T17:29:21.493921+0000",
    #     "level": "DEBUG",
    #     "message": {
    #         "description": "cutoffDate",
    #         "trace_context": {
    #             "callerId": "aws-781c7e86-1dbe-5498-a6a4-23b56c90135e",
    #             "executionId": "ci-781c7e86-1dbe-5498-a6a4-23b56c90135e",
    #             "transactionId": "ci-781c7e86-1dbe-5498-a6a4-23b56c90135e",
    #         },
    #         "context": {"adCreationDate": "2019-05-15 22:11:48+00:00", "adCreationCutoffDateStart": "2022-04-27 22:12:58+02:00"},
    #     },
    #     "process": "8",
    #     "thread": "140607888807744",
    #     "module": "main",
    #     "file": "main.py",
    #     "name": "ingestor_filter.app.main",
    #     "line": "189",
    # }

    # deleteMsgInvalidSchema = {
    #     "timestamp": "2023-07-20T17:24:25.949960+0000",
    #     "level": "DEBUG",
    #     "message": {
    #         "description": "deleteMsgInvalidSchema",
    #         "trace_context": {
    #             "callerId": "aws-da5c2284-bad0-505c-a31e-7fb7cad96121",
    #             "executionId": "ci-da5c2284-bad0-505c-a31e-7fb7cad96121",
    #             "transactionId": "ci-da5c2284-bad0-505c-a31e-7fb7cad96121",
    #         },
    #         "context": {
    #             "message": {
    #                 "messageId": "9073f9a2-1fbd-4544-a535-f6b1f2e35a01",
    #                 "receiptHandle": "AQEBTHmCWyrkp6JUEIHvtA+YkbnvEIN33UB09whaCzn2sdTywaiLPMOcUP4i9uyGOurWKWS2G5QKtki7pIUAPwDxPs4rpdoyb7Tx9RUUmmbv20PtTbNL1w1maQuGKJT8rdoCrHfhmeQc1+KnF8hlbKn0HLJyIBE/LqK5GZZuCnCWyo/lAX8jpmWGK2eCh5SriOk5tGg2dQqLyaeQnxrse7XDQEeLd8IS+dTFxSZy+NzfBibUhTxP4RGRNLrOQknh/pWWI6whI/5I5Bo44Z9xdUdajM0VuhT7xtNRQIyyOd4vkENw8aJa7PY0tBNuPtSg/W8UTm2iVRxF/R+rOnPX3f98dCmkOYH61jPJw/dAJ1bUWkI=",
    #                 "body": {
    #                     "platform": "facebook",
    #                     "status": "PAUSED",
    #                     "configured_status": "PAUSED",
    #                     "origin": "smartly",
    #                     "platform_id": "6113481568916",
    #                     "id": "5c66c0ae72be5569f32d89ff",
    #                     "account_id": "589c71f57bff853d568b4567",
    #                     "company_id": "5acde5def3fd8f5845053de2",
    #                     "account_platform_id": "1384915905101932",
    #                     "campaign_id": "5c66c0a872be5569f32d89f3",
    #                     "adset_id": "5c66c0a872be5569f32d89f5",
    #                     "adset_platform_id": "6113481563116",
    #                     "name": "BE-NL_DTA_hotels_City_retargeting_high -",
    #                     "product_set_id": "829724997205631",
    #                     "created_at": "2019-02-15T13:37:52.000Z",
    #                     "updated_at": "2019-06-28T12:04:54.000Z",
    #                     "issues": [
    #                         {
    #                             "level": "AD_SET",
    #                             "error_type": "HARD_ERROR",
    #                             "error_summary": "This Ad Set Has 1 Error",
    #                             "error_message": 'This Ad Set Has 1 Error: Your ad set was paused because the audience "Retargeting>61d::Inclusion::Hotel Audience" was deleted and removed from this ad set. Review your audience settings and if needed, make changes before turning the ad set back on.',
    #                             "error_code": 2446446,
    #                         }
    #                     ],
    #                 },
    #                 "attributes": {
    #                     "ApproximateReceiveCount": "1",
    #                     "AWSTraceHeader": "Root=1-64b96dc4-48ab64a45d43982f766d6419;Parent=7d6b907801a9f7d4;Sampled=0;Lineage=6d0fcd51:0%7C355d3733:0",
    #                     "SentTimestamp": "1689873860769",
    #                     "SequenceNumber": "18879351782066417664",
    #                     "MessageGroupId": "dc991cf4-a079-43ff-bd59-00b4cc9951e7",
    #                     "SenderId": "AROATSJUOQUCO5RVXQC4P:CREAINT_prod_infra-creative-ingestion-enqueuer_Enqueuer",
    #                     "MessageDeduplicationId": "897708113665748a91aecd895591d6444e797933e3cff13022dca5e39ea19c63",
    #                     "ApproximateFirstReceiveTimestamp": "1689873865872",
    #                 },
    #                 "messageAttributes": {},
    #                 "md5OfBody": "8fc8fcf4792da43a200c7f77df67bf99",
    #                 "eventSource": "aws:sqs",
    #                 "eventSourceARN": "arn:aws:sqs:eu-central-1:245460010244:ci-prod-creative-ingestion-ingestor-filter_creative_ingestor_queue.fifo",
    #                 "awsRegion": "eu-central-1",
    #             }
    #         },
    #     },
    #     "process": "8",
    #     "thread": "139703415633728",
    #     "module": "main",
    #     "file": "main.py",
    #     "name": "ingestor_filter.app.main",
    #     "line": "72",
    # }

    # creaint_prod_infra_creative_ingestion_enqueuer_Enqueuer_log = {
    #     "message": "ReceivedEnqueueRequest",
    #     "timestamp": "2023-08-25T10:17:04.352213+0000",
    #     "level": "INFO",
    #     "line": "15",
    #     "name": "enqueuer.app.main",
    #     "project": "infra-creative-ingestion-enqueuer",
    #     "process": "16",
    #     "module": "main",
    #     "thread": "140058610808640",
    #     "file": "main.py",
    #     "aws_request_id": "411ad72f-e4b2-412a-a233-cd7f2649ac8b",
    #     "team": "CREAINT",
    # }

    # print(json.dumps(snsEventMsg))
    # print(json.dumps(checkCutoffDateAndProcessMsgs))
    # print(json.dumps(cutoffDate))
    # print(json.dumps(deleteMsgInvalidSchema))
    # print(json.dumps(creaint_prod_infra_creative_ingestion_enqueuer_Enqueuer_log))

    return {"statusCode": 200, "body": json.dumps("Hello from Lambda!")}
