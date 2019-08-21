from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = app.contact.get_contact_list
    index = randrange(len(old_contacts))
    contact =Contact(firstname="edit", middlename="edit",lastname="edit", nickname="edit",title="edit",
company="ggygg", address="gyfhg", home="frrg", mobile="9030620633",  work="gfgdghyfyu", fax="ggfgf", email="gyfgf",   email2="gdtr",
email3="nbjhg", homepage="ggfdghb",bday="15", bmonth="May", byear="1993", aday="10", amonth="March", ayear="2001", address2="gffgjf",
phone2 ="fygfsdf",  notes="hgk")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(contact, index)
    app.return_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = app.contact.get_contact_list
    contact = Contact(firstname="new_name")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = app.contact.get_contact_list
    contact = Contact(middlename="new_name")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) == len(new_contacts)
