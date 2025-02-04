import pytest
import pandas as pd
from mentorship_app.mentorship import assign_mentorships

@pytest.fixture
def sample_members():
    return pd.DataFrame([
        {"uuid": "mentor-1", "fullname": "Alice Smith", "email": "alice@example.com", "age": 45, "gender": "female", "id_value": "ID1", "registered_date": "2003-06-01", "address": "123 Street, Toronto"},
        {"uuid": "mentor-2", "fullname": "Lisa Brown", "email": "lisa@example.com", "age": 50, "gender": "female", "id_value": "ID2", "registered_date": "2001-04-15", "address": "789 Ave, Ottawa"},
        {"uuid": "mentoree-1", "fullname": "Bob Jones", "email": "bob@example.com", "age": 25, "gender": "male", "id_value": "ID3", "registered_date": "2015-09-12", "address": "456 Ave, Vancouver"},
        {"uuid": "mentoree-2", "fullname": "Charlie Black", "email": "charlie@example.com", "age": 28, "gender": "male", "id_value": "ID4", "registered_date": "2013-06-24", "address": "101 St, Calgary"},
    ])

def test_assign_mentorships(sample_members):
    mentorships_df = assign_mentorships(sample_members)
    
    assert len(mentorships_df) == 2  # 2 mentorees should be assigned
    assert set(mentorships_df["mentor_uuid"]) == {"mentor-1", "mentor-2"}
