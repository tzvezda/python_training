from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test_firstname", middlename="test_middlename", lastname="test_lastname"))
    app.contact.delete_first_contact()