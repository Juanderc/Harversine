import os

class development():
    DEBUG = True
    HOST = "localhost"
    PORT = os.environ.get("PORT",7575) #It take a default port, if not take 7575
    SECRET_KEY = 'JAJKFK325%432@'

class production():
    class_name = "production_config"
    FLASK_ENV = 'production'
    HOST = "0.0.0.0"
    PORT = 7575
    SECRET_KEY = 'JAJKFK325%432@'

config = {
    "development":development,
    "production": production,
}

#Here create a development class and production class for the config