import streamlit as st
import requests
import folium

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
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")

# Dropoff longitude and latitude
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")

# Passenger count
passenger_count = st.number_input("Passenger Count", min_value=1, step=1)

## Once we have these, let's call our API in order to retrieve a prediction

url = 'https://taxifare.lewagon.ai/predict'


# Build the parameters dictionary for API
params = {
    "pickup_datetime": f"{date_time} {time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}


@st.cache
def get_prediction(params):
    # Call the API and retrieve the prediction
    response = requests.get(url, params=params)
    data = response.json()
    prediction = data['prediction']
    return prediction

# Call the API and retrieve the prediction (cached if inputs are the same)
prediction = get_prediction(params)

'''
## Finally, we can display the prediction to the user
'''
st.success(f'The predicted taxi fare is {prediction} USD')

# Create a base map centered on New York City
map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# Add a marker for pickup location
pickup_marker = folium.Marker(location=[pickup_latitude, pickup_longitude],
                              popup='Pickup Location',
                              icon=folium.Icon(color='blue'))
map.add_child(pickup_marker)

# Add a marker for dropoff location
dropoff_marker = folium.Marker(location=[dropoff_latitude, dropoff_longitude],
                               popup='Dropoff Location',
                               icon=folium.Icon(color='red'))
map.add_child(dropoff_marker)

# Display the map using Streamlit
st.write(map._repr_html_(), unsafe_allow_html=True)
