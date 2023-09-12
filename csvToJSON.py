import json
import requests
import csv
import time
import random
from time import sleep
from datetime import datetime

def process_and_send_row(row, endpoint, min_delay, max_delay):
    try:
        # Insert current timestamp in the 'Timestamp' field
        row['Timestamp'] = datetime.now().isoformat()
        
        # Convert the row to JSON
        json_payload = json.dumps(row)
        print(f"Sending payload: {json_payload}")  

        # Send the JSON payload using HTTP POST
        response = requests.post(endpoint, json=row, timeout=0.001)

        if response.status_code == 200:
            print(f"Successfully sent row.")
        else:
            print(f"Failed to send row. Response: {response.text}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while sending the request: {e}")

    sleep_duration = random.uniform(min_delay, max_delay)
    sleep(sleep_duration)

def read_large_csv_and_send(file_path, endpoint, min_delay=0.010, max_delay=0.500):
    print("Starting to send data...")  
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as f:
            csv_reader = csv.DictReader(f)
            print("Headers: ", csv_reader.fieldnames)
            for row in csv_reader:
                selected_fields = {k: row[k] for k in row.keys() if k in ['Timestamp', 'TypeOfMobile', 'MMSI', 'Latitude', 'Longitude']}
                start_time = time.time()
                process_and_send_row(selected_fields, endpoint, min_delay, max_delay)
                end_time = time.time()
                print(f"Time taken for request: {end_time - start_time}")

    except KeyboardInterrupt:
        print("Interrupted! Stopping script.")
        return

if __name__ == '__main__':
    FILE_PATH = 'aisdata_for_10min.csv'
    ENDPOINT = 'http://localhost:5000'
    
    read_large_csv_and_send(FILE_PATH, ENDPOINT)