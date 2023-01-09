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

def product_delete(productID):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("DELETE FROM producten WHERE productID =%s", productID)
        conn.commit()
        response = jsonify('SUCCES')
        return response 
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  