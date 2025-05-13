from datetime import datetime
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Read credentials from environment variables
APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SHEETY_USERNAME = os.getenv('SHEETY_USERNAME')
SHEETY_PASSWORD = os.getenv('SHEETY_PASSWORD')

# Optional user info from environment
GENDER = os.getenv('GENDER')
WEIGHT_KG = float(os.getenv('WEIGHT_KG'))
HEIGHT_CM = float(os.getenv('HEIGHT_CM'))
AGE = int(os.getenv('AGE'))

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/58cfdd465ff6282136cbd49fcc696aa1/copyOfMyWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(SHEETY_USERNAME, SHEETY_PASSWORD)
    )
    print(sheet_response.text)
