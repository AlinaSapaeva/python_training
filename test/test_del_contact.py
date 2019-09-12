from model.contact import Contact
import random

def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list())== 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == app.contact.count()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        new_contacts_from_db = map(clean, new_contacts)
        assert sorted(new_contacts_from_db, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

