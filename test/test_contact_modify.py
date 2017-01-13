# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    check_contact_list_is_not_empty(app)
    app.contact.modify_first_contact (Contact(firstname="TEST1", middlename="TEST1", lastname="TEST1", nickname="TEST1", title="TEST1",
                               company="TEST1", address="TEST1", home="TEST1", mobile="TEST1", work="TEST1", fax="TEST1",
                               email="TEST1", email2="TEST1", email3="TEST1", homepage="TEST1", bday="0",
                               bmonth="0", byear="1990", aday="0", amonth="0", ayear="1990", group="TEST1",
                               address2="TEST1", phone2="TEST1", notes="TEST1"))



def test_modify_contact_firstname(app):
    check_contact_list_is_not_empty(app)
    app.contact.modify_first_contact (Contact(firstname="changed_firstname"))


def test_modify_contact_lastname(app):
    check_contact_list_is_not_empty(app)
    app.contact.modify_first_contact(Contact(lastname="changed_lastname"))


def test_modify_contact_middlename(app):
    check_contact_list_is_not_empty(app)
    app.contact.modify_first_contact(Contact(middlename="changed_middlename"))


def check_contact_list_is_not_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname"))