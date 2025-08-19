
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("../firebase/firebase_config.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def save_user_data(user_id, data):
    ref = db.collection("users").document(user_id).collection("cashflow")
    for row in data:
        ref.add(row)

def save_forecast(user_id, forecast, tips):
    ref = db.collection("users").document(user_id)
    ref.set({
        "forecast": forecast,
        "recommendations": tips
    })
