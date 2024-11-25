from models.contact import Contact
from services.google_service import send_request
from utils import logs


def has_details_stored(contact) -> bool:
    details = ["names", "birthdays", "phoneNumbers"]
    return all(detail in contact and contact[detail] for detail in details)


@logs(message="Fetching contacts...")
def get_contacts(google) -> list[Contact]:
    contacts, next_page_token = list(), None
    while True:
        results = send_request(google, next_page_token)
        connections = results.get("connections", [])
        contacts.extend(connections)
        next_page_token = results.get("nextPageToken", None)
        if not next_page_token:
            break
    return [Contact.create(c) for c in contacts if has_details_stored(c)]
