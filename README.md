
# WeatherCLI: Your Local Weather at a Command

WeatherCLI is a command-line weather application that fetches and displays weather forecasts from various sources, starting with AccuWeather. It's designed for those who prefer working within a terminal environment or require a straightforward, scriptable interface to obtain weather forecasts.

## Features

- Fetch weather forecasts from AccuWeather.
- Display weather data for a specified city.
- Support for different forecast durations: 1 day, 5 days, 10 days, and 15 days.
- Customizable output formats: default, verbose, and short.
- Extendable architecture to support more weather data providers in the future.

## Installation

Before you can run WeatherCLI, you'll need Python 3.7 or later. Clone this repository to your local machine to get started:

```bash
git clone https://github.com/yourgithub/weathercli.git
cd weathercli
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run WeatherCLI with Python. Here are some example commands:

```bash
# Get a 5-day weather forecast for Cork in the default format
python main.py forecast -c Cork -dur 5day

# Get a verbose weather forecast for Tokyo
python main.py forecast -c Tokyo -o verbose

# Get a short weather forecast for New York with a 15-day duration
python main.py forecast -c "New York" -dur 15day -o short
```

## Configuration

WeatherCLI uses API keys for fetching data from weather providers. Before using WeatherCLI, you'll need to obtain an API key from [AccuWeather](https://developer.accuweather.com/) and set it as an environment variable:

```bash
export ACCUWEATHER_API_KEY='your_api_key_here'
```

## Extending WeatherCLI

WeatherCLI is designed to be extendable:

- **Adding New Data Providers**: Implement the `WeatherApiClient` interface in a new class.
- **Custom Output Formats**: Extend the `OutputFormatter` class to create new output formats.

See the developer documentation for more details.
