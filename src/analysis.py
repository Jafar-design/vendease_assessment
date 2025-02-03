import pandas as pd
from datetime import datetime
import pandasql as ps

def get_median_age_male_mentorees(members_df, mentorships_df):
    """
    Calculates the median age of male mentorees who registered on or after 2010-01-01.

    Parameters:
    - members_df (pd.DataFrame): DataFrame containing members' details.
    - mentorships_df (pd.DataFrame): DataFrame containing mentorships.

    Returns:
    - float: Median age of male mentorees who registered after 2010.
    """
    # Convert registered date to datetime format
    members_df["registered_date"] = pd.to_datetime(members_df["registered_date"])

    # Filter mentorees who registered after 2010-01-01
    filtered_mentorees = members_df[
        (members_df["uuid"].isin(mentorships_df["mentoree_uuid"])) &  # Only mentorees
        (members_df["gender"] == "male") &  # Male only
        (members_df["registered_date"] >= datetime(2010, 1, 1))  # Registered after 2010
    ]

    # Compute median age
    median_age = filtered_mentorees["age"].median()

    return median_age

def count_mentorees_by_gender_mentored_by_seniors(members_df, mentorships_df):
    """
    Counts the total number of mentorees (grouped by gender) who are mentored by members aged 60+.
    
    Args:
        members_df (pd.DataFrame): DataFrame containing all members.
        mentorships_df (pd.DataFrame): DataFrame containing mentorship pairs.

    Returns:
        pd.DataFrame: DataFrame containing the count of mentorees grouped by gender.
    """

    query = """
        SELECT m.gender, COUNT(*) AS mentoree_count
        FROM mentorships_df AS ms
        JOIN members_df AS m ON ms.mentoree_uuid = m.uuid
        JOIN members_df AS mentor ON ms.mentor_uuid = mentor.uuid
        WHERE mentor.age >= 60
        GROUP BY m.gender
    """

    # Execute SQL query
    result_df = ps.sqldf(query, locals())
    
    print(result_df) 
    return result_df


# def check_data_discrepancies(members_df, mentorships_df):
#     """
#     Checks for data discrepancies in members and mentorships data.

#     Args:
#         members_df (pd.DataFrame): DataFrame containing all members.
#         mentorships_df (pd.DataFrame): DataFrame containing mentorship pairs.

#     Returns:
#         dict: Summary of discrepancies found.
#     """

#     discrepancies = {}

#     # 1. Check for missing values
#     missing_members = members_df.isnull().sum()
#     missing_mentorships = mentorships_df.isnull().sum()
    
#     discrepancies["missing_members"] = missing_members[missing_members > 0].to_dict()
#     discrepancies["missing_mentorships"] = missing_mentorships[missing_mentorships > 0].to_dict()

#     # 2. Check for duplicate UUIDs
#     duplicate_members = members_df['uuid'].duplicated().sum()
#     duplicate_mentorships = mentorships_df[['mentor_uuid', 'mentoree_uuid']].duplicated().sum()

#     discrepancies["duplicate_member_uuids"] = duplicate_members
#     discrepancies["duplicate_mentorships"] = duplicate_mentorships

#     # 3. Validate age calculations
#     age_mismatch = members_df[
#         (members_df["age"] < 0) | (members_df["age"] > 120)  # Unreasonable ages
#     ]
#     discrepancies["invalid_ages"] = age_mismatch[["uuid", "fullname", "age"]].to_dict(orient="records")

#     # 4. Check for mentorships assigned to non-existent members
#     invalid_mentors = mentorships_df[~mentorships_df["mentor_uuid"].isin(members_df["uuid"])]
#     invalid_mentorees = mentorships_df[~mentorships_df["mentoree_uuid"].isin(members_df["uuid"])]

#     discrepancies["invalid_mentors"] = invalid_mentors.to_dict(orient="records")
#     discrepancies["invalid_mentorees"] = invalid_mentorees.to_dict(orient="records")

#     # 5. Check if mentorships are following the correct mentor-mentoree age rule
#     merged_df = mentorships_df.merge(
#         members_df, left_on="mentor_uuid", right_on="uuid", suffixes=("_mentorship", "_mentor")
#     ).merge(
#         members_df, left_on="mentoree_uuid", right_on="uuid", suffixes=("_mentor", "_mentoree")
#     )

#     # Merge mentorships with members to get mentor details
#     merged_df = mentorships_df.merge(
#         members_df, left_on="mentor_uuid", right_on="uuid", suffixes=("_mentorship", "_mentor")
#     ).merge(
#         members_df, left_on="mentoree_uuid", right_on="uuid", suffixes=("_mentorship", "_mentoree")
#     )


#     incorrect_mentorships = merged_df[
#         (merged_df["age_mentor"] < 40) | (merged_df["registered_date_mentor"] > "2004-01-01") |
#         (merged_df["age_mentoree"] > 30)
#     ]
    
#     discrepancies["incorrect_mentorships"] = incorrect_mentorships[
#         ["mentor_uuid", "mentoree_uuid", "age_mentor", "age_mentoree"]
#     ].to_dict(orient="records")

#     # Print results for discussion
#     print("\n=== Data Discrepancies Summary ===")
#     for key, value in discrepancies.items():
#         if value:
#             print(f"{key}: {value}")
#         else:
#             print(f"{key}: No issues found ✅")

#     return discrepancies
