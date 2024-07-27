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


def load_processed_emails():
    if os.path.exists(PROCESSED_EMAILS_FILE):
        with open(PROCESSED_EMAILS_FILE, "r") as f:
            return json.load(f)
    return []


def save_processed_emails(processed_emails):
    with open(PROCESSED_EMAILS_FILE, "w") as f:
        json.dump(processed_emails, f)


def check_current_date_mail():
    processed_emails = load_processed_emails()
    client = login_to_imap()
    try:
        # Select the inbox
        client.select_folder("INBOX")

        # Get today's date
        today = datetime.now().date()

        # Format the date for IMAP search criteria
        date_str = today.strftime("%d-%b-%Y").upper()

        # Search for unread emails
        search_criteria = ["UNSEEN"]
        print(f"Searching with criteria: {search_criteria}")

        try:
            messages = client.search(search_criteria)
            print(f"Number of unread messages: {len(messages)}")
        except Exception as search_e:
            print(f"Search error: {search_e}")
            return None, None

        # Fetch and process unread emails
        if messages:
            for msg_id in messages:
                if msg_id in processed_emails:
                    print(f"Message ID {msg_id} already processed. Skipping.")
                    continue

                # Fetch the full message data
                message_data = client.fetch([msg_id], ["RFC822"])

                # Debug: Print raw email data
                raw_message = message_data[msg_id][b"RFC822"]
                print(f"Raw Message Data for ID {msg_id}:")
                # print(raw_message.decode("utf-8", errors="replace"))

                # Parse the email message
                msg = message_from_bytes(raw_message)

                # Extract email details
                subject = msg.get("subject", "No Subject")
                sender = msg.get("from", "No Sender")
                body = ""

                # Get the body of the email
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode(
                                "utf-8", errors="replace"
                            )
                            break
                        elif content_type == "text/html":
                            html_body = part.get_payload(decode=True).decode(
                                "utf-8", errors="replace"
                            )
                            body += f"\n[HTML Content]\n{html_body}"
                else:
                    body = msg.get_payload(decode=True).decode(
                        "utf-8", errors="replace"
                    )

                # Check for any of the keywords in the email body
                if any(keyword in body.lower() for keyword in keywords):
                    print(f"Keyword found in message ID {msg_id}. Forwarding...")
                    forward_email(subject, body)
                    processed_emails.append(msg_id)
                    save_processed_emails(processed_emails)
                    client.add_flags([msg_id], ["\\Seen"])
                    return subject, body  # Return subject and body for further processing
                else:
                    print(f"No keywords found in message ID {msg_id}. Skipping forwarding.")

        else:
            print("No unread messages found.")
            return None, None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
    finally:
        logout_from_imap(client)


# Example usage
check_current_date_mail()
