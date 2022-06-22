from urllib import response
import boto3

s3_client = boto3.client('s3')

response = s3_client.upload_file(
    r"C:\Users\Manthan\Downloads\Manthan_Thakkar_Resume_N.pdf", 'mys3boto3bucket', 'Manthan.pdf')
