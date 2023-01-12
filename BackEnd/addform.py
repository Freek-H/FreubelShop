from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

from config import *

def addForm():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        _json = request.json
        _naam = _json['naam']
        _ordernummer = _json['ordernummer']
        _email= _json['email']
        _telefoonnummer = _json['telefoonnummer']
        _vraag = _json['vraag']

        if  _naam and _ordernummer and _email and _telefoonnummer and _vraag and request.method == 'POST':
            sqlQuery = "INSERT INTO contactformulier(naam, ordernummer, email, telefoonnummer, vraag) VALUES(%s, %s, %s, %s, %s)"
            bindData = (_naam, _ordernummer, _email, _telefoonnummer, _vraag)
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