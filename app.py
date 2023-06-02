import streamlit as st
import requests
import datetime
from PIL import Image

'''
# TaxiFareModel front
'''
st.write('Welcome to my app :sparkles:')

st.markdown('''
NEW YORK TAXI FARE
''')

# Date and time
date_time = st.date_input("Date")
time = st.time_input("Time")

# Pickup longitude and latitude
pickup_longitude = str(st.number_input("Pickup Longitude"))
pickup_latitude = str(st.number_input("Pickup Latitude"))

# Dropoff longitude and latitude
dropoff_longitude = str(st.number_input("Dropoff Longitude"))
dropoff_latitude = str(st.number_input("Dropoff Latitude"))

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, step=1)

## Once we have these, let's call our API in order to retrieve a prediction

url = 'https://taxifare.lewagon.ai/predict'
datetime_var= datetime.datetime.combine(date_time, time)

# Build the parameters dictionary for API
params = {
    "pickup_datetime": f"{date_time} {time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
prediction = response.json()['fare']


'''
## Have a nice TRIP!!!
'''
st.markdown(f'The predicted taxi fare is {prediction} USD')

image = Image.open("/Users/arieleamorim/code/arielimaa/taxifare-website/depositphotos_113580470-stock-photo-cute-dog-in-car.jpg")
st.image(image, caption=' Have a nice trip', use_column_width=True)
