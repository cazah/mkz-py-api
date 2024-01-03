from flask import Flask, jsonify, request
import mysql.connector
from config import DB_CONFIG
from models.blog import Blog
def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)


def getBlogPosts():
    try:
        db = get_db_connection()
        cur = db.cursor()
        cur.execute('SELECT * FROM blogs;')
        data = cur.fetchall()

        # Convert the data to a list of dictionaries for jsonify
        result = [Blog(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]) for row in data]
        blog_list = [blog.to_dict() for blog in result]
        return jsonify(blog_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

    finally:
        # Close the cursor and database connection in the finally block
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

def addBlogPost(data):
    try:
        # Extract data from the request
        topic = data.get('topic')
        title = data.get('title')
        shortdesc = data.get('shortdesc')
        image = data.get('image')
        imagetitle = data.get('imagetitle')
        imagedesc = data.get('imagedesc')
        socialmedias = data.get('socialmedias')
        introduction = data.get('introduction')
        content = data.get('content')
        conclution = data.get('conclution')

        # Perform database insertion
        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'INSERT INTO blogs (topic, title, shortdesc, image, imagetitle, imagedesc, socialmedias, introduction, content, conclution) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (topic, title, shortdesc, image, imagetitle, imagedesc, socialmedias, introduction, content, conclution))

        db.commit()

        # Return success response
        response = {'message': 'Blog post added successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code

def updateBlogPost(data, id):
    try:
        # Extract data from the request
        topic = data.get('topic')
        title = data.get('title')
        shortdesc = data.get('shortdesc')
        image = data.get('image')
        imagetitle = data.get('imagetitle')
        imagedesc = data.get('imagedesc')
        socialmedias = data.get('socialmedias')
        introduction = data.get('introduction')
        content = data.get('content')
        conclution = data.get('conclution')

        db = get_db_connection()
        cur = db.cursor()
        cur.execute(
            'UPDATE blogs SET topic=%s, title=%s, shortdesc=%s, image=%s, imagetitle=%s, imagedesc=%s, socialmedias=%s, introduction=%s, content=%s, conclution=%s WHERE id=%s',
            (topic, title, shortdesc, image, imagetitle, imagedesc, socialmedias, introduction, content, conclution, id))
        db.commit()

        # Return success response
        response = {'message': 'Blog post updated successfully'}
        return jsonify(response), 201  # 201 Created status code

    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code



def deleteBlogPost(id):
    try:
        # Perform database deletion
        db = get_db_connection()
        cur = db.cursor()

        # Execute the DELETE statement
        cur.execute('DELETE FROM blogs WHERE id = %s', (id,))

        # Commit the changes
        db.commit()

        # Return success response
        response = {'message': f'Blog item with ID {id} deleted successfully'}
        return jsonify(response)
    except Exception as e:
        # Handle errors appropriately (log or return an error response)
        response = {'error': str(e)}
        return jsonify(response), 500  # 500 Internal Server Error status code
