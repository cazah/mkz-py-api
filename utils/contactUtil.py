from flask import Flask, jsonify,request
import mysql.connector
from config import DB_CONFIG
from models.contact import Contact
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def getContactus():
    try:
        db = get_db_connection()
        cur1 = db.cursor()
        cur1.execute('SELECT * FROM contactus;')
        data = cur1.fetchall()
        # Convert the data to a list of dictionaries for jsonify
        result = [Contact(row[0], row[1],row[2],row[3], row[4],row[5],row[6], row[7],row[8]) for row in data]
        list = [contacts.to_dict() for contacts in result]
        return jsonify(list)

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        # Close the cursor and database connection in the finally block
        if 'cur1' in locals():
            cur1.close()
        if 'db' in locals():
            db.close()

def addContact(data):
    try:
        # Assuming the request contains JSON data like {"image": "base64Str"}
        # data = request.get_json()

        # Extract data from the request
        name = data.get('name')
        subname = data.get('subname')
        email = data.get('email')

        logo = data.get('logo')
        phones = data.get('phones')
        socialmedias = data.get('socialmedias')

        address = data.get('address')
        location = data.get('location')


        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO contactus (name, subname, email, logo, phones, socialmedias, address, location) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            (name, subname, email,
             logo, phones, socialmedias,
             address, location))

        db.commit()

        # Return success response
        response = {'message': 'Contact us added successfully'}
        return jsonify(response), 201  # 201 Created status code
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code


def updateContact(data,id):
    try:
        name = data.get('name')
        subname = data.get('subname')
        email = data.get('email')

        logo = data.get('logo')
        phones = data.get('phones')
        socialmedias = data.get('socialmedias')

        address = data.get('address')
        location = data.get('location')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE contactus SET name=%s, subname=%s, email=%s, logo=%s, phones=%s, socialmedias=%s, address=%s, location=%s WHERE id=%s',
            (name, subname, email, logo,
             phones, socialmedias, address,
             location, id))
        db.commit()

        # Return success response
        response = {'message': 'Contact us Updated successfully'}
        return jsonify(response), 201  # 201 Created status code
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code