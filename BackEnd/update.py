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

def update():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        _json = request.json
        _ID = _json['ID']

        if(_json['Adres']):
            _Adres = _json['Adres']
            sqlQuery = "UPDATE users SET Adres=%s WHERE ID=%s"
            bindData = (_Adres, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['Telefoon']):
            _Telefoon = _json['Telefoon']
            sqlQuery = "UPDATE users SET Telefoon=%s WHERE ID=%s"
            bindData = (_Telefoon, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['Email']):
            _Email = _json['Email']
            sqlQuery = "UPDATE users SET Email=%s WHERE ID=%s"
            bindData = (_Email, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['Betaling']):
            _Betaling = _json['Betaling']
            sqlQuery = "UPDATE users SET Betaling=%s WHERE ID=%s"
            bindData = (_Betaling, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['Aflever']):
            _Aflever = _json['Aflever']
            sqlQuery = "UPDATE users SET Aflever=%s WHERE ID=%s"
            bindData = (_Aflever, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['Password']):
            _Password = sha512_crypt.encrypt(_json['Password'])
            sqlQuery = "UPDATE users SET Password=%s WHERE ID=%s"
            bindData = (_Password, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(not _json['Adres'] and not _json['Telefoon'] and not _json['Email'] and not _json['Betaling'] and not _json['Aflever'] and not _json['Password']):
            response = jsonify('FAIL')
            return response 
        else: 
            response = jsonify('SUCCES')
            return response 
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  