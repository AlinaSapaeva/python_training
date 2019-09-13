from model.contact import Contact
from fixtura.orm import ORMFixture
import re
from random import randrange

"""
def test_db_matches_data_from_home_page(app, db):
    all_contacts_from_ui = app.contact.get_contact_list()
    all_contacts_from_db = db.get_contact_list()
    assert sorted(all_contacts_from_ui, key=Contact.id_or_max) == sorted(all_contacts_from_db, key=Contact.id_or_max)

def test_db_matches_data_from_home_page_use_orm(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    all_contacts_from_ui = app.contact.get_contact_list()
    all_contacts_from_db = db.get_contact_list()
    assert sorted(all_contacts_from_ui, key=Contact.id_or_max) == sorted(all_contacts_from_db, key=Contact.id_or_max)
"""

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_db_matches_data_from_home_page_use_orm(app):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    print(contacts_from_db)
    print(contacts_from_home_page)
    for contact_from_hp, contact_from_db in zip(contacts_from_home_page, contacts_from_db):
        assert contact_from_hp.firstname == contact_from_db.firstname
        assert contact_from_hp.lastname == contact_from_db.lastname
        assert contact_from_hp.address == contact_from_db.address
        assert contact_from_hp.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)
        assert contact_from_hp.all_emails__from_home_page == merge_emails_like_on_home_page(contact_from_db)


def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip(),
                       address=contact.address,
                       homephone =contact.homephone, mobilephone =contact.mobilephone,
                       workphone =contact.workphone, phone2=contact.phone2,
                       email =contact.email, email2 =contact.email2, email3 =contact.email3)

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                          map(lambda x: clear(x),
                                               filter(lambda x: x is not None,
                                               [contact.homephone, contact.mobilephone, contact.workphone, contact.phone2 ]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                               filter(lambda x: x is not None,
                                               [contact.email, contact.email2, contact.email3])))