from models.contact import Contact
from services.google_service import fetch_from_page
from utils import logs


def has_details_stored(contact) -> bool:
    details = ["names", "birthdays", "phoneNumbers"]
    return all(detail in contact and contact[detail] for detail in details)


@logs(message="Fetching contacts...")
def get_contacts(google) -> list[Contact]:
    contacts, next_page_token = list(), None
    while True:
        results = fetch_from_page(google, next_page_token)
        connections = results.get("connections", [])
        contacts.extend(connections)
        next_page_token = results.get("nextPageToken", None)
        if not next_page_token:
            break
    return [Contact.map(c) for c in contacts if has_details_stored(c)]
