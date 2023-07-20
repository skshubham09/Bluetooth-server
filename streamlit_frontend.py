# streamlit_frontend.py
import streamlit as st
import requests
import pandas as pd
from datetime import datetime

def receive_data(device_id, device_name, health_data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
    data = {
        'device_id': device_id,
        'device_name': device_name,
        'health_data': health_data,
        'timestamp': timestamp,  # Include the formatted timestamp
    }
    response = requests.post('http://localhost:8000/bluetooth_data_app/receive_bluetooth_data/', json=data)
    if response.status_code == 200:
        st.success("Bluetooth data received successfully.")
    else:
        st.error("Error occurred while receiving Bluetooth data.")

def fetch_data():
    response = requests.get('http://localhost:8000/bluetooth_data_app/get_bluetooth_data/')
    if response.status_code == 200:
        data = response.json()
        timestamped_data = data['timestamped_data']
        devices = data['devices']

        # Combine the two tables into one based on the 'device_id' column
        combined_data = []
        for entry in timestamped_data:
            device_id = entry['device']
            if device_name := next(
                (
                    device['device_name']
                    for device in devices
                    if device['device_id'] == device_id
                ),
                None,
            ):
                entry['device_name'] = device_name
            combined_data.append(entry)

        st.subheader('Combined Bluetooth Data and Device Details')
        df = pd.DataFrame(combined_data)
        st.dataframe(df)
    else:
        st.error("Error occurred while fetching data.")

def main():
    st.title('Bluetooth Data Visualization')

    device_id = st.text_input("Enter Device ID:")
    device_name = st.text_input("Enter Device Name:")
    health_data = st.text_input("Enter Health Data:")

    if st.button("Receive Data"):
        receive_data(device_id, device_name, health_data)

    fetch_data()

if __name__ == '__main__':
    main()
