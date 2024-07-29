from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
from random_string import generate_random_string

# Define Google API scopes and credentials file
SCOPES = ["https://www.googleapis.com/auth/calendar"]
SERVICE_ACCOUNT_FILE = "credentials.json"


def create_google_meet_event(subject: str, body: str) -> None:
    """
    Creates a Google Calendar event with Google Meet integration.

    :param subject: The subject of the event.
    :param body: The description of the event.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    service = build("calendar", "v3", credentials=credentials)

    # Define event details with timezone-aware datetime
    start_time = datetime.now(timezone.utc) + timedelta(minutes=10)
    end_time = start_time + timedelta(hours=1)

    event = {
        "summary": subject,
        "description": body,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "UTC",
        },
        "conferenceData": {
            "createRequest": {
                "requestId": generate_random_string(),  # Unique request ID
                # "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},  # 24 hours before
                {"method": "popup", "minutes": 10},  # 10 minutes before
            ],
        },
    }

    try:
        # Insert the event with conference data
        event_result = service.events().insert(
            calendarId="primary",
            body=event,
            conferenceDataVersion=1  # Include conference data
        ).execute()

        event_link = event_result.get("htmlLink")
        event_id = event_result.get("id")

        print(f"Google Meet event created: {event_link}")
        print(f"Event ID: {event_id}")
        print(f"Event Details: {event_result}")

    except Exception as e:
        print(f"An error occurred while creating the event: {e}")
