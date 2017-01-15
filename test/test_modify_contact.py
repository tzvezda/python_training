# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    check_contact_list_is_not_empty(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="TEST1", middlename="TEST1", lastname="TEST1", nickname="TEST1", title="TEST1",
                                  company="TEST1", address="TEST1", home="TEST1", mobile="TEST1", work="TEST1", fax="TEST1",
                                  email="TEST1", email2="TEST1", email3="TEST1", homepage="TEST1", bday="0",
                                  bmonth="0", byear="1990", aday="0", amonth="0", ayear="1990", group="TEST1",
                                  address2="TEST1", phone2="TEST1", notes="TEST1")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact (contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname(app):
    check_contact_list_is_not_empty(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="changed_firstname")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    app.contact.modify_first_contact (contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    check_contact_list_is_not_empty(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="changed_lastname")
    contact.id = old_contacts[0].id
    contact.firstname = old_contacts[0].firstname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_middlename(app):
    check_contact_list_is_not_empty(app)
    old_contacts = app.contact.get_contact_list()
    contact = Contact(middlename="changed_middlename")
    contact.id = old_contacts[0].id
    contact.lastname = old_contacts[0].lastname
    contact.firstname = old_contacts[0].firstname
    app.contact.modify_first_contact(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def check_contact_list_is_not_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname"))