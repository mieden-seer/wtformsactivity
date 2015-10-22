from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

scroute = Blueprint('shopping_cart', __name__)

products = [
		{
			'name': 'Bag',
			'price': 50
		},

		{
			'name': 'Shoes',
			'price': 100
		},

		{
			'name': 'Socks',
			'price': 25
		}

	]

in_products = []
total_price = 0

@scroute.route('/')
def index():
	return render_template('default/shopping_cart.html', products=products, in_products=in_products, total_price=total_price)

@scroute.route('/', methods=['POST'])
def post_item():
	name = request.form['product_name']
	price = request.form['product_price']

	prod = {
		'name': name,
		'price': price,
		'quantity': 1
	}

	global total_price
	total_price += int(price)

	for p in in_products:

		if(p['name'] == prod['name']):
			p['quantity'] += 1
			break
	else:
		in_products.append(prod)

	return redirect(url_for('.index'))	




