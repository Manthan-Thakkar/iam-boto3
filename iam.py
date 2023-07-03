import boto3
import yaml
from botocore.exceptions import ClientError

iam_client = boto3.client("iam")

def create_users(users):
    for user in users:
        if check_user(user) == None:
            response = iam_client.create_user(UserName=user)
            attach_iam_change_password_role(user)
            create_login(user)
        else:
            print("User "+user+" already Exists")

def assign_users_to_groups(group_assignment):
    for group in group_assignment:
        for user in group_assignment[group]:
            response = iam_client.add_user_to_group(
                GroupName=group,
                UserName=user
            )

def check_user(user):
    try:
        response = iam_client.get_user(
        UserName=user)
    except ClientError as e:
        if e.response["Error"]["Code"] == "NoSuchEntity":
            response=None
        else:
            raise e
    return response

def attach_iam_change_password_role(user):
    response = iam_client.attach_user_policy(
    UserName=user,
    PolicyArn='arn:aws:iam::aws:policy/IAMUserChangePassword'
)

def create_login(user):
    response = iam_client.create_login_profile(
    UserName=user,
    Password='First@123',
    PasswordResetRequired=True
)


def main():
    with open(r"data.yaml") as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    
    users = data.get("Users", [])
    groups = data.get("GroupAssignment", {})
    create_users(users)
    assign_users_to_groups(groups)

if __name__ == "__main__":
    main()
