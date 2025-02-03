from models import Mentorship
from utils import create_members
from datetime import datetime

def assign_mentorships():
    members = create_members()

    mentors = [m for m in members if m.gender == 'female' and m.age >= 40 and m.registered_date <= datetime(2004, 1, 1)]
    mentorees = [m for m in members if m.age <= 30]

    mentors.sort(key=lambda m: m.registered_date)
    mentorees.sort(key=lambda m: m.registered_date)

    mentorships = []
    mentor_index = 0
    for mentoree in mentorees:
        mentor = mentors[mentor_index]
        mentorships.append(Mentorship.create(mentor, mentoree))
        mentor_index = (mentor_index + 1) % len(mentors)

    return mentorships

if __name__ == "__main__":
    mentorships = assign_mentorships()
    print(mentorships[:5])  # Preview first 5 mentorships
