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

# In models.py, add these new functions:

def get_all_users():
    """Retrieve all users from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_user(user_id):
    """Retrieve a single user by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        return user
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_user(user_id, full_name, age, email, city):
    """Update user information in the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE users SET full_name = %s, age = %s, email = %s, city = %s WHERE id = %s"
        values = (full_name, age, email, city, user_id)
        cursor.execute(query, values)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def delete_user(user_id):
    """Delete a user from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()