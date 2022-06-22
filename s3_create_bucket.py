from http import client
from urllib import response
from venv import create
import boto3

s3_client = boto3.client('s3')

response = s3_client.create_bucket(
    ACL='private',
    Bucket='mys3boto3bucket'
)

print(response)
