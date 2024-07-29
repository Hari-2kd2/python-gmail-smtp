import json
import os
from email import message_from_bytes
from login import login_to_imap
from logout import logout_from_imap
from email_forwarder import forward_email
from env_setup import load_env_variables

# Load environment variables
imap_hostname, smtp_hostname, smtp_port, username, password, forward_to, keywords = load_env_variables()

PROCESSED_EMAILS_FILE = "processed_emails.json"


def load_processed_emails() -> list:
    """
    Loads the list of processed email IDs from a JSON file.

    :return: A list of processed email IDs.
    """
    if os.path.exists(PROCESSED_EMAILS_FILE):
        with open(PROCESSED_EMAILS_FILE, "r") as f:
            return json.load(f)
    return []


def save_processed_emails(processed_emails: list) -> None:
    """
    Saves the list of processed email IDs to a JSON file.

    :param processed_emails: A list of processed email IDs.
    """
    with open(PROCESSED_EMAILS_FILE, "w") as f:
        json.dump(processed_emails, f)


def check_mail():
    """
    Checks for unread emails, processes them if they contain specified keywords,
    and forwards them if necessary. Marks processed emails as read.

    :return: A tuple containing the subject and body of the processed email, or (None, None) if no email is processed.
    """
    processed_emails = load_processed_emails()
    client = login_to_imap()

    try:
        # Select the inbox
        client.select_folder("INBOX")

        # Search for unread emails
        messages = client.search(["UNSEEN"])
        print(f"Number of unread messages: {len(messages)}")

        if messages:
            for msg_id in messages:
                if msg_id in processed_emails:
                    print(f"Message ID {msg_id} already processed. Skipping.")
                    continue

                # Fetch and process the email
                message_data = client.fetch([msg_id], ["RFC822"])
                raw_message = message_data[msg_id][b"RFC822"]
                print(f"Raw Message Data for ID {msg_id}:")
                print(raw_message.decode("utf-8", errors="replace"))

                msg = message_from_bytes(raw_message)
                subject = msg.get("subject", "No Subject")
                body = extract_email_body(msg)

                if any(keyword in body.lower() for keyword in keywords):
                    print(f"Keyword found in message ID {msg_id}. Forwarding...")
                    forward_email(subject, body)
                    processed_emails.append(msg_id)
                    save_processed_emails(processed_emails)
                    client.add_flags([msg_id], ["\\Seen"])
                    return subject, body  # Return subject and body for further processing

                print(f"No keywords found in message ID {msg_id}. Skipping forwarding.")

        else:
            print("No unread messages found.")
            return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

    finally:
        logout_from_imap(client)


def extract_email_body(msg) -> str:
    """
    Extracts the body of an email message, including both plain text and HTML parts.

    :param msg: The email message object.
    :return: The extracted email body as a string.
    """
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            if content_type == "text/plain":
                body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                break
            elif content_type == "text/html":
                html_body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                body += f"\n[HTML Content]\n{html_body}"
    else:
        body = msg.get_payload(decode=True).decode("utf-8", errors="replace")

    return body
