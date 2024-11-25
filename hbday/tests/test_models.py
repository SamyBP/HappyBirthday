import unittest

from models.contact import Contact
from models.date import Date


class DateTests(unittest.TestCase):

    def test_whenNow_createsDateInstance(self):
        date = Date.now()
        self.assertIsInstance(date, Date)


class ContactTests(unittest.TestCase):

    def test_whenCheckingContactBirthday_notEquals(self):
        given_date = Date(10, 5)
        contact = Contact(name="Test", phone_number="test", birthdate=Date(4, 5))

        self.assertNotEqual(contact.birthdate, given_date)

    def test_whenCheckingContactBirthday_equals(self):
        given_date = Date(month=10, day=5)
        contact = contact = Contact(name="Test", phone_number="test", birthdate=Date(month=10, day=5))

        self.assertEqual(contact.birthdate, given_date)
