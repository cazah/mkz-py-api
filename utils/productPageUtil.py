from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.productPage import ProductPage  # Assuming you have a ProductPage model defined

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_product_pages():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM product_pages;')
        data = cur.fetchall()

        result = [ProductPage(row[0], row[1], row[2], row[3], row[4]) for row in data]
        product_page_list = [product_page.to_dict() for product_page in result]
        return jsonify(product_page_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def add_product_page(data):
    try:
        # data = request.get_json()

        # Extract data from the request
        details = data.get('details')
        content = data.get('content')
        quote_content = data.get('quote_content')
        extra_content = data.get('extra_content')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO product_pages (details, content, quote_content, extra_content) VALUES (%s, %s, %s, %s)',
            (details, content, quote_content, extra_content)
        )

        db.commit()

        response = {'message': 'Product page added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def update_product_page(data,page_id):
    try:
        # data = request.get_json()

        # Extract data from the request
        details = data.get('details')
        content = data.get('content')
        quote_content = data.get('quote_content')
        extra_content = data.get('extra_content')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
                'UPDATE product_pages SET details=%s, content=%s, quote_content=%s, extra_content=%s WHERE id=%s',
            (details, content, quote_content, extra_content, page_id)
        )
        db.commit()

        response = {'message': 'Product page updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def delete_product_page(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM product_pages WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'product pages item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code