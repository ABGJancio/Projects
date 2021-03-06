"""Fake contacts generator."""
from faker import Faker
fake = Faker('pl_PL')


def create_contacts(kind, q):
    """Create class lists od fake contacts."""
    if kind == "BusinessCardHolder":
        new_card_contacts = [(fake.first_name(), fake.last_name(
        ), fake.company(), fake.job(), fake.company_email()) for _ in range(q)]
        with open("BusinessCardHolder.txt", 'w') as write_file:
            write_file.write(str(new_card_contacts))
        return new_card_contacts
    elif kind == "BaseContacts":
        base_contacts = [(fake.first_name(), fake.last_name(
        ), fake.company_email(), fake.phone_number()) for _ in range(q)]
        with open("BaseContacts.txt", 'w') as write_file:
            write_file.write(str(base_contacts))
        return base_contacts
    elif kind == "BusinessContacts":
        business_contacts = [(fake.first_name(), fake.last_name(
        ), fake.company(), fake.job(), fake.phone_number()) for _ in range(q)]
        with open("BusinessContacts.txt", 'w') as write_file:
            write_file.write(str(business_contacts))
        return business_contacts
    else:
        return "Set right kind!"


create_contacts("BusinessCardHolder", 5)
create_contacts("BaseContacts", 5)
create_contacts("BusinessContacts", 5)
