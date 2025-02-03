import requests

API_URL = "https://randomuser.me/api/?nat=ca&results=500&seed=vendease"

def fetch_users():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()['results']

if __name__ == "__main__":
    users = fetch_users()
    print(users[:2])  # Preview first 2 users
