from email.message import EmailMessage
import smtplib
from env_setup import load_env_variables

# Load environment variables
imap_hostname, smtp_hostname, smtp_port, username, password, forward_to, keywords = (
    load_env_variables()
)


def forward_email(subject, body):
    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = username  # Use authenticated email address
    message["To"] = forward_to

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_hostname, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(message)
            print(f"Email forwarded to {forward_to}")
    except Exception as e:
        print(f"An error occurred while forwarding email: {e}")
