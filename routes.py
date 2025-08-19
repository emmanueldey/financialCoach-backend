
from flask import Blueprint, request, jsonify
import pandas as pd
from forecast import forecast_cashflow
from recommend import generate_advice
from firebase_util import save_user_data, save_forecast

routes = Blueprint('routes', __name__)

@routes.route('/analyze', methods=['POST'])
def analyze():
    payload = request.get_json()
    user_id = payload.get("user_id")
    data = payload.get("data")

    df = pd.DataFrame(data)
    df.to_csv("user_cashflow.csv", index=False)

    forecast = forecast_cashflow("user_cashflow.csv")
    tips = generate_advice(df)

    # Save to Firestore
    save_user_data(user_id, data)
    save_forecast(user_id, forecast.to_dict(orient="records"), tips)

    return jsonify({
        "forecast": forecast.to_dict(orient="records"),
        "recommendations": tips
    })
