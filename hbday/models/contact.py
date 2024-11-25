from dataclasses import dataclass

from models.date import Date


@dataclass
class Contact:
    name: str
    phone_number: str
    birthdate: Date

    @classmethod
    def map(cls, response: dict) -> "Contact":
        return cls(
            name=response["names"][0]["givenName"],
            phone_number=response["phoneNumbers"][0]["canonicalForm"],
            birthdate=Date(
                month=response["birthdays"][0]["date"]["month"],
                day=response["birthdays"][0]["date"]["day"]
            )
        )
