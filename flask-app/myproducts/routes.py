from myproducts import app
from flask import render_template, request
from myproducts.models import Item


@app.route('/products')
def product_page():
    items = Item.query.all()
    return render_template('products.html', items=items)


@app.route('/qtr1')
def productsByQuarter1():
    items = Item.query.filter_by(qtr=1)
    return {'data': [item.to_dict() for item in items]}

@app.route('/qtr2')
def productsByQuarter2():
    items = Item.query.filter_by(qtr=2)
    return {'data': [item.to_dict() for item in items]}

@app.route('/qtr3')
def productsByQuarter3():
    items = Item.query.filter_by(qtr=3)
    return {'data': [item.to_dict() for item in items]}

@app.route('/qtr4')
def productsByQuarter4():
    items = Item.query.filter_by(qtr=4)
    return {'data': [item.to_dict() for item in items]}


