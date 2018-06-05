from config import Config
from app.forms import choices


class one_year:
    
    def ask_to_buy_land(water_in_storage, land_price, acres):
        'Ask user how many acres they will buy'
        acres = acres
        ACFT_in_storage = water_in_storage
        cost_per_acres = land_price
        while acres * cost_per_acre > ACFT_in_storage:
            print ('Hey Water Master, we have but ', ACFT_in_storage,' ACFT of water!')
            acres = cs50.get_int('How many acres will you buy? ')
        return acres

