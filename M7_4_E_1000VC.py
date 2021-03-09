"""Fake contacts generator and measure of generation duration."""
from datetime import datetime
from faker import Faker
fake = Faker('pl_PL')


class Contacts:
    """This is a class for my business contacts."""

    def __init__(self, first_name, last_name, e_mail, phone, company, occupation, business_phone):
        """
        Construct for Contacts class.

        Parameters:
            first_name (str)
            last_name (str)
            e_mail (str)
            phone (str)
            company (str)
            occupation (str)
            business_phone (str)
        """
        self.first_name = first_name
        self.last_name = last_name
        self.e_mail = e_mail
        self.phone = phone
        self.company = company
        self.occupation = occupation
        self.business_phone = business_phone


def measure(func):
    """Measure time of function execution."""
    def wrapper():
        start_time = datetime.now()
        func()
        end_time = datetime.now()
        duration = end_time - start_time
        return f"Duration of function execution: {duration}"
    return wrapper


@measure # Is equivalent to the expression create_contacts = measure(create_contacts).
def create_contacts():
    """Create class lists od fake contacts."""
    return [Contacts(fake.first_name(), fake.last_name(), fake.company_email(), fake.phone_number(), fake.company(), fake.job(), fake.phone_number()) for _ in range(1000)]


#print(create_contacts())
