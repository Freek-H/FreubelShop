from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

import producten
import addform
import register
import login
import profiel
import update
import delete
import addproduct
import updateproduct
import deleteproduct

from config import *


#app = Flask(__name__)
#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
#CORS(app)

#mysql = MySQL()
#app.config['MYSQL_DATABASE_USER'] = 'acknowledge'
#app.config['MYSQL_DATABASE_PASSWORD'] = 'abcd1234ABCD!@#$'
#app.config['MYSQL_DATABASE_DB'] = 'ackgrannyinc'
#app.config['MYSQL_DATABASE_HOST'] = 'ack2211dbdemofelix.mysql.database.azure.com'
#mysql.init_app(app)

if __name__ == "__main__":
    app.run()
    
@app.route('/register', methods=['POST'])
def user_register():
    return register.register()

@app.route('/addform', methods=['POST'])
def send_form():
    return addform.addForm()

@app.route('/login', methods=['POST'])
def user_login():
    return login.login()

### Probleem met GET --> Voor iedereen toegankelijk met URL --> Enkel alle profielen oproepen via JSON door bv Admin zoals gebeurt door individuele gebruikers in eigen profiel ### 
@app.route('/profile')
def user_profile():
    return profiel.profile()

@app.route('/update', methods=['PUT'])
def user_update():
    return update.update()
        
@app.route('/delete/<int:user_ID>', methods=['DELETE'])
def user_delete(user_ID):
    return delete.delete(user_ID)

@app.route('/addproduct', methods=['POST'])
def product_add():
    return addproduct.add()

@app.route('/updateproduct', methods=['PUT'])
def product_update():
    return updateproduct.product_update()

@app.route('/deleteproduct/<int:productID>', methods=['DELETE'])
def product_delete(productID):
    return deleteproduct.product_delete(productID)

@app.route('/producten')
def vinddeproducten():
    #return producten.vindalleproducten() 
    return producten.vindNonStandardGegevens()

### ERROR CODES ### 

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'STATUS': 404,
        'MESSAGE': 'Niet gevonden: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

@app.errorhandler(405)
def showMessage(error=None):
    message = {
        'STATUS': 405,
        'MESSAGE': 'Methode kan niet handmatig worden opgeroepen: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 405
    return response

@app.errorhandler(500)
def showMessage(error=None):
    message = {
        'STATUS': 500,
        'MESSAGE': 'Er is een probleem opgetreden op de server of website: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 500
    return response