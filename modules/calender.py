from datetime import datetime, timedelta
import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Define the required scopes
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]

def get_calendar_service():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("calendar", "v3", credentials=creds)

def schedule_meeting():
    service = get_calendar_service()
    
    event = {
        "summary": "Team Meeting",
        "location": "Google Meet",
        "description": "Discussion on project progress.",
        "start": {
            "dateTime": (datetime.utcnow() + timedelta(days=1, hours=2)).isoformat() + "Z",
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": (datetime.utcnow() + timedelta(days=1, hours=3)).isoformat() + "Z",
            "timeZone": "Asia/Kolkata",
        },
        "recurrence": ["RRULE:FREQ=DAILY;COUNT=1"],
        "attendees": [
            {"email": "example@gmail.com"},
        ],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 30},
                {"method": "popup", "minutes": 10},
            ],
        },
    }

    event = service.events().insert(calendarId="primary", body=event).execute()
    print(f"Meeting Scheduled: {event.get('htmlLink')}")

if __name__ == "__main__":
    schedule_meeting()
