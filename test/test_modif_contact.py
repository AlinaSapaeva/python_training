from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    app.contact.modify_first_contact(Contact(firstname="edit", middlename="edit",lastname="edit", nickname="edit",title="edit",
company="ggygg", address="gyfhg", home="frrg", mobile="9030620633",  work="gfgdghyfyu", fax="ggfgf", email="gyfgf",   email2="gdtr",
email3="nbjhg", homepage="ggfdghb",bday="15", bmonth="May", byear="1993", aday="10", amonth="March", ayear="2001", address2="gffgjf",
phone2 ="fygfsdf",  notes="hgk"))

def test_modify_contact_name(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    app.contact.modify(Contact(firstname="new_name"))

def test_modify_contact_middlename(app):
    if app.contact.count()==0:
        app.contact.add_new(Contact(firstname="del", middlename="del"))
    app.contact.modify(Contact(middlename="new_name"))