from model.group import Group


def test_modify_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="edit", header="edit", footer="edit"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="new_name"))
    app.session.logout()

def test_modify_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(header ="new_header"))
    app.session.logout()