from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify
import json
from flask import flash, request
from passlib.hash import sha512_crypt

import producten


## Splits in config etc voor overzicht
## clean imports 

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'webshopusers'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

### REST API CRUD ###
### CREATE - POST  ### 

@app.route('/register', methods=['POST'])
def user_register():
    # Niet ideaal om altijd te moeten verbinden, ook als daar geen reden voor is 
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
    except Exception:
            response = jsonify('FAIL')
            return response
    finally:
        cursor.close() 
        conn.close()  
        
### READ - GET ###

@app.route('/profile')
def user():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("SELECT ID, Username, Password, Voornaam, Achternaam, Geslacht, Adres, Telefoon, Email, Geboortedatum, Betaling, Aflever FROM users")
        empRows = cursor.fetchall()
        response = jsonify(empRows)
        response.status_code = 200
        return response
    except Exception:
            response = jsonify('Fout in het ophalen van gegevens!')
            return response
    finally:
        cursor.close() 
        conn.close()  

### Haal mogelijkheid weg om met USER-ID handmatig profiel aan te roepen ### 
@app.route('/profile/<int:user_ID>')
def user_details(user_ID):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("SELECT ID, Username, Password, Voornaam, Achternaam, Geslacht, Adres, Email, Geboortedatum, Betaling, Aflever FROM users WHERE ID =%s", user_ID)
        empRow = cursor.fetchone()
        response = jsonify(empRow)
        response.status_code = 200
        return response
    except Exception:
            response = jsonify('Fout in het ophalen van gegevens!')
            return response
    finally:
        cursor.close() 
        conn.close()
        
### UPDATE - PUT ### 
### Update Functionaliteit ### 

@app.route('/update', methods=['PUT'])
def update_user():
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        _json = request.json
        _ID = _json['ID']
        _Username = _json['Username']
        ##_Password = sha512_crypt.encrypt(_json['Password'])
        _Voornaam = _json['Voornaam']
        _Achternaam = _json['Achternaam']
        _Geslacht = _json['Geslacht']
        _Telefoon = _json['Telefoon']
        _Adres = _json['Adres']
        _Email = _json['Email']
       ## _Geboortedatum = _json['Geboortedatum']
        _Betaling = _json['Betaling']
        _Aflever = _json['Aflever']
        if _Username and _Voornaam and _Achternaam and _Geslacht and _Adres and _Telefoon and _Email and _Betaling and _Aflever and _ID and request.method == 'PUT':
            sqlQuery = "UPDATE users SET Username=%s, Voornaam=%s, Achternaam=%s, Geslacht=%s, Adres=%s, Telefoon=%s, Email=%s, Betaling=%s, Aflever=%s WHERE ID=%s"
            bindData = (_Username, _Voornaam, _Achternaam, _Geslacht, _Adres, _Telefoon, _Email, _Betaling, _Aflever, _ID)
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
        
### DESTROY = DELETE ###
### Block Access, nu kan iedereen er bij ? ###

@app.route('/delete/<int:user_ID>', methods=['DELETE'])
def delete_user(user_ID):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    
    try:
        cursor.execute("DELETE FROM users WHERE ID =%s", user_ID)
        conn.commit()
        response = jsonify('SUCCES')
        response.status_code = 200
        return response 
    except Exception:
            response = jsonify('Verwijderen mislukt!')
            return response
    finally:
        cursor.close() 
        conn.close()  

### LOGIN 
### evt met Salts voor extra beveiliging 

@app.route('/login', methods=['POST'])
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
                ##session['Username'] = account['Username']
                response = jsonify('SUCCES')
                response.status_code = 200
                return response 
        else: 
            response = jsonify('Foutieve gebruikersnaam en / of wachtwoord!')
            return response
    except Exception:
            response = jsonify('ERROR')
            return response
    finally:
        cursor.close() 
        conn.close()  
        
@app.route('/addproduct', methods=['POST'])
def add_product():

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
            response.status_code = 200
            return response 
        else: 
            response = jsonify('FAILXXX')
            return response 
    except Exception as e:
            print(e)
    finally:
        cursor.close() 
        conn.close()  


@app.route('/producten')
def vinddeproducten():
    #return producten.vindalleproducten() 
    return producten.vindNonStandardGegevens()

### LOGOUT - VIA LOCAL STORAGE HTML

##@app.route('/logout')
##def logout():
##   if 'Username' in session:
##        session.pop('Username', None)
##    response = jsonify('Succesvol uitgelogd!')
##    return response
    

### DEFINE ERRORS / RESPONSE CODES ### 
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'STATUS': 404,
        'MESSAGE': 'Niet gevonden: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

### 405

if __name__ == "__main__":
    app.run()
        