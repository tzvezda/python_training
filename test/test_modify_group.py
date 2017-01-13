# -*- coding: utf-8 -*-
from model.group import Group


def test_modify_first_group(app):
    app.group.modify_first_group(Group(name="modified_name", header="modified_header", footer="modified_footer"))


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="modified_name"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="modified_header"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="modified_footer"))
