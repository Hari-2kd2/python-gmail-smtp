from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
import os.path
import pickle
from datetime import datetime, timedelta

# Define the scope
SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_credentials():
    """Get valid credentials from storage or prompt user to login."""
    creds = None
    # Check if token.pickle file exists
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # If no valid credentials, prompt user to login
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return creds


def create_google_meet_event(subject, body):
    """Create a Google Calendar event with Google Meet integration."""
    creds = get_credentials()
    service = build("calendar", "v3", credentials=creds)

    # Define event details with timezone-aware datetime
    start_time = datetime.utcnow() + timedelta(minutes=10)
    end_time = start_time + timedelta(hours=1)

    event = {
        "summary": subject,
        "description": body,
        "start": {
            "dateTime": start_time.isoformat() + "Z",
            "timeZone": "UTC",
        },
        "end": {
            "dateTime": end_time.isoformat() + "Z",
            "timeZone": "UTC",
        },
        "conferenceData": {
            "createRequest": {
                "requestId": "random-string",  # Unique request ID
                "conferenceSolutionKey": {"type": "hangoutsMeet"},
            }
        },
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
            .insert(calendarId="primary", body=event, conferenceDataVersion=1)
            .execute()
        )
        print(f"Google Meet event created: {event_result.get('htmlLink')}")
        print(f"Event ID: {event_result.get('id')}")
    except HttpError as error:
        print(f"An error occurred: {error}")
