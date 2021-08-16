from flask import Flask
from .routes.routes import api_bp #import the 'api_bp' variable to register
from .config.config import config #import the 'config' variable to register
import os 

app = Flask(__name__)
app.register_blueprint(api_bp)
app.config.from_object(config['development'])

def init_app(): #Create a function to run the flask app.
    app.run(host="0.0.0.0",port=os.environ.get("PORT",7575))