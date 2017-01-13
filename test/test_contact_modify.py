# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_first_contact(app):
    app.contact.modify_first_contact (Contact(firstname="TEST1", middlename="TEST1", lastname="TEST1", nickname="TEST1", title="TEST1",
                               company="TEST1", address="TEST1", home="TEST1", mobile="TEST1", work="TEST1", fax="TEST1",
                               email="TEST1", email2="TEST1", email3="TEST1", homepage="TEST1", bday="0",
                               bmonth="0", byear="1990", aday="0", amonth="0", ayear="1990", group="TEST1",
                               address2="TEST1", phone2="TEST1", notes="TEST1"))