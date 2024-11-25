import pywhatkit

from models.date import Date
from services.contact_service import get_contacts
from services.google_service import build_google_service, signin
from services.whatsapp_service import send_whatsapp_message


def main() -> None:
    credentials = signin("../token.json", "../client-secret.json")
    service = build_google_service(credentials)
    contacts = [x for x in get_contacts(service) if x.birthdate == Date.now()]
    for contact in contacts:
        message = f"La Multi Ani, {contact.name}!!!"
        send_whatsapp_message(contact.phone_number, message)


if __name__ == "__main__":
    main()
