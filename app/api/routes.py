from flask import (
    Blueprint, render_template, request
)
import requests


api_bp = Blueprint('w_api', __name__, url_prefix='/w_api')


@api_bp.route('/search', methods=['GET', 'POST'])
def search_city():
    if request.method == 'POST':
        city = request.form.get('city').capitalize()

    api_key = '2a9882821859c518cce5e1e1be745c5d'
    api_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    api_call = requests.get(api_url)
    data = api_call.json()

    name_city = data['city']['name']
    date = data['list'][0]['dt_txt']
    temperature = data['list'][0]['main']['temp']
    speed = data['list'][0]['wind']['speed']

    return render_template(
        'city.html', city=city, date=date,
        temperature=temperature, speed=speed,
        name_city=name_city
    )
