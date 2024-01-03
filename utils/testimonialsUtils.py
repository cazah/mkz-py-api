from flask import Flask, jsonify,request
import mysql.connector
from config import DB_CONFIG
from models.testimonial import Testinonial

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def getTestimonials():
    try:
        db = get_db_connection()
        cur1 = db.cursor()
        cur1.execute('SELECT * FROM testimonials;')
        data = cur1.fetchall()
        # Convert the data to a list of dictionaries for jsonify
        result = [Testinonial(row[0], row[1],row[2],row[3]) for row in data]
        list = [bean.to_dict() for bean in result]
        return jsonify(list)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the cursor and database connection in the finally block
        if 'cur1' in locals():
            cur1.close()
        if 'db' in locals():
            db.close()


def addTestimonial(data):
    try:
        # Assuming the request contains JSON data like {"image": "base64Str"}
        # data = request.get_json()

        # Extract data from the request
        name = data.get('name')
        message = data.get('message')
        type = data.get('type')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO testimonials (name, message, type) VALUES (%s, %s, %s)',
            (name, message, type))

        db.commit()

        # Return success response
        response = {'message': 'Testimonial added successfully'}
        return jsonify(response), 201  # 201 Created status code
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code



def updateTestimonial(data,id):
    try:
        name = data.get('name')
        message = data.get('message')
        type = data.get('type')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE testimonials SET name=%s, message=%s, type=%s WHERE id=%s',
            (name, message, type, id))
        db.commit()

        # Return success response
        response = {'message': 'Testimonials Updated successfully'}
        return jsonify(response), 201  # 201 Created status code
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def deleteTestimonial(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM testimonials WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'Testimonials item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code