import pymysql.cursors
from fixtura.orm import ORMFixture
from model.group import Group

db = ORMFixture(host = "127.0.0.1", name = "addressbook", user = "root", password = "")
"""
try:
   groups = db.get_group_list()
   for group in groups:
       print(group)
   print(len(groups))
finally:
    pass
"""

try:
   contacts = db.get_contacts_not_in_group(Group(id ="221"))
   for contact in contacts:
       print(contact)
   print(len(contacts))
finally:
    pass
