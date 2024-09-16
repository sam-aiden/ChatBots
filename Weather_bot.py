import requests
import streamlit as st

# OpenWeatherMap API Key
API_KEY = '5ffd9cc595983d3e4a3ad1fb219875db'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Function to fetch weather data
def get_weather(city):
    url = f'{BASE_URL}?q={city}&units=metric&appid={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]['description']
        temperature = main['temp']
        wind_speed = wind['speed']
        humidity = main['humidity']

        return f'Weather in {city.capitalize()}:\nTemperature: {temperature}°C\nWeather: {weather.capitalize()}\nWind Speed: {wind_speed} m/s\nHumidity: {humidity}%'
    else:
        return f'Error: Unable to fetch weather data for {city}. (Status code: {response.status_code})'

# Streamlit App
def weather_chatbot():
    st.title("Weather Chatbot")
    st.write("Type a city name to get weather information, or type 'quit' to exit.")

    city = st.text_input("Enter city name:")

    # Retain the conversation by showing history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if st.button("click") and city:
        if city.lower() == 'quit':
            st.session_state.chat_history.append("Goodbye! Have a great day!")
            city = " "  # Clear input after 'quit'
        else:
            weather_info = get_weather(city)
            st.session_state.chat_history.append(f"You: {city}")
            st.session_state.chat_history.append(f"Chatbot: {weather_info}")

    # Display conversation history
    for i,chat in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.info(chat) # user message(you)
        else:
            st.success(chat) # chatbot's message(bot)

# Run the app
if __name__ == '__main__':
    weather_chatbot()
