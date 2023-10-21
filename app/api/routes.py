"""
Weather API Consumption Module
------------------------------

This module contains the routes and consumption of the API 
from https://openweathermap.org/api.

It includes requests with the API key, error handling, 
and template rendering.

Routes:
    - /search_city
    """
from flask import (
    Blueprint, render_template, request,
    flash, redirect, url_for
)
import requests
import datetime
from os import getenv

# Create a Blueprint for routes related to the weather API.
api_bp = Blueprint('w_api', __name__, url_prefix='/w_api')


@api_bp.route('/search', methods=['GET', 'POST'])
def search_city():
    """
    Endpoint to search for the weather forecast of a city.

    If the method is POST, the city is retrieved from the form,
    a request is made to the OpenWeather API to fetch the forecast,
    and the result is rendered in a template.

    Returns:
        - Redirection to the index if there's an error.
        - Renders the city.html template with the weather forecast details.
    """
    error = None
    if request.method == 'POST':
        city = request.form.get('city').capitalize()

    # Construct the API URL with the provided city and API key
    api_key = getenv('API_KEY')
    api_url_parts = [
        'http://api.openweathermap.org/data/2.5/forecast?',
        f'q={city}',
        f'&appid={api_key}'
    ]
    api_url = ''.join(api_url_parts)

    try:
        # Attempt to make a request to the API and get the JSON response.
        api_call = requests.get(api_url)
        api_call.raise_for_status()
        data = api_call.json()
    except requests.HTTPError:
        # Error handling for when the city is not found or other HTTP errors.
        if api_call.status_code == 404:
            error = 'City not found'
            flash(error)
            return redirect(url_for('index'))
        # Additional error handling can be added here for
        # other types of HTTP errors.

    # Extract relevant forecast information.
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

    # Render the template with the extracted information.
    return render_template(
        'city.html', city=city, temperature=temperature,
        speed=speed, name_city=name_city, time=time,
        date_to_show=date_to_show, wheather=wheather
    )
