class ContactHelper:

    def __init__(self, app):
        self.app=app

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact form
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion of first contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        # edit contact form
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()
        self.return_to_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_day_field_value("//div[@id='content']/form/select[1]//option[%s]", contact.bday)
        self.change_month_field_value("//div[@id='content']/form/select[2]//option[%s]", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_day_field_value("//div[@id='content']/form/select[3]//option[%s]", contact.aday)
        self.change_month_field_value("//div[@id='content']/form/select[4]//option[%s]", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_month_field_value(self, xpath, month):
        wd = self.app.wd
        if month is not None:
            if not wd.find_element_by_xpath(
                        xpath % str(int(month) + 1)).is_selected():
                wd.find_element_by_xpath(
                    xpath % str(int(month) + 1)).click()

    def change_day_field_value(self, xpath, day):
        wd = self.app.wd
        if day is not None:
            if not wd.find_element_by_xpath(
                            xpath % str(int(day) + 2)).is_selected():
                wd.find_element_by_xpath(
                    xpath % str(int(day) + 2)).click()

    def return_to_home_page(self):
        wd = self.app.wd
        # click on "home page" link
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))