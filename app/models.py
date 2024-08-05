import mysql.connector
from app import app

def get_db_connection():
    """Establish a database connection using configuration parameters"""
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

def save_user(full_name, age, email, city):
    """Save user information to the database"""
    try:
        # Establish database connection
        conn = get_db_connection()
        cursor = conn.cursor()

        # Prepare SQL query
        query = "INSERT INTO users (full_name, age, email, city) VALUES (%s, %s, %s, %s)"
        values = (full_name, age, email, city)

        # Execute the query
        cursor.execute(query, values)

        # Commit the transaction
        conn.commit()
        return True
    except mysql.connector.Error as err:
        # Log the error (in a real application, use proper logging)
        print(f"Database error: {err}")
        return False
    finally:
        # Ensure database connection is closed
        if conn.is_connected():
            cursor.close()
            conn.close()