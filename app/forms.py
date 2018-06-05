from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField 
from wtforms.validators import DataRequired, Required
from config import Config
import random

class choices(FlaskForm):
    acres_to_buy_field = IntegerField('Acres of land to buy', validators=[DataRequired(
        'Enter the number of Acres of land to buy')])
    acres_to_sell_field = IntegerField('Acres of land to sell', validators=[DataRequired(
        'Enter the number of acres of land to sell')])
    ACFT_for_citizens = IntegerField('AC-FT of water to give citizens', validators=[DataRequired(
        'Enter the number of AC-FT of water to give citizens')])
    acres_to_water = IntegerField('Acres of land to farm and water', validators=[DataRequired(
        'Enter the number of acres of land to farm')])
    submit = SubmitField('Make it so')
