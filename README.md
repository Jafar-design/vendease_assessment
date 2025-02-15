# Mentorship Program

## 📌 Project Overview
This project is designed to facilitate a mentorship program for a community of 500 members in Canada. The program pairs mentors (experienced members) with mentorees (younger members) based on predefined criteria. The data is retrieved from the Random User Generator API, stored in a PostgreSQL database, and analyzed using Python and Pandas.

## 🎯 Objectives
- Collect 500 records from the Random User Generator API.
- Filter and classify members as mentors or mentorees.
- Assign mentorees to mentors based on the registration date.
- Store and manage data using PostgreSQL.
- Provide insights through data analysis and SQL queries.
- Dockerize the entire application for easy deployment.

---

## 🏗️ Project Structure
```
mentorship_project/
│── app/
│   ├── data_processing.py  # Functions to fetch and process API data
│   ├── models.py           # Member and Mentorship class definitions
│   ├── database.py         # PostgreSQL database connection setup
│   ├── mentorship_logic.py # Logic to pair mentors and mentorees
│   ├── analysis.py         # Functions for analysis and SQL queries
│   ├── discrepancy.py      # Function to check for data inconsistencies
│   ├── drop_tables.py      # Function to drop tables for reproducibility
│   ├── main.py             # Main script to run the application
│── docker-compose.yml      # Docker Compose setup for database and app
│── Dockerfile              # Docker configuration for the application
│── requirements.txt        # Python dependencies
│── README.md               # Project documentation
```

---

## 📥 Setup Instructions

### 1️⃣ Prerequisites
Ensure you have the following installed:
- Docker & Docker Compose
- Python 3.x

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Jafar-design/vendease_assessment.git
cd mentorship_project
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add your database URL:
```bash
DATABASE_URL=postgresql://username:password@db:5432/mentorship_db
```

### 4️⃣ Build and Run the Project
```bash
docker-compose up --build
```

---

## 🔄 Reproducibility
If you need to reset the database and start fresh, run:
```bash
docker-compose down -v
python drop_tables.py
```

---

## 🔍 Features Implemented
### ✅ Data Collection
- Retrieves 500 Canadian users from the API with `ca` nationality and seed `vendease`.
- *It should be noted that seed passed into the api did not produce the assumed data as indicated in the problem statement, i.e. user 1 was not Ariana Denys and user 500 was not Alexis Li*


### ✅ Data Processing
- The code checks for duplicate records of members and did found about 20 records duplicated, bringing the total record size to 480 members. This was implemented both on the database and dataframe levels in the `models.py` and `utils.py` respectively.
- I extracted relevant user information (UUID, name, age, gender, registration date, etc.).
- Filtered members based on mentorship criteria.


### ✅ Mentorship Pairing
- Assigned mentorees to mentors. This was enforced in the 

### ✅ Database Management
- Stores members and mentorships in PostgreSQL.
- The `models.py` file defines the structure of your database tables using SQLAlchemy ORM (Object-Relational Mapping). It translates Python objects into database tables and manages relationships between them.
- Allows querying mentorship statistics.

### ✅ Data Analysis
- Calculates the median age of male mentorees who registered after 2010.
- Finds the number of mentorees (by gender) mentored by a member aged 60 or older.

### ✅ Data Discrepancy Check
- Detects missing values, duplicate UUIDs, incorrect mentorship assignments, and invalid ages.

---

## 🛠️ How to Use
### 1️⃣ Run Data Collection & Processing
```bash
python main.py
```

### 2️⃣ Run Analysis Queries
```bash
python analysis.py
```

### 3️⃣ Check Data Discrepancies
```bash
python data_discrepancy.py
```

---

## 🚀 Future Improvements
- Improve error handling for API requests.
- Implement a web interface to visualize mentor-mentoree assignments.
- Add unit tests for validation.

---

## 🤝 Contributions
Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

## 📬 Contact
For any questions or suggestions, reach out via [your email] or open an issue on GitHub.

