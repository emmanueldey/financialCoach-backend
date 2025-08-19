
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json

# ✅ Read from environment variable
firebase_config = os.environ.get("FIREBASE_CONFIG")

# ✅ Convert JSON string to dict
firebase_dict = json.loads(firebase_config)

# ✅ Initialize Firebase using the in-memory dictionary
cred = credentials.Certificate(firebase_dict)
firebase_admin.initialize_app(cred)

# ✅ Firestore client
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
