from email.headerregistry import Group
from urllib import response
import boto3
import yaml

with open(r"data.yaml") as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

iam_client = boto3.client("iam")
# creating IAM Users
for i in data["Users"]:
    response = iam_client.create_user(
        UserName = i
    )
#Assigning Group to IAM Users
for group in data['GroupAssignment']:
    for user in data["GroupAssignment"][group]:
        response = iam_client.add_user_to_group(
            GroupName = group,
            UserName = user
        )