# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="fn1", middlename="mn1", lastname="ln1", nickname="nn1",
                            title="title1", company="company1", address="address1", home="home1", mobile="mobile1",
                            work="work1", fax="fax1", email="email1@mail.ru1", email2="email2@mail.ru2",
                            email3="email3@mail.ru3", homepage="homepage1.com1", bday="2",bmonth="4", byear="1980",
                            aday="6", amonth="5", ayear="1990", group="", address2="address2_1",phone2="123321",
                            notes="text_notes1"))
        self.logout()

    def test_add_empty_contact(self):
        self.login(username="admin", password="secret")
        self.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",
                            company="", address="", home="", mobile="", work="", fax="",
                            email="", email2="", email3="", homepage="", bday="0", bmonth="0", byear="", aday="0",
                            amonth="0", ayear="", group="", address2="", phone2="", notes=""))
        self.logout()


    def logout(self):
        # logout
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def create_contact(self, contact):
        wd = self.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(int(contact.bday)+2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % str(int(contact.bday)+2)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(int(contact.bmonth)+1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % str(int(contact.bmonth)+1)).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(int(contact.aday)+2)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[%s]" % str(int(contact.aday)+2)).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(int(contact.amonth)+1)).is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[%s]" % str(int(contact.amonth)+1)).click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_home_page(self):
        wd = self.wd
        # open homepage
        wd.get("http://localhost/addressbook/")


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
