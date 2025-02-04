import os
import time
from sqlalchemy import create_engine, Column, String, Integer, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class MemberDB(Base):
    __tablename__ = "members"

    uuid = Column(String, primary_key=True)
    fullname = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # Enforce uniqueness
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    id = Column(String, nullable=False)
    registered_date = Column(DateTime, nullable=False)
    address = Column(String, nullable=False)

    __table_args__ = (UniqueConstraint('email', name='unique_email_constraint'),)

class MentorshipDB(Base):
    __tablename__ = "mentorships"
    uuid = Column(String, primary_key=True)
    mentor_uuid = Column(String)
    mentoree_uuid = Column(String)

# Base.metadata.create_all(engine)

