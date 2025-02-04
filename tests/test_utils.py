import pytest
import pandas as pd
from mentorship_app.utils import check_data_discrepancy

@pytest.fixture
def sample_data():
    members_data = [
        {"uuid": "mentor-1", "fullname": "Alice Smith", "email": "alice@example.com", "age": 45, "gender": "female", "id_value": "ID1", "registered_date": "2003-06-01", "address": "123 Street, Toronto"},
        {"uuid": "mentoree-1", "fullname": "Bob Jones", "email": "bob@example.com", "age": 25, "gender": "male", "id_value": "ID2", "registered_date": "2015-09-12", "address": "456 Ave, Vancouver"},
    ]
    
    mentorships_data = [
        {"uuid": "mentorship-1", "mentor_uuid": "mentor-1", "mentoree_uuid": "mentoree-1"}
    ]
    
    members_df = pd.DataFrame(members_data)
    mentorships_df = pd.DataFrame(mentorships_data)
    
    return members_df, mentorships_df

def test_check_data_discrepancy(sample_data):
    members_df, mentorships_df = sample_data

    result = check_data_discrepancy(members_df, mentorships_df)

    assert isinstance(result, dict)
    assert result["missing_values"] == {"members": {}, "mentorships": {}}
    assert result["duplicate_entries"]["members"] == 0
    assert result["invalid_mentorships"]["invalid_mentors"] == []
    assert result["invalid_mentorships"]["invalid_mentorees"] == []
