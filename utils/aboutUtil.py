from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.aboutus import Aboutus  # Assuming you have an Aboutus model defined

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def get_aboutus():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM aboutus;')
        data = cur.fetchall()

        result = [Aboutus(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]) for row in data]
        aboutus_list = [aboutus.to_dict() for aboutus in result]
        return jsonify(aboutus_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def add_aboutus(data):
    try:
        # data = request.get_json()

        # Extract data from the request
        companyname = data.get('companyname')
        info = data.get('info')
        visioncontent = data.get('visioncontent')
        empowercontent = data.get('empowercontent')
        costcontent = data.get('costcontent')
        missioncontent = data.get('missioncontent')
        valuescontent = data.get('valuescontent')
        principlecontent = data.get('principlecontent')
        principlekey = data.get('principlekey')
        integrity = data.get('integrity')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO aboutus (companyname, info, visioncontent, empowercontent, costcontent, missioncontent, valuescontent, principlecontent, principlekey, integrity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (companyname, info, visioncontent, empowercontent, costcontent, missioncontent, valuescontent, principlecontent, principlekey, integrity)
        )

        db.commit()

        response = {'message': 'Aboutus added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def update_aboutus(data,aboutus_id):
    try:
        # data = request.get_json()

        # Extract data from the request
        companyname = data.get('companyname')
        info = data.get('info')
        visioncontent = data.get('visioncontent')
        empowercontent = data.get('empowercontent')
        costcontent = data.get('costcontent')
        missioncontent = data.get('missioncontent')
        valuescontent = data.get('valuescontent')
        principlecontent = data.get('principlecontent')
        principlekey = data.get('principlekey')
        integrity = data.get('integrity')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE aboutus SET companyname=%s, info=%s, visioncontent=%s, empowercontent=%s, costcontent=%s, missioncontent=%s, valuescontent=%s, principlecontent=%s, principlekey=%s, integrity=%s WHERE id=%s',
            (companyname, info, visioncontent, empowercontent, costcontent, missioncontent, valuescontent, principlecontent, principlekey, integrity, aboutus_id)
        )
        db.commit()

        response = {'message': 'Aboutus updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code
