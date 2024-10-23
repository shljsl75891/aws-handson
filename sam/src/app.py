import json
import os

import boto3

print('Loading function')

region = os.environ['REGION']
dynamo = boto3.client('dynamodb', region_name=region)
table_name = os.environ['TABLE_NAME']


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    scan_result = dynamo.scan(TableName=table_name)
    return respond(None, res=scan_result)
