# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="fn1", middlename="mn1", lastname="ln1", nickname="nn1",
                        title="title1", company="company1", address="address1", home="home1", mobile="mobile1",
                        work="work1", fax="fax1", email="email1@mail.ru1", email2="email2@mail.ru2",
                        email3="email3@mail.ru3", homepage="homepage1.com1", bday="2",bmonth="4", byear="1980",
                        aday="6", amonth="5", ayear="1990", group="", address2="address2_1",phone2="123321",
                        notes="text_notes1"))
    app.logout()

def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                        company="", address="", home="", mobile="", work="", fax="",
                        email="", email2="", email3="", homepage="", bday="0", bmonth="0", byear="", aday="0",
                        amonth="0", ayear="", group="", address2="", phone2="", notes=""))
    app.logout()