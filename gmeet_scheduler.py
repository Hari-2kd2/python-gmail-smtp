from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from random_string import generate_random_string

SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_google_meet_event(subject: str, body: str) -> None:
    """Creates a Google Calendar event with Google Meet integration."""
    flow = InstalledAppFlow.from_client_secrets_file(
        'credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)

    service = build('calendar', 'v3', credentials=creds)

    start_time = datetime.now(timezone.utc) + timedelta(minutes=10)
    end_time = start_time + timedelta(hours=1)

    event = {
        'summary': subject,
        'description': body,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'UTC',
        },
        'conferenceData': {
            'createRequest': {
                'requestId': generate_random_string(),  # Unique request ID
                'conferenceSolutionKey': {'type': 'hangoutsMeet'},
            }
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    try:
        event_result = service.events().insert(
            calendarId='primary',
            body=event,
            conferenceDataVersion=1
        ).execute()

        event_link = event_result.get('htmlLink')
        event_id = event_result.get('id')

        print(f"Google Meet event created: {event_link}")
        print(f"Event ID: {event_id}")
        print(f"Event Details: {event_result}")

    except HttpError as error:
        print(f'An error occurred: {error}')
