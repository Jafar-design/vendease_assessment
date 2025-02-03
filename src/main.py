from mentorship import assign_mentorships
from database import SessionLocal, MemberDB, MentorshipDB, drop_tables, Base, engine
from utils import create_members
from queries import median_age_of_male_mentorees
from api_client import fetch_users
from models import Member, Mentorship
from analysis import get_median_age_male_mentorees, count_mentorees_by_gender_mentored_by_seniors #,check_data_discrepancies

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

    return pd.DataFrame(members_dict)

from models import Mentorship  # Import Mentorship class


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
    print("============== Dropping tables for idempotency and reproducibility ======================")
    drop_tables()
    print("============== Recreating the tables  ======================")
    Base.metadata.create_all(engine)
    print("============== Saving the changes  ======================")
    save_to_db()

     # Fetch members from API
    members = fetch_members()

    # Convert to DataFrame
    members_df = create_members_dataframe(members)

    # Display the first 5 rows
    print(members_df.head())

    print("Data successfully saved to PostgreSQL!")

    print("============== Solution to Step 8  ======================")
    # median_age_of_male_mentorees()
    mentorships = assign_mentorships()
    mentorships_df = create_mentorships_dataframe(mentorships)
    median_age = get_median_age_male_mentorees(members_df, mentorships_df)
    print(f"🟢 Median age of male mentorees registered after 2010: {median_age}")

    print("============== Solution to Step 9  ======================")
    count_mentorees_by_gender_mentored_by_seniors(members_df, mentorships_df)

    # Run data discrepancy check
    print("============== Solution to Step 10  ======================")
    #discrepancies = check_data_discrepancies(members_df, mentorships_df)

