from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def get_calendar_service():
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)
    return service

def list_events():
    service = get_calendar_service()
    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])
    return events

def speak_events(events):
    for event in events:
        print(event['summary'], event['start']['dateTime'])
