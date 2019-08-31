# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts=app.contact.get_contact_list()
    contact=Contact(firstname="Alina", middlename="Maratovna",lastname="Sapaeva", nickname="hhh",title="gsdhfg",
company="ggygg", address="gyfhg", home="frrg", mobile="9030620645",  work="gfgdghyfyu", fax="ggfgf", email="gyfgf",   email2="gdtr",
email3="nbjhg", homepage="ggfdghb", bday="12", bmonth="March", byear="1994", aday="17", amonth="May", ayear="2000", address2="gffgjf",
phone2 ="fygfsdf",  notes="hgk")
    app.contact.add_new(contact)
    # хеширование      == app.contact.count()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_add_empty_contact(app):
    old_contacts=app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="",lastname="", nickname="",title="",
company="", address="", home="", mobile="",  work="", fax="", email="",   email2="",
email3="", homepage="", bday="-", bmonth="-", byear="-", aday="-", amonth="-", ayear="-", address2="",
phone2 ="",  notes="")
    app.contact.add_new(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts=app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








