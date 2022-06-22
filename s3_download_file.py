from urllib import response
import boto3

s3_client = boto3.client('s3')

response = s3_client.download_file(
    'mys3boto3bucket', 'Manthan.pdf', r'C:\Users\Manthan\Documents\Manthan.pdf')
