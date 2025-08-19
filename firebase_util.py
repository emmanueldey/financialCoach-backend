
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

firebase_config = os.environ.get("FIREBASE_CONFIG")
firebase_dict = json.loads(firebase_config)

# ✅ Fix escaped newline issue in private_key
if "private_key" in firebase_dict:
    firebase_dict["private_key"] = firebase_dict["private_key"].replace("\\n", "\n")

cred = credentials.Certificate(firebase_dict)

# Firestore client
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
