import os
from dotenv import load_dotenv


def load_env_variables():
    load_dotenv()
    imap_hostname = "imap.gmail.com"
    smtp_hostname = "smtp.gmail.com"
    smtp_port = 587
    username = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_PASSWORD")
    forward_to =  os.getenv("FORWARD_TO")
    keywords = os.getenv("KEYWORDS", "").split(",")

    if not username or not password:
        raise ValueError("Username or password not provided in environment variables.")

    return (
        imap_hostname,
        smtp_hostname,
        smtp_port,
        username,
        password,
        forward_to,
        keywords,
    )
