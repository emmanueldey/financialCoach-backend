
# Example alert scheduler — combine both email and push
from send_email import send_email_alert
from send_push import send_push_alert

def run_alerts(user_data):
    email = user_data.get("email")
    token = user_data.get("fcm_token")
    overspending = user_data.get("overspending", False)

    if overspending:
        message = "You’ve exceeded your budget this week. Consider reducing expenses."
        if email:
            send_email_alert(email, "Overspending Alert", message)
        if token:
            send_push_alert(token, message)
