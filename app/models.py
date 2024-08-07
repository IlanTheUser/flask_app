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

def save_user(full_name, age, skill_level, country, motorcycle):
<<<<<<< HEAD
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO riders (full_name, age, skill_level, country, motorcycle) VALUES (%s, %s, %s, %s, %s)"
        values = (full_name, age, skill_level, country, motorcycle)
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

def get_all_users():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM riders")
        riders = cursor.fetchall()
        return riders
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def get_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM riders WHERE id = %s", (user_id,))
        rider = cursor.fetchone()
        return rider
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
=======
    """Save rider information to the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Updated query to include new fields
        query = "INSERT INTO riders (full_name, age, skill_level, country, motorcycle) VALUES (%s, %s, %s, %s, %s)"
        values = (full_name, age, skill_level, country, motorcycle)

        cursor.execute(query, values)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
>>>>>>> parent of dd95ca3 (Added background and changed html files)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

<<<<<<< HEAD
def update_user(user_id, full_name, age, skill_level, country, motorcycle):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "UPDATE riders SET full_name = %s, age = %s, skill_level = %s, country = %s, motorcycle = %s WHERE id = %s"
        values = (full_name, age, skill_level, country, motorcycle, user_id)
        cursor.execute(query, values)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
=======
def get_all_users():
    """Retrieve all registered riders from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM riders")  # Updated table name to 'riders'
        riders = cursor.fetchall()
        return riders
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return []
>>>>>>> parent of dd95ca3 (Added background and changed html files)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

<<<<<<< HEAD
def delete_user(user_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM riders WHERE id = %s", (user_id,))
=======
def get_user(user_id):
    """Retrieve a single rider by ID"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM riders WHERE id = %s", (user_id,))  # Updated table name to 'riders'
        rider = cursor.fetchone()
        return rider
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def update_user(user_id, full_name, age, skill_level, country, motorcycle):
    """Update rider information in the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Updated query to include new fields
        query = "UPDATE riders SET full_name = %s, age = %s, skill_level = %s, country = %s, motorcycle = %s WHERE id = %s"
        values = (full_name, age, skill_level, country, motorcycle, user_id)
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
    """Delete a rider from the database"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM riders WHERE id = %s", (user_id,))  # Updated table name to 'riders'
>>>>>>> parent of dd95ca3 (Added background and changed html files)
        conn.commit()
        return True
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()