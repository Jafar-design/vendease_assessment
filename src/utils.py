from api_client import fetch_users
from sqlalchemy.exc import IntegrityError
from models import Member


import pandas as pd

def create_members():
    users = fetch_users()
    
    # Convert to list of dictionaries to process duplicates
    user_dicts = [Member.from_api(user).__dict__ for user in users]
    
    # Convert to DataFrame for easy duplicate removal
    members_df = pd.DataFrame(user_dicts)
    
    # Remove duplicate emails, keeping the first occurrence
    members_df = members_df.drop_duplicates(subset=["email"], keep="first")

    # Convert back to Member objects
    return [Member(**row) for _, row in members_df.iterrows()]


if __name__ == "__main__":
    members = create_members()
    print(members[:2])  # Preview first 2 members
