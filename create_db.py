import sqlite3

def create_db():
    # Connect to the SQLite database (this will create the database if it doesn't exist)
    con = sqlite3.connect("srms.db")
    cur = con.cursor()

    # Create the courses table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id INTEGER PRIMARY KEY AUTOINCREMENT,
            course_name TEXT NOT NULL,
            duration TEXT NOT NULL,
            charges REAL NOT NULL,
            description TEXT
        )
    """)

    # Create the students table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll TEXT PRIMARY KEY,  -- Unique student roll number
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            gender TEXT NOT NULL,
            dob TEXT NOT NULL,
            contact TEXT NOT NULL,
            course TEXT NOT NULL,
            admission_date TEXT NOT NULL
        )
    """)

    # Create the result table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            result_id INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT NOT NULL,
            name TEXT NOT NULL,
            course TEXT NOT NULL,
            marks_obtained TEXT NOT NULL,
            per TEXT NOT NULL,
            full_marks TEXT NOT NULL,
            FOREIGN KEY (roll) REFERENCES student(roll) ON DELETE CASCADE
        )
    """)

    # Commit the changes and close the connection
    con.commit()
    con.close()

# Call the function to create the database and tables
create_db()
