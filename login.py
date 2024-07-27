from imapclient import IMAPClient
import os
from dotenv import load_dotenv


def login_to_imap():
    load_dotenv()

    imap_hostname = "imap.gmail.com"
    username = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_PASSWORD")

    if not username or not password:
        raise ValueError("Username or password not provided in environment variables.")

    print("Connecting to IMAP server...")
    client = IMAPClient(imap_hostname, ssl=True)
    print(f"Logging in with username: {username}")
    client.login(username, password)
    print("Login successful!")

    return client
