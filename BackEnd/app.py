from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

import producten
import register
import login
import profiel
import update
import delete
import addproduct

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'webshopusers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

if __name__ == "__main__":
    app.run()
    
@app.route('/register', methods=['POST'])
def user_register():
    return register.register()

@app.route('/login', methods=['POST'])
def user_login():
    return login.login()
        
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

@app.route('/producten')
def vinddeproducten():
    #return producten.vindalleproducten() 
    return producten.vindNonStandardGegevens()

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'STATUS': 404,
        'MESSAGE': 'Niet gevonden: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response
