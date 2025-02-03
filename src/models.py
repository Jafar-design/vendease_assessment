from pydantic import BaseModel
from uuid import uuid4
from datetime import datetime

class Member(BaseModel):
    uuid: str
    fullname: str
    email: str
    age: int
    gender: str
    id: str
    registered_date: datetime
    address: str

    @staticmethod
    def from_api(data):
        return Member(
            uuid=data['login']['uuid'],
            fullname=f"{data['name']['first']} {data['name']['last']}",
            email=data['email'],
            age=data['dob']['age'],
            gender=data['gender'],
            id=data['id']['value'] or "N/A",
            registered_date=datetime.fromisoformat(data['registered']['date'].replace("Z", "")),
            address=f"{data['location']['street']['number']} {data['location']['street']['name']}, {data['location']['city']} {data['location']['postcode']}"
        )

class Mentorship(BaseModel):
    uuid: str
    mentor_uuid: str
    mentoree_uuid: str

    @staticmethod
    def create(mentor, mentoree):
        return Mentorship(uuid=str(uuid4()), mentor_uuid=mentor.uuid, mentoree_uuid=mentoree.uuid)

