from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.carousel import Corousel  # Assuming you have a Corousel model defined

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_corousels():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM corousels;')
        data = cur.fetchall()

        result = [Corousel(row[0], row[1], row[2], row[3], row[4]) for row in data]
        corousel_list = [corousel.to_dict() for corousel in result]
        return jsonify(corousel_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def add_corousel(data):
    try:
        # data = request.get_json()

        # Extract data from the request
        title = data.get('title')
        content = data.get('content')
        image = data.get('image')
        link = data.get('link')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO corousels (title, content, image, link) VALUES (%s, %s, %s, %s)',
            (title, content, image, link)
        )

        db.commit()

        response = {'message': 'Corousel added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def update_corousel(data,corousel_id):
    try:
        # data = request.get_json()

        # Extract data from the request
        title = data.get('title')
        content = data.get('content')
        image = data.get('image')
        link = data.get('link')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE corousels SET title=%s, content=%s, image=%s, link=%s WHERE id=%s',
            (title, content, image, link, corousel_id)
        )
        db.commit()

        response = {'message': 'Corousel updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def delete_Coursel(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM corousels WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'Coursel item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code
