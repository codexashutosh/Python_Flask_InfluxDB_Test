from flask import Flask
from data_api import data_api

app = Flask(__name__)
app.register_blueprint(data_api)


if __name__ == '__main__':
    app.run()