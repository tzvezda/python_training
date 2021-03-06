from sys import maxsize

class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, group=None,
                 address2=None, secondaryphone=None, notes=None, id = None, all_phones_from_home_page= None,
                 all_emails_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.group = group
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return self.lastname == other.lastname and self.firstname == other.firstname \
               and (self.id is None or other.id is None or self.id == other.id)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def print_contact(contact):
        return print(
            "firstname =" + contact.firstname + "; middlename = " + contact.middlename + "; lastname = " + contact.lastname +
            "; nickname = " + contact.nickname + "; title = " + contact.title + "; company = " + contact.company +
            "; address = " + contact.address + "; homephone = " + contact.homephone + "; mobilephone = " +
            contact.mobilephone + "; workphone = " + contact.workphone + "; fax = " + contact.fax + "; email = " +
            contact.email + "; email2 = " + contact.email2 + "; email3 = " + contact.email3 + "; homepage = " +
            contact.homepage + "; bday = " + str(contact.bday) + "; bmonth = " + str(contact.bmonth) + "; byear = " +
            str(contact.byear) + "; aday = " + str(contact.aday) + "; amonth = " + str(
                contact.amonth) + "; ayear = " + str(contact.ayear) +
            "; address2 = " + contact.address2 + "; secondaryphone = " + contact.secondaryphone +
            "; notes = " + contact.notes)
