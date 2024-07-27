from email_checker import check_mail
from check_current_date_mail import check_current_date_mail
from gmeet_scheduler import create_google_meet_event


def process_emails():
    try:
        subject, body = check_mail()
        if subject and body:
            # create_google_meet_event(subject, body)
            print(f"Processed email with subject: {subject}")
        else:
            print("No emails processed.")
    except Exception as e:
        print(f"An error occurred during processing emails: {e}")


def process_today_emails():
    try:
        subject, body = check_current_date_mail()
        if subject and body:
            create_google_meet_event(subject, body)
            print(f"Processed today's email with subject: {subject}")
        else:
            print("No emails processed.")
    except Exception as e:
        print(f"An error occurred during processing today's emails: {e}")


# # Example usage if needed
# if __name__ == "__main__":
#     process_emails()
#     process_today_emails()
