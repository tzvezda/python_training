# -*- coding: utf-8 -*-
from model.group import Group
from random import randrange


def test_modify_group_by_index(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified_name", header="modified_header", footer="modified_footer")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)


def test_modify_group_name(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="modified_name")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_modify_group_header(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(header="modified_header")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_modify_group_footer(app):
    check_group_list_not_empty(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(footer="modified_footer")
    group.id = old_groups[index].id
    group.name = old_groups[index].name
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def check_group_list_not_empty(app):
    if app.group.count() == 0:
        #if groups list is empty then create at least one group
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))