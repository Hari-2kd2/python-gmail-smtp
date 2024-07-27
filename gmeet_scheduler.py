from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
from random_string import generate_random_string

# Load Google API credentials
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "credentials.json"

def create_google_meet_event(subject, body):
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    # Define event details with timezone-aware datetime
    event = {
        "summary": subject,
        "description": body,
        "start": {
            "dateTime": (datetime.now(timezone.utc) + timedelta(minutes=10)).isoformat(),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat(),
            "timeZone": "UTC",
        },
        "conferenceData": {
            "createRequest": {
                # Uncomment if using a valid conference solution key
                # "conferenceSolutionKey": {"type": "hangoutsMeet"},
                "requestId": generate_random_string(),  # Replace with a unique string
            }
        },
        # Uncomment and modify the following section if adding attendees
        # 'attendees': [
        #     {'email': 'attendee1@example.com'},
        #     {'email': 'attendee2@example.com'}
        # ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    try:
        # Insert the event with conference data
        event_result = (
            service.events()
            .insert(
                calendarId="primary",
                body=event,
                conferenceDataVersion=1  # Include conference data
            )
            .execute()
        )

        event_link = event_result.get("htmlLink")
        event_id = event_result.get("id")

        print(f"Google Meet event created: {event_link}")
        print(f"Event ID: {event_id}")
        print(f"Event Details: {event_result}")

    except Exception as e:
        print(f"An error occurred while creating the event: {e}")