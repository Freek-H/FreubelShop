from flask import Flask, session, abort
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
CORS(app)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'acknowledge'
app.config['MYSQL_DATABASE_PASSWORD'] = 'abcd1234ABCD!@#$'
app.config['MYSQL_DATABASE_DB'] = 'ackgrannyinc'
app.config['MYSQL_DATABASE_HOST'] = 'ack2211dbdemofelix.mysql.database.azure.com'
mysql.init_app(app)