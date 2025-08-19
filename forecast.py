
import pandas as pd
from datetime import timedelta

def forecast_cashflow(csv_path):
    df = pd.read_csv(csv_path, parse_dates=['date'])
    df['net_cashflow'] = df['income'] - df['expense']
    df = df.sort_values('date')

    avg_flow = df['net_cashflow'].rolling(window=7).mean().iloc[-1]
    last_date = df['date'].max()
    future_dates = [last_date + timedelta(days=i) for i in range(1, 31)]
    forecast = pd.DataFrame({
        'date': future_dates,
        'predicted_net_cashflow': [round(avg_flow, 2)] * 30
    })

    return forecast
