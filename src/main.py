from mentorship import assign_mentorships
from database import SessionLocal, MemberDB, MentorshipDB, Base, engine
from drop_tables import drop_tables
from utils import create_members
from api_client import fetch_users
from models import Member
from analysis import get_median_age_male_mentorees, count_mentorees_by_gender_mentored_by_seniors 
from data_descrepancy import check_data_discrepancy

import pandas as pd

def fetch_members():
    """
    Fetch 500 users from the Random User Generator API and create Member objects.
    
    Returns:
    - A list of Member objects.
    """
    data = fetch_users()  # Extract the 'results' from the api_client file

    # Convert each user to a Member object
    members = [Member.from_api(user) for user in data]
    
    return members

def create_members_dataframe(members):
    """
    Convert the list of Member objects into a Pandas DataFrame.
    
    Parameters:
    - members: List of Member objects.
    
    Returns:
    - Pandas DataFrame containing all members.
    """
    members_dict = [member.dict() for member in members]

    members_df = pd.DataFrame(members_dict)

    """
    Remove duplicate emails from the members DataFrame, keeping the first occurrence.
    """
    members_df = members_df.drop_duplicates(subset=["email"], keep="first")
    return members_df

# Convert mentorships list to DataFrame
def create_mentorships_dataframe(mentorships):
    """
    Creates a pandas DataFrame from a list of Mentorship objects.
    """
    mentorships_data = [
        {
            "uuid": mentorship.uuid,
            "mentor_uuid": mentorship.mentor_uuid,
            "mentoree_uuid": mentorship.mentoree_uuid
        }
        for mentorship in mentorships
    ]
    
    return pd.DataFrame(mentorships_data)

def save_to_db():
    session = SessionLocal()
    members = create_members()
    mentorships = assign_mentorships()

    session.bulk_save_objects([MemberDB(**m.dict()) for m in members])
    session.bulk_save_objects([MentorshipDB(**m.dict()) for m in mentorships])

    session.commit()
    session.close()

if __name__ == "__main__":
    print("\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..\n..")
    print("============== Dropping tables for idempotency and reproducibility ======================")
    drop_tables()
    print("============== Recreating the tables  ======================")
    Base.metadata.create_all(engine)
    print("============== Saving the changes  ======================")
    save_to_db()
    print("Data successfully saved to PostgreSQL!")

    print("""
        ====================SOLUTION TO THE ASSESSMENT==========================
        """)
     # Fetch members from API
    members = fetch_members()

    print("============== Solution to Step 6  ======================")
    members_df = create_members_dataframe(members)
    # Display the first 5 rows
    print(members_df.head())
    print("\n..\n..\n..\n..\n..")

    print("============== Solution to Step 7  ======================")
    mentorships = assign_mentorships()
    mentorships_df = create_mentorships_dataframe(mentorships)
    print(mentorships_df.head())
    print("\n..\n..\n..\n..\n..")

    print("============== Solution to Step 8  ======================")
    # median_age_of_male_mentorees()
    median_age = get_median_age_male_mentorees(members_df, mentorships_df)
    print(f"🟢 Median age of male mentorees registered after 2010: {median_age}")
    print("\n..\n..\n..\n..\n..")

    print("============== Solution to Step 9  ======================")
    count_mentorees_by_gender_mentored_by_seniors(members_df, mentorships_df)
    print("\n..\n..\n..\n..\n..")

    # Run data discrepancy check
    print("============== Solution to Step 10  ======================")
    check_data_discrepancy(members_df, mentorships_df)
    print("\n..\n..\n..\n..\n..")

