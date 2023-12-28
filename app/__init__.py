from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import UPLOAD_FILES

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_Key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['UPLOAD_FILES'] = UPLOAD_FILES

db = SQLAlchemy()
db.init_app(app=app)

migrate = Migrate()
migrate.init_app(app=app, db=db)

from app.routes import app_bp
app.register_blueprint(app_bp)


