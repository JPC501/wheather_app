from flask import (
    Blueprint, render_template, request,
    flash, redirect, url_for
)
import requests
import datetime


api_bp = Blueprint('w_api', __name__, url_prefix='/w_api')


@api_bp.route('/search', methods=['GET', 'POST'])
def search_city():
    error = None
    if request.method == 'POST':
        city = request.form.get('city').capitalize()

    api_key = '2a9882821859c518cce5e1e1be745c5d'
    api_url_parts = [
        'http://api.openweathermap.org/data/2.5/forecast?',
        f'q={city}',
        f'&appid={api_key}'
    ]
    api_url = ''.join(api_url_parts)

    try:
        api_call = requests.get(api_url)
        api_call.raise_for_status()
        data = api_call.json()
    except requests.HTTPError:
        if api_call.status_code == 404:
            error = 'City not found'
            flash(error)
            return redirect(url_for('index'))

    name_city = data['city']['name']
    date = data['list'][0]['dt']
    read_date = datetime.datetime.fromtimestamp(date)
    date_to_show = read_date.date().strftime('%Y-%m-%d')
    time = read_date.time().strftime('%H:%M')
    wheather = data['list'][0]['weather'][0]['description']
    temperature = data['list'][0]['main']['temp']
    temperature = temperature - 273.15
    temperature = round(temperature, 2)
    speed = data['list'][0]['wind']['speed']

    return render_template(
        'city.html', city=city, temperature=temperature,
        speed=speed, name_city=name_city, time=time,
        date_to_show=date_to_show, wheather=wheather
    )
