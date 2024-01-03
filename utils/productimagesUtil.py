from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.productimages import ProductImage  # Assuming you have a ProductImage model defined

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_product_images():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM product_images;')
        data = cur.fetchall()

        result = [ProductImage(row[0], row[1], row[2], row[3]) for row in data]
        product_image_list = [product_image.to_dict() for product_image in result]
        return jsonify(product_image_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def add_product_image(data):
    try:
        # data = request.get_json()

        # Extract data from the request
        title = data.get('title')
        image = data.get('image')
        category = data.get('category')  # Assuming you have a 'category' attribute

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO product_images (title, image, category) VALUES (%s, %s, %s)',
            (title, image, category)
        )

        db.commit()

        response = {'message': 'Product image added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def update_product_image(data,image_id):
    try:
        # data = request.get_json()

        # Extract data from the request
        title = data.get('title')
        image = data.get('image')
        category = data.get('category')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE product_images SET title=%s, image=%s, category=%s WHERE id=%s',
            (title, image, category, image_id)
        )
        db.commit()

        response = {'message': 'Product image updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def delete_product_image(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM product_images WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'Product images item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code