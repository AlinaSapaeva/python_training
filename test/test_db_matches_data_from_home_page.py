from model.contact import Contact
from fixtura.orm import ORMFixture

def test_db_matches_data_from_home_page(app, db):
    all_contacts_from_ui = app.contact.get_contact_list()
    all_contacts_from_db = db.get_contact_list()
    assert sorted(all_contacts_from_ui, key=Contact.id_or_max) == sorted(all_contacts_from_db, key=Contact.id_or_max)

def test_db_matches_data_from_home_page_use_orm(app, db):
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    all_contacts_from_ui = app.contact.get_contact_list()
    all_contacts_from_db = db.get_contact_list()
    assert sorted(all_contacts_from_ui, key=Contact.id_or_max) == sorted(all_contacts_from_db, key=Contact.id_or_max)