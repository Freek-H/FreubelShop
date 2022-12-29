from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'webshopusers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def delete(user_ID):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("DELETE FROM users WHERE ID =%s", user_ID)
        conn.commit()
        response = jsonify('SUCCES')
        response.status_code = 200
        return response 
    except Exception:
            response = jsonify('Verwijderen mislukt!')
            return response
    finally:
        cursor.close() 
        conn.close()  