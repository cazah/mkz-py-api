from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.servicePage import ServicePage
app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_service_pages():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM service_pages;')
        data = cur.fetchall()

        result = [ServicePage(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) for row in data]
        service_page_list = [service_page.to_dict() for service_page in result]
        return jsonify(service_page_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def add_service_page(data):
    try:
        # data = request.get_json()

        # Extract data from the request
        topic = data.get('topic')
        title = data.get('title')
        introduction = data.get('introduction')
        content = data.get('content')
        makizh_amc_service_json = data.get('makizh_amc_service_json')
        makizh_amc_service_note = data.get('makizh_amc_service_note')
        amc_service_json = data.get('amc_service_json')
        amc_service_note = data.get('amc_service_note')
        package_table = data.get('package_table')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO service_pages (topic, title, introduction, content, makizh_amc_service_json, makizh_amc_service_note, amc_service_json, amc_service_note, package_table) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (topic, title, introduction, content, makizh_amc_service_json, makizh_amc_service_note, amc_service_json, amc_service_note, package_table)
        )

        db.commit()

        response = {'message': 'Service page added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def update_service_page(data,page_id):
    try:
        # data = request.get_json()

        # Extract data from the request
        topic = data.get('topic')
        title = data.get('title')
        introduction = data.get('introduction')
        content = data.get('content')
        makizh_amc_service_json = data.get('makizh_amc_service_json')
        makizh_amc_service_note = data.get('makizh_amc_service_note')
        amc_service_json = data.get('amc_service_json')
        amc_service_note = data.get('amc_service_note')
        package_table = data.get('package_table')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE service_pages SET topic=%s, title=%s, introduction=%s, content=%s, makizh_amc_service_json=%s, makizh_amc_service_note=%s, amc_service_json=%s, amc_service_note=%s, package_table=%s WHERE id=%s',
            (topic, title, introduction, content, makizh_amc_service_json, makizh_amc_service_note, amc_service_json, amc_service_note, package_table, page_id)
        )
        db.commit()

        response = {'message': 'Service page updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def delete_service_page(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM service_pages WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'service pages item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code