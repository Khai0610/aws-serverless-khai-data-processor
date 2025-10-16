import json
import boto3
import uuid
import datetime
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserLogs')

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

       
        if 'body' in event:
            body = json.loads(event['body'])
        else:
           
            body = event

        name = body.get('name')
        email = body.get('email')

        if not name or not email:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing name or email"})
            }

    
        user_id = str(uuid.uuid4())
        timestamp = datetime.datetime.utcnow().isoformat()
        file_name = f"user_{user_id}.json"
        bucket_name = os.environ.get('S3_BUCKET', 'serverless-khai-data-demo')

        s3.put_object(
            Bucket=bucket_name,
            Key=file_name,
            Body=json.dumps({"name": name, "email": email, "timestamp": timestamp})
        )

   
        table.put_item(Item={
            'id': user_id,
            'name': name,
            'email': email,
            'timestamp': timestamp,
            's3_file': file_name
        })

        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Data saved successfully!"})
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
