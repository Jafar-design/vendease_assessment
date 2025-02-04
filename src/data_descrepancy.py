import pandas as pd

def check_data_discrepancy(members_df, mentorships_df):
    """
    Check for discrepancies in the mentorship project data.
    
    Parameters:
    - members_df (pd.DataFrame): DataFrame containing member data.
    - mentorships_df (pd.DataFrame): DataFrame containing mentorships.

    Returns:
    - dict: A report summarizing any discrepancies found.
    """

    discrepancy_report = {}

    # 🔹 1. Check for Missing Values
    missing_members = members_df.isnull().sum()
    missing_mentorships = mentorships_df.isnull().sum()
    discrepancy_report["missing_values"] = {
        "members": missing_members[missing_members > 0].to_dict(),
        "mentorships": missing_mentorships[missing_mentorships > 0].to_dict(),
    }

    # 🔹 2. Check for Duplicate UUIDs
    duplicate_members = members_df["uuid"].duplicated().sum()
    duplicate_mentorships = mentorships_df[["mentor_uuid", "mentoree_uuid"]].duplicated().sum()
    discrepancy_report["duplicate_entries"] = {
        "members": duplicate_members,
        "mentorships": duplicate_mentorships,
    }

    # 🔹 3. Verify Mentorship Pairs Exist in Members
    valid_mentors = set(members_df["uuid"])
    invalid_mentors = mentorships_df[~mentorships_df["mentor_uuid"].isin(valid_mentors)]["mentor_uuid"].tolist()
    invalid_mentorees = mentorships_df[~mentorships_df["mentoree_uuid"].isin(valid_mentors)]["mentoree_uuid"].tolist()
    discrepancy_report["invalid_mentorships"] = {
        "invalid_mentors": invalid_mentors,
        "invalid_mentorees": invalid_mentorees,
    }

    # 🔹 4. Validate Mentor Eligibility (Age & Registration Date)
    mentors = members_df[
        (members_df["age"] >= 40) & (members_df["registered_date"] <= "2004-01-01")
    ]["uuid"]
    invalid_mentors = mentorships_df[~mentorships_df["mentor_uuid"].isin(mentors)]["mentor_uuid"].tolist()
    discrepancy_report["invalid_mentors"] = invalid_mentors

    # 🔹 5. Validate Mentoree Eligibility (Age ≤ 30)
    mentorees = members_df[members_df["age"] <= 30]["uuid"]
    invalid_mentorees = mentorships_df[~mentorships_df["mentoree_uuid"].isin(mentorees)]["mentoree_uuid"].tolist()
    discrepancy_report["invalid_mentorees"] = invalid_mentorees

    # 🔹 6. Check for Unassigned Mentorees
    assigned_mentorees = set(mentorships_df["mentoree_uuid"])
    unassigned_mentorees = set(mentorees) - assigned_mentorees
    discrepancy_report["unassigned_mentorees"] = list(unassigned_mentorees)

    print("\n=== Data Discrepancies Summary ===")
    for key, value in discrepancy_report.items():
        if value:
            print(f"{key}: {value}")
        else:
            print(f"{key}: No issues found ✅")


    return discrepancy_report


# Example Usage:
# Assuming you have members_df and mentorships_df already created
# report = check_data_discrepancy(members_df, mentorships_df)
# print(report)
