from flask import Flask
from modules import shopping_cart

app = Flask(__name__)

app.register_blueprint(shopping_cart.scroute)