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
        ##_Username = _json['Username']
        ##_Password = sha512_crypt.encrypt(_json['Password'])
        ##_Voornaam = _json['Voornaam']
        ##_Achternaam = _json['Achternaam']
        ## _Geslacht = _json['Geslacht']
        _Telefoon = _json['Telefoon']
        _Adres = _json['Adres']
        _Email = _json['Email']
       ## _Geboortedatum = _json['Geboortedatum']
        _Betaling = _json['Betaling']
        _Aflever = _json['Aflever']
        if _Adres and _Telefoon and _Email and _Betaling and _Aflever and _ID and request.method == 'PUT':
            sqlQuery = "UPDATE users SET Adres=%s, Telefoon=%s, Email=%s, Betaling=%s, Aflever=%s WHERE ID=%s"
            bindData = (_Adres, _Telefoon, _Email, _Betaling, _Aflever, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('SUCCES')
            response.status_code = 200
            return response 
    except Exception:
            response = jsonify('Niet alles is ingevuld!')
            return response
    finally:
        cursor.close() 
        conn.close()  