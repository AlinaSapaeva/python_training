from model.group import Group

def test_modify_first_group(app):
    app.group.modify(Group(name="edit", header="edit", footer="edit"))

def test_modify_group_name(app):
    app.group.modify(Group(name="new_name"))

def test_modify_group_header(app):
    app.group.modify(Group(header ="new_header"))
