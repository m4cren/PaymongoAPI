import eventlet

eventlet.monkey_patch()

from flask import Flask
from .extensions import db, migrate, socketio, jwt



import pymysql
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

pymysql.install_as_MySQLdb()


def create_website():

    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'cacascsac'
    app.config["JWT_SECRET_KEY"] = 'cacasc'
    CORS(app, supports_credentials=True)

  

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://root:%40%23OctObEr102704@192.168.1.33/metafeastdb?charset=utf8"
    )
   

    from .api.auth import auth
    from .api.paymongo import paymongo


 
    app.register_blueprint(auth)
    app.register_blueprint(paymongo)




    db.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app, async_mode="eventlet", cors_allowed_origins="*")

    create_database(app)

    return app


def create_database(app):
    
    with app.app_context():
        db.create_all()
