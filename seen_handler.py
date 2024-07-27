from imapclient import IMAPClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
imap_hostname = "imap.gmail.com"
username = os.getenv("GMAIL_ADDRESS")
password = os.getenv("GMAIL_PASSWORD")

if not username or not password:
    raise ValueError("Username or password not provided in environment variables.")

try:
    print("Connecting to IMAP server...")
    with IMAPClient(imap_hostname, ssl=True) as client:
        print(f"Logging in with username: {username}")
        client.login(username, password)
        print("Login successful!")

        # Select the inbox
        client.select_folder("INBOX")

        # Search for unread emails
        messages = client.search(["UNSEEN"])
        print(f"Number of unread messages: {len(messages)}")

        if messages:
            # Mark all unread messages as read
            client.add_flags(messages, ["\\Seen"])
            print(f"Marked {len(messages)} messages as read.")
        else:
            print("No unread messages found.")

except Exception as e:
    print(f"An error occurred: {e}")
