from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

DB_USERNAME = 'root'
DB_PASSWORD = ''
DB_PORT = 3306

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = F'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@localhost:{DB_PORT}/constancetan7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

import routes