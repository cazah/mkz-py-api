from flask import Flask, jsonify,request
import mysql.connector
from config import DB_CONFIG
from models.gallery import Gallery

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def getGallery():
    try:
        db = get_db_connection()
        cur1 = db.cursor()
        cur1.execute('SELECT * FROM gallery;')
        data = cur1.fetchall()
        # Convert the data to a list of dictionaries for jsonify
        result = [Gallery(row[0], row[1]) for row in data]
        gallery_list = [gallery.to_dict() for gallery in result]
        return jsonify(gallery_list)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the cursor and database connection in the finally block
        if 'cur1' in locals():
            cur1.close()
        if 'db' in locals():
            db.close()

def addgallery(data):
    try:
        # Assuming the request contains JSON data like {"image": "base64Str"}
        # data = request.get_json()

        # Extract data from the request
        imageStr = data.get('image')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('INSERT INTO gallery (image) VALUES (%s)', (imageStr,))
        db.commit()

        # Return success response
        response = {'message': 'Gallery added successfully'}
        return jsonify(response), 201  # 201 Created status code
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def deleteGallery(gallery_id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM gallery WHERE id = %s', (gallery_id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'Gallery item with ID {gallery_id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code
