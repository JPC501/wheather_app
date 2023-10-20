# MeteoFlask: Simple Weather Lookup by City

_A user-friendly interface to instantly fetch key weather details such as sky conditions, wind speed, and whether it's sunny or cloudy based on a city input._

## Project Description

MeteoFlask is a web application designed to provide a straightforward and user-friendly interface for users to swiftly understand the current weather conditions based on a city's name. The information is sourced in real-time from an external weather API.

## Key Features

- **City Search:** Enter the name of any city to receive its current forecast.
- **Essential Weather Data:** View details like sky conditions, wind speed, and whether the day is sunny or overcast.

## How It Works

The application utilizes Flask, a Python microframework, to manage web requests and responses. When a city name is entered into the search field:

1. The application makes a call to the weather API using the provided city name.
2. It processes the API's JSON response to extract key weather details.
3. Displays the processed information on a result page for the user to view.

## Installation and Usage

If you'd like to run MeteoFlask on your local environment:

1. Clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Create an environment using `python3 -m venv env`
4. Activate the enviroment using `source venv/bin/activate` mac/linux
   `venv\Scripts\activate` for windows
5. Run `python run.py` to start the local server.
6. Navigate to `http://127.0.0.1:5000` in your browser to view the application.

## License

This project is open-source and is available under the [MIT License](LICENSE). Feel free to use, modify, and distribute as you see fit.
