import json
import os
from email import message_from_bytes
from datetime import datetime
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
    """
    if os.path.exists(PROCESSED_EMAILS_FILE):
        try:
            with open(PROCESSED_EMAILS_FILE, "r") as f:
                file_content = f.read().strip()
                if not file_content:
                    print("The JSON file is empty.")
                    return []
                try:
                    processed_emails = json.loads(file_content)
                    if isinstance(processed_emails, list):
                        return processed_emails
                    else:
                        print("The JSON file does not contain a valid list.")
                        return []
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from file: {e}")
                    return []
        except IOError as e:
            print(f"Error reading the file: {e}")
            return []
    else:
        print(f"File {PROCESSED_EMAILS_FILE} does not exist.")
        return []


def save_processed_emails(processed_emails: list) -> None:
    """
    Saves the list of processed email IDs to a JSON file.
    """
    with open(PROCESSED_EMAILS_FILE, "w") as f:
        json.dump(processed_emails, f, indent=4)


def extract_email_body(msg) -> str:
    """
    Extracts the body of an email message, including both plain text and HTML parts.
    """
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            payload = part.get_payload(decode=True)
            if payload:
                payload = payload.decode("utf-8", errors="replace")
            else:
                payload = ""
            if content_type == "text/plain":
                body = payload
                break
            elif content_type == "text/html":
                body += f"\n[HTML Content]\n{payload}"
    else:
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode("utf-8", errors="replace")
        else:
            body = ""
    return body


def check_current_date_mail():
    """
    Checks for emails received today, processes them if they contain specified keywords,
    and forwards them if necessary. Marks processed emails as read.
    """
    processed_emails = load_processed_emails()
    client = login_to_imap()

    try:
        client.select_folder("INBOX")

        today = datetime.now().date()
        date_str = today.strftime("%d-%b-%Y").upper()

        search_criteria = ['SINCE', date_str]
        print(f"Searching with criteria: {search_criteria}")

        try:
            messages = client.search(search_criteria)
            print(f"Number of messages: {len(messages)}")
        except Exception as search_e:
            print(f"Search error: {search_e}")
            return None, None

        if messages:
            for msg_id in messages:
                if msg_id in processed_emails:
                    print(f"Message ID {msg_id} already processed. Skipping.")
                    continue

                try:
                    message_data = client.fetch([msg_id], ["RFC822"])
                    raw_message = message_data[msg_id][b"RFC822"]
                    msg = message_from_bytes(raw_message)

                    subject = msg.get("subject", "No Subject")
                    body = extract_email_body(msg)

                    # Check the email for keywords in subject, body, and custom header
                    email_subject = subject.lower()
                    email_body = body.lower()
                    custom_header = msg.get("X-Category", "").lower()  # Example header, adjust as needed

                    if any(keyword in email_subject or keyword in email_body or keyword in custom_header for keyword in
                           keywords):
                        print(f"Keyword found in message ID {msg_id}. Forwarding...")
                        forward_email(subject, body)
                        processed_emails.append(msg_id)
                        save_processed_emails(processed_emails)
                        client.add_flags([msg_id], ["\\Seen"])
                        return subject, body

                    processed_emails.append(msg_id)
                    save_processed_emails(processed_emails)
                    print(f"No keywords found in message ID {msg_id}. Skipping forwarding.")
                except Exception as fetch_e:
                    print(f"Error fetching or processing message ID {msg_id}: {fetch_e}")
                    continue

        print("No new messages found.")
        return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

    finally:
        logout_from_imap(client)
