import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from utils import logs

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


@logs(message="Signing in...")
def signin(auth_token_path, client_secret_path) -> Credentials:
    creds = None

    if os.path.exists(auth_token_path):
        creds = Credentials.from_authorized_user_file(auth_token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(auth_token_path, "w") as token:
            token.write(creds.to_json())
    return creds


@logs("Building GooglePeopleService")
def build_google_service(creds):
    return build("people", "v1", credentials=creds)


request_parameters = {
    'resourceName': 'people/me',
    'pageSize': 10,
    'personFields': 'names,birthdays,phoneNumbers',
}


def fetch_from_page(google, page_token=None) -> dict:
    if page_token:
        request_parameters['pageToken'] = page_token

    return google.people().connections().list(**request_parameters).execute()
