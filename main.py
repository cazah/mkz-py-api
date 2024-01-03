from flask import Flask, jsonify
import mysql.connector
from config import DB_CONFIG
app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    try:
        db = get_db_connection()

        cur1 = db.cursor()
        cur1.execute('SELECT * FROM student;')
        data = cur1.fetchall()

        # Convert the data to a list of dictionaries for jsonify
        result = [{'id': row[0], 'name': row[1], 'age': row[2]} for row in data]

        return jsonify(result)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the cursor and database connection in the finally block
        if 'cur1' in locals():
            cur1.close()
        if 'db' in locals():
            db.close()

if __name__ == '__main__':
    app.run(debug=True)