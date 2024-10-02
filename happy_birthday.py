import os.path

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/contacts.readonly']


def get_credentials(auth_token_path, client_secret_path):
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


def get_people_service(creds):
    return build("people", "v1", credentials=creds)


def get_contacts(service):
    results = (
        service.people()
        .connections()
        .list(
            resourceName="people/me",
            pageSize=10,
            personFields="names,emailAddresses",
        )
        .execute()
    )
    return results.get("connections", [])


if __name__ == "__main__":
    try:
        credentials = get_credentials("token.json", "client-secret.json")
        people_service = get_people_service(credentials)
        contacts = get_contacts(people_service)
        for contact in contacts:
            names = contact.get("names", [])
            if names:
                name = names[0].get("displayName")
                print(name)
    except HttpError as error:
        print(error)

