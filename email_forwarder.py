from email.message import EmailMessage
import smtplib
from env_setup import load_env_variables

# Load environment variables
imap_hostname, smtp_hostname, smtp_port, username, password, forward_to, keywords = load_env_variables()


def forward_email(subject: str, body: str) -> None:
    """
    Forwards an email with the given subject and body to the specified recipient.

    :param subject: The subject of the email.
    :param body: The body content of the email.
    """
    message = EmailMessage()
    message.set_content(body)
    message["Subject"] = subject
    message["From"] = username
    message["To"] = forward_to

    try:
        print("Connecting to SMTP server...")
        with smtplib.SMTP(smtp_hostname, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)
            server.send_message(message)
            print(f"Email forwarded to {forward_to}")
    except smtplib.SMTPException as e:
        print(f"SMTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred while forwarding email: {e}")
