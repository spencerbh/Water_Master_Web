from flask import render_template, flash, redirect, jsonify
from app import app
from app.forms import choices
import json

@app.route('/')
@app.route('/index', methods=['GET','POST'])
def index():
    year = {'currentyear': '1'}
    
    immigrants = {'new_citizens': '5'}
    population = {'citizens': '100'}

    acres = {'acres_owned': '1000'}
    water_allocation = {'water_alotment': '3'}
    environmentals = {'environmentalists': '200'}
    water_in_storage = {'storage': '2800'}
    land_price = {'cost_per_acre': '24'}

    form = choices()
    if form.validate_on_submit():
        acres = jsonify(form.acres_to_buy_field)
        acres_to_sell = jsonify(form.acres_to_sell_field)
        ACFT_for_feeding = jsonify(form.ACFT_for_citizens)
        acres_to_farm = jsonify(form.acres_to_water)
        flash('Water Master isn\'t done yet, but stay tuned!')
        return redirect('/more')
    return render_template('index.html', title='Home', year=year, immigrants=immigrants, population=population, acres=acres, water_allocation=water_allocation, environmentals=environmentals, water_in_storage=water_in_storage, land_price=land_price, form=form)

@app.route('/more', methods=['GET', 'POST'])
def more():
    return render_template('more.html')
