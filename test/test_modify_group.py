# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    group = Group(name="modified_name", header="modified_header", footer="modified_footer")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_modify_group_name(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    group = Group(name="modified_name")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_modify_group_header(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    group = Group(header="modified_header")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_modify_group_footer(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    group = Group(footer="modified_footer")
    group.id = old_groups[0].id
    group.name = old_groups[0].name
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def check_group_list_not_empty(app):
    if app.group.count() == 0:
        #if groups list is empty then create at least one group
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))