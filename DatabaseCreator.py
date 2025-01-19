import mysql.connector
import re

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Esc@lier8282",  # Replace with your MySQL password
    database="breached_data"  # Replace with your database name
)

cursor = db.cursor()

# File path
file_path = "processed_file.txt"

# Insert query
query = "INSERT INTO users (url, username, password) VALUES (%s, %s, %s)"

# Regular expression pattern to match the URL, username, and password
pattern = re.compile(r'^(https?://[^:]+):([^:]+):(.+)$')

# Initialize a counter
inserted_count = 0

# Read the file and process data
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:  # Skip empty lines
                match = pattern.match(line)
                if match:
                    url, username, password = match.groups()
                    # Insert into the database
                    cursor.execute(query, (url, username, password))
                    inserted_count += 1
                else:
                    print(f"Line format is incorrect and will be skipped: {line}")

    # Commit all changes to the database
    db.commit()
    print(f"Inserted {inserted_count} records successfully!")

except FileNotFoundError:
    print(f"File {file_path} not found!")
except mysql.connector.Error as db_err:
    print(f"Database error occurred: {db_err}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    # Close the database connection
    cursor.close()
    db.close()
