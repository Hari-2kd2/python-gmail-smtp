from email_checker import check_mail
from check_current_date_mail import check_current_date_mail
from gmeet_scheduler import create_google_meet_event

def process_emails():
    """
    Processes emails by calling the check_mail function.

    This function retrieves the subject and body of the email and prints information about
    the processed email. If no email is processed, a message is printed indicating so.
    """
    try:
        subject, body = check_mail()
        if subject and body:
            print(f"Processed email with subject: {subject}")
        else:
            print("No emails processed.")
    except Exception as e:
        print(f"An error occurred during processing emails: {e}")


def process_today_emails():
    """
    Processes emails for the current date by calling the check_current_date_mail function.

    This function retrieves the subject and body of today's email and prints information about
    the processed email. If no email is processed, a message is printed indicating so.
    """
    try:
        subject, body = check_current_date_mail()
        if subject and body:
            print(f"Processed today's email with subject: {subject}")
            create_google_meet_event(subject, body)
        else:
            print("No emails processed for today.")
    except Exception as e:
        print(f"An error occurred during processing today's emails: {e}")

