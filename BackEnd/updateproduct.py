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

def product_update():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        _json = request.json
        _ID = _json['ID']

        if(_json['naam']):
            _naam = _json['naam']
            sqlQuery = "UPDATE producten SET naam=%s WHERE productID=%s"
            bindData = (_naam, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['categorie']):
            _categorie = _json['categorie']
            sqlQuery = "UPDATE producten SET categorie=%s WHERE productID=%s"
            bindData = (_categorie, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['prijs']):
            _prijs = _json['prijs']
            sqlQuery = "UPDATE producten SET prijs=%s WHERE productID=%s"
            bindData = (_prijs, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['sterren']):
            _sterren = _json['sterren']
            sqlQuery = "UPDATE producten SET sterren=%s WHERE productID=%s"
            bindData = (_sterren, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['leverbaar']):
            _leverbaar = _json['leverbaar']
            sqlQuery = "UPDATE producten SET leverbaar=%s WHERE productID=%s"
            bindData = (_leverbaar, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(_json['afbeelding_url']):
            _afbeelding_url = _json['afbeelding_url']
            sqlQuery = "UPDATE producten SET afbeelding_url=%s WHERE productID=%s"
            bindData = (_afbeelding_url, _ID)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
        if(not _json['naam'] and not _json['categorie'] and not _json['prijs'] and not _json['sterren'] and not _json['leverbaar'] and not _json['afbeelding_url']):
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