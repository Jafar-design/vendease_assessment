import os
import time
import psycopg2

DATABASE_URL = os.getenv("DATABASE_URL")

def drop_tables():
    retries = 5
    for attempt in range(retries):
        try:
            conn = psycopg2.connect(DATABASE_URL)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS mentorships, members CASCADE;")
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ Tables dropped successfully.")
            return
        except psycopg2.OperationalError as e:
            print(f"🔄 Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(5)
    
    print("❌ Failed to drop tables after multiple attempts.")

if __name__ == "__main__":
    drop_tables()