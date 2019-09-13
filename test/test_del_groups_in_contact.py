from model.contact import Contact
import random
from fixtura.orm import ORMFixture
from model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_del_groups_in_contact(app):
    old_contacts=db.get_contact_list()
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name="del", header="del"))
        old_groups = db.get_group_list()
    if len(old_contacts)== 0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
        old_contacts = db.get_contact_list()
    group = random.choice(old_groups)
    contacts_in_group = db.get_contacts_in_group(group)
    if len(contacts_in_group) < 1:
        random_contact=  random.choice(old_contacts)
        app.contact.add_contact_to_group(group.id, random_contact.id)
        contacts_in_group = db.get_contacts_in_group(group)
    contact= random.choice(contacts_in_group)
    app.contact.delete_group_in_contact(group.id, contact.id)
    contacts_not_in_group = db.get_contacts_not_in_group(group)
    assert contact in contacts_not_in_group


