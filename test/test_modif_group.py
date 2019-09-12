from model.group import Group
import random

def test_modify_first_group(app, db, check_ui):
    if len(db.get_group_list())== 0:
        app.group.create(Group(name="first", header="first"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    index = old_groups.index(group)
    group_data = Group(name="edit", header="edit", footer="edit")
    group_data.id = group.id
    app.group.modify_group_by_id(group_data, group.id)
    # хеширование == app.group.count()
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group_data
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups_from_db = map(clean, new_groups)
        assert sorted(new_groups_from_db, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
 #   assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


"""
def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first", header="first"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(name="new_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="first", header="first"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header ="new_header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
"""