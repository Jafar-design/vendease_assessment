import os
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class MemberDB(Base):
    __tablename__ = "members"
    uuid = Column(String, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    age = Column(Integer)
    gender = Column(String)
    id = Column(String)
    registered_date = Column(DateTime)
    address = Column(String)

class MentorshipDB(Base):
    __tablename__ = "mentorships"
    uuid = Column(String, primary_key=True)
    mentor_uuid = Column(String)
    mentoree_uuid = Column(String)

# Base.metadata.create_all(engine)

def drop_tables():
    """
    Drops the 'members' and 'mentorships' tables from the PostgreSQL database using DATABASE_URL.
    """
    if not DATABASE_URL:
        print("❌ DATABASE_URL is not set. Please check your environment variables.")
        return

    try:
        # Connect to PostgreSQL using DATABASE_URL
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        
        # Drop tables safely
        cur.execute("DROP TABLE IF EXISTS mentorships;")
        cur.execute("DROP TABLE IF EXISTS members;")
        
        # Commit changes and close connection
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Tables dropped successfully.")

    except Exception as e:
        print(f"❌ Error dropping tables: {e}")
