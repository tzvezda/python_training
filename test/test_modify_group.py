# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    check_group_list_not_empty(app)
    app.group.modify_first_group(Group(name="modified_name", header="modified_header", footer="modified_footer"))

def test_modify_group_name(app):
    check_group_list_not_empty(app)
    app.group.modify_first_group(Group(name="modified_name"))


def test_modify_group_header(app):
    check_group_list_not_empty(app)
    app.group.modify_first_group(Group(header="modified_header"))


def test_modify_group_footer(app):
    check_group_list_not_empty(app)
    app.group.modify_first_group(Group(footer="modified_footer"))

def check_group_list_not_empty(app):
    if app.group.count() == 0:
        #if group list is empty then add at least one group
        app.group.create(Group(name="test_name", header="test_header", footer="test_footer"))