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

def register():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        _json = request.json
        _Username = _json['Username']
        _Password = sha512_crypt.encrypt(_json['Password'])
        _Voornaam = _json['Voornaam']
        _Achternaam = _json['Achternaam']
        _Geslacht = _json['Geslacht']
        _Adres = _json['Adres']
        _Telefoon = _json['Telefoon']
        _Email = _json['Email']
        _Geboortedatum = _json['Geboortedatum']
        _Betaling = _json['Betaling']
        _Aflever = _json['Aflever']
        
        if _Username and _Password:
            cursor.execute('SELECT * FROM users WHERE Username = %s', _Username)
            account = cursor.fetchone()
        if account:
            response = jsonify('BESTAAT')
            return response 
        if  _Username and _Password and _Voornaam and _Achternaam and _Geslacht and _Adres and _Telefoon and _Email and _Geboortedatum and _Betaling and _Aflever and request.method == 'POST':
            sqlQuery = "INSERT INTO users(Username, Password, Voornaam, Achternaam, Geslacht, Adres, Telefoon, Email, Geboortedatum, Betaling, Aflever) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_Username, _Password, _Voornaam, _Achternaam, _Geslacht, _Adres, _Telefoon, _Email, _Geboortedatum, _Betaling, _Aflever)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('SUCCES')
            response.status_code = 200
            return response 
        else: 
            response = jsonify('FAIL')
            return response 
    except Exception as e:
            print(e)
    finally:
        cursor.close() 
        conn.close()  
    