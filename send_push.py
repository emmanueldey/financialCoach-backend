
from firebase_admin import messaging

def send_push_alert(token, message_text):
    message = messaging.Message(
        notification=messaging.Notification(
            title="Financial Alert",
            body=message_text,
        ),
        token=token
    )
    response = messaging.send(message)
    return response

# Example usage:
# send_push_alert("device_token", "You're exceeding your budget this week!")
