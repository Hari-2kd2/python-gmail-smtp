import os

from dotenv import load_dotenv


def load_env_variables():
    """
    Loads environment variables and returns email configuration settings.

    :return: A tuple containing IMAP hostname, SMTP hostname, SMTP port,
             username, password, forward_to email address, and a list of keywords.
    :raises ValueError: If username or password is not provided in environment variables.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Define default values
    imap_hostname = "imap.gmail.com"
    smtp_hostname = "smtp.gmail.com"
    smtp_port = 587

    # Retrieve configuration from environment variables
    username = os.getenv("GMAIL_ADDRESS")
    password = os.getenv("GMAIL_PASSWORD")
    forward_to = os.getenv("FORWARD_TO")
    keywords = os.getenv("KEYWORDS", "").split(",")

    # Validate required environment variables
    if not username or not password:
        raise ValueError("Username or password not provided in environment variables.")

    # Return the configuration settings as a tuple
    return (
        imap_hostname,
        smtp_hostname,
        smtp_port,
        username,
        password,
        forward_to,
        keywords,
    )
