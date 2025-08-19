
import smtplib
from email.mime.text import MIMEText

def send_email_alert(to_email, subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = "your@email.com"
    msg["To"] = to_email

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your@email.com", "your-password")
        server.send_message(msg)

# Example usage:
# send_email_alert("student@example.com", "Overspending Alert", "You spent $150 more than expected.")
