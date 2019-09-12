from model.contact import Contact
import random


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    index = old_contacts.index(contact)
    contact_data = Contact(firstname="edit", lastname="edit")
    contact_data.id = contact.id
    app.contact.modify_contact_by_index(contact_data,index)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact_data
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        new_contacts_from_db = map(clean, new_contacts)
        assert sorted(new_contacts_from_db, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


"""
def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="new_name")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middlename="new_name")
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
"""