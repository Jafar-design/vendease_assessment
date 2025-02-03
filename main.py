from app.api import fetch_users
from app.mentorship import generate_mentorships
from app.db import create_tables
from app.analysis import calculate_median_age, count_mentorees_by_senior_mentors

create_tables()
mentors, mentorees = fetch_users()
mentorships = generate_mentorships(mentors, mentorees)

print(f"Median Age of Male Mentorees: {calculate_median_age()}")
count_mentorees_by_senior_mentors()
