# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fn1", middlename="mn1", lastname="ln1", nickname="nn1",
                      title="title1", company="company1", address="address1", homephone="home1", mobilephone="mobile1",
                      workphone="work1", fax="fax1", email="email1@mail.ru1", email2="email2@mail.ru2",
                      email3="email3@mail.ru3", homepage="homepage1.com1", bday="2", bmonth="4", byear="1980",
                      aday="6", amonth="5", ayear="1990", group="", address2="address2_1", secondaryphone="123321",
                      notes="text_notes1")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",
                      company="", address="", homephone="", mobilephone="", workphone="", fax="",
                      email="", email2="", email3="", homepage="", bday="0", bmonth="0", byear="", aday="0",
                      amonth="0", ayear="", group="", address2="", secondaryphone="", notes="")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)