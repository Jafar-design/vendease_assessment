from api_client import fetch_users
from models import Member

def create_members():
    users = fetch_users()
    return [Member.from_api(user) for user in users]

if __name__ == "__main__":
    members = create_members()
    print(members[:2])  # Preview first 2 members
