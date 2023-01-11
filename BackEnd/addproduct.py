from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

from config import *

# app = Flask(__name__)
# app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# CORS(app)

# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = ''
# app.config['MYSQL_DATABASE_DB'] = 'webshopusers'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)

def add():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        _json = request.json
        _naam = _json['naam']
        _categorie = _json['categorie']
        _prijs= _json['prijs']
        _sterren = _json['sterren']
        _leverbaar = _json['leverbaar']
        _afbeelding_url = _json['afbeelding_url']
        
        if  _naam and _categorie and _prijs and _sterren and _leverbaar and _afbeelding_url and request.method == 'POST':
            sqlQuery = "INSERT INTO producten(naam, categorie, prijs, sterren, leverbaar, afbeelding_url) VALUES(%s, %s, %s, %s, %s, %s)"
            bindData = (_naam, _categorie, _prijs, _sterren, _leverbaar, _afbeelding_url)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('SUCCES')
            return response 
        else: 
            response = jsonify('FAIL')
            return response 
    except Exception as e:
            print(e)
    finally:
        cursor.close() 
        conn.close()  