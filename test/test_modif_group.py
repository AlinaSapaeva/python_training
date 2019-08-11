from model.group import Group

def test_modify_first_group(app):
    if app.group.count()==0:
        app.group.create(Group(name="del", header="del"))
    old_groups=app.group.get_group_list()
    app.group.modify(Group(name="edit", header="edit", footer="edit"))
    new_groups=app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_name(app):
    if app.group.count()==0:
        app.group.create(Group(name="del", header="del"))
    old_groups=app.group.get_group_list()
    app.group.modify(Group(name="new_name"))
    new_groups=app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count()==0:
        app.group.create(Group(name="del", header="del"))
    old_groups=app.group.get_group_list()
    app.group.modify(Group(header ="new_header"))
    new_groups=app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
