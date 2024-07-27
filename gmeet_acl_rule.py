from google.oauth2 import service_account
from googleapiclient.discovery import build

# Load Google API credentials
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "credentials.json"


def add_acl_rule():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    # Define ACL rule details
    rule = {
        "scope": {
            "type": "user",
            "value": "user@example.com",  # Replace with the email of the user you want to grant access
        },
        "role": "writer",  # 'reader' or 'writer'
    }

    try:
        # Insert ACL rule
        created_rule = service.acl().insert(calendarId="primary", body=rule).execute()
        print(f"ACL rule created with ID: {created_rule['id']}")
    except Exception as e:
        print(f"An error occurred while creating the ACL rule: {e}")


# Example usage
add_acl_rule()
