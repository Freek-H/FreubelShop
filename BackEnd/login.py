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

def login():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        _json = request.json
        _Username = _json['Username']
        _Password = _json['Password']
        
        if _Username and _Password:
            cursor.execute('SELECT * FROM users WHERE Username = %s', _Username)
            account = cursor.fetchone()
            if account:
                if sha512_crypt.verify(_Password, account['Password']):
                    response = jsonify('SUCCES')
                    return response 
                else:
                    response = jsonify('FAIL')
                    return response        
        else:
            response = jsonify('FAIL')
            return response   
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  