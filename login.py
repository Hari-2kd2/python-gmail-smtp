from imapclient import IMAPClient
import os
from dotenv import load_dotenv


def login_to_imap():
    """
    Logs into the IMAP server using credentials from environment variables.

    :return: An IMAPClient instance if login is successful.
    :raises ValueError: If environment variables for username or password are not set.
    :raises Exception: For any issues during connection or login.
    """
    load_dotenv()

    imap_hostname = "imap.gmail.com"
    username = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_PASSWORD")

    if not username or not password:
        raise ValueError("Username or password not provided in environment variables.")

    try:
        print("Connecting to IMAP server...")
        imap_client = IMAPClient(imap_hostname, ssl=True)
        print(f"Logging in with username: {username}")
        imap_client.login(username, password)
        print("Login successful!")
        return imap_client
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    login_to_imap()