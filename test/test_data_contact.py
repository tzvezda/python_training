import re
from random import randrange
from model.contact import Contact

def test_phones_on_home_page(app):
    check_contact_list_is_not_empty(app)
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)

def test_names_on_home_page(app):
    check_contact_list_is_not_empty(app)
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == remove_spaces_at_the_beginning(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == remove_spaces_at_the_beginning(contact_from_edit_page.firstname)

def test_address_on_home_page(app):
    check_contact_list_is_not_empty(app)
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == remove_spaces_at_the_beginning(contact_from_edit_page.address)

def test_emails_on_home_page(app):
    check_contact_list_is_not_empty(app)
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = contacts_list[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_info_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]","",s)

def remove_spaces_at_the_beginning(s):
    return re.sub("^\s*","",s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map (lambda x: clear(x),
                                  filter(lambda x: x is not None,
                                         [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter (lambda x: x != "",
                             map (lambda x: remove_spaces_at_the_beginning(x),
                                  filter(lambda x: x is not None,
                                         [contact.email, contact.email2, contact.email3]))))

def check_contact_list_is_not_empty(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname"))