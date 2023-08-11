import os
import requests
import json
import boto3
from datetime import datetime

DISPATCH_POST_URI = os.getenv("DISPATCH_POST_URI")
DISPATCH_MIN_BATCH_SIZE = int(os.getenv("DISPATCH_MIN_BATCH_SIZE")) or 1;

# def dispatch_telmetery(queue, force):
#     while ((not queue.empty()) and (force or queue.qsize() >= DISPATCH_MIN_BATCH_SIZE)):
#         print ("[telementry_dispatcher] Dispatch telemetry data")
#         batch = queue.get_nowait()

#         if DISPATCH_POST_URI is None:
#             print ('[telementry_dispatcher:dispatch] dispatchPostUri not found. Discarding log events from the queue')
#         else:
#             # Modify the below line to dispatch/send the telemetry data to the desired choice of observability tool.
#             response = requests.post(
#                 DISPATCH_POST_URI, 
#                 data = json.dumps(batch),
#                 headers= {'Content-Type': 'application/json'}
#             )
#             #print(f"BATCH RECEIVED: {batch}", flush=True)

def dispatch_telmetery(queue, force):
    s3_bucket = (os.environ['S3_BUCKET_NAME'])
    s3 = boto3.resource('s3')
    while ((not queue.empty()) and (force or queue.qsize() >= DISPATCH_MIN_BATCH_SIZE)):
        print ("[telementry_dispatcher] Dispatch telemetry data")
        batch = queue.get_nowait()
        # This following line logs the events received to CloudWatch.
        # Replace it to send logs to elsewhere.
        # If you've subscribed to extension logs, e.g. "types": ["platform", "function", "extension"],
        # you'll receive the logs of this extension back from Logs API.
        # And if you log it again with the line below, it will create a cycle since you receive it back again.
        # Use `extension` log type if you'll egress it to another endpoint,
        # or make sure you've implemented a protocol to handle this case.
#                print(f"Log Batch Received from Lambda: {batch}", flush=True)

#       There are two options illustrated:
#       1. Sending the entire log batch to S3
#       2. Parsing the batch and sending individual log lines.
#       This could be used to parse the log lines and only selectively send logs to S3, or amend for any other destination.

        s3_filename = (os.environ['AWS_LAMBDA_FUNCTION_NAME'])+'-'+(datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f'))+'.log'
        try:
            response = s3.Bucket(s3_bucket).put_object(Key=s3_filename, Body=str(batch))
        except Exception as e:
            raise Exception(f"Error sending log to S3 {e}") from e

#       2. The following parses the batch and sends individual log line
#           try:
#              for item in range(len(batch)):
#                  s3_filename = (os.environ['AWS_LAMBDA_FUNCTION_NAME'])+'-'+(datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f'))+'.'+str(item)+'.log'
#                  content = str(batch[item])
#                  response = s3.Bucket(s3_bucket).put_object(Key=s3_filename, Body=content)
#           except Exception as e:
#               raise Exception(f"Error sending log to S3 {e}") from e
