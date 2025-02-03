from database import SessionLocal
from sqlalchemy import text

#Solution to Question 
def median_age_of_male_mentorees():
    session = SessionLocal()
    query = text("""
        SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY age)
        FROM members
        WHERE gender = 'male' AND registered_date >= '2010-01-01'
    """)
    result = session.execute(query).scalar()
    session.close()
    return result
