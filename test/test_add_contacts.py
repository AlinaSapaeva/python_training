# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix , maxlen):
    simbols = string.ascii_letters + string.digits + string.punctuation + " "*4
    return prefix + "".join([random.choice(simbols) for i in range(random.randrange(maxlen))])

def random_number(maxlen):
    symbols = string.digits
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="", fax="", email="", email2="",
                      email3="", homepage="",  address2="",
                      phone2 ="", notes="")] + [
    Contact(firstname=random_string("firstname", 5), middlename=random_string("middlename", 5),
            lastname=random_string("lastname", 5), nickname=random_string("nickname", 5),
            title=random_string("title", 5), company=random_string("company", 5),
            address=random_string("address", 5), homephone=random_number(8),
            mobilephone=random_number(8), workphone=random_number(8),
            fax=random_string("fax", 5),email=random_string("email", 5),
            email2=random_string("email2", 5), email3=random_string("email3", 5),
            homepage=random_string("homepage", 5),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10),
            notes=random_string("notes", 10),)
    for i in range(2)
]

@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts=app.contact.get_contact_list()
    app.contact.add_new(contact)
    # хеширование      == app.contact.count()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









