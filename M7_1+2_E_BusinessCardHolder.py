class BusinessCardHolder:
    def __init__(self, first_name, last_name, company, occupation, e_mail):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.occupation = occupation
        self.e_mail = e_mail
        # Variables
        self.label_max = 16

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.e_mail}'

    def __repr__(self):
        # return f"\nfirst_name={self.first_name} last_name={self.last_name}, company={self.company}, occupation={self.occupation}, e_mail={self.e_mail}"
        return f"\nfirst_name={self.first_name} last_name={self.last_name}, e_mail={self.e_mail}"

    def contact(self):
        return f"Kontaktuję się z {self.first_name} {self.last_name} , {self.e_mail}"

    @property
    def label_length(self):
        return len(f"{self.first_name} {self.last_name}")

    # @label_length.setter
    @property
    def length_check(self):
        if self.label_length <= self.label_max:
            return f"Name {self.first_name} {self.last_name} fits in the address line"
        else:
            try:
                raise ValueError()
            except ValueError:
                return f"Name {self.first_name} {self.last_name} is to long - {self.label_length} characters; exceeds top length of address line: 15 characters"


class BaseContact(BusinessCardHolder):
    def __init__(self, first_name, last_name, e_mail, phone):
        super().__init__(first_name, last_name, None, None, e_mail)
        self.phone = phone

    def contact(self):
        return f"wybieram numer {self.phone} i dzwonię do {self.first_name} {self.last_name}"


class BusinessContact(BusinessCardHolder):
    def __init__(self, first_name, last_name, company, occupation, business_phone):
        super().__init__(first_name, last_name, company, occupation, None)
        self.business_phone = business_phone

    def __str__(self):
        return f'{self.first_name} {self.last_name} : {self.business_phone}'

    def contact(self):
        return f"wybieram numer {self.business_phone} i dzwonię do {self.first_name} {self.last_name}"


f_one = BusinessCardHolder('Konstanty', 'Wiercigroch', 'Małyszek-Hawro Sp.k.',
                           'Projektant gier komputerowych', 'langieralbert@ppuh.pl')
f_two = BusinessCardHolder('Leonard', 'Micał', 'Grupa Helman i syn s.c.',
                           'Babcia klozetowa', 'albert44@fundacja.net')
f_three = BusinessCardHolder('Antoni', 'Towarek', 'Gabinety Józefczak-Demiańczuk s.c.',
                             'Ekonomista', 'henniganna-maria@frydrychowicz-oglaza.org')
f_four = BusinessCardHolder('Julianna', 'Matraszek', 'Spółdzielnia Sobstyl-Pasztaleniec Sp. z o.o.',
                            'Architekt krajobrazu', 'hubert89@grupa.pl')
f_five = BusinessCardHolder(
                            'Kaja', 'Włodarz', 'Gabinety Kapka', 'Archeolog', 'sgraj@gabinety.com')
# print(f_five)

f_one1 = BaseContact('Eryk', 'Mazanek', 'alan42@ppuh.com', '+48 693 903 040')
f_two1 = BaseContact('Bianka', 'Pokusa',
                     'pdruszcz@gabinety.com', '881 648 733')
f_three1 = BaseContact('Malwina', 'Szymajda',
                       'nicole30@andziak-fac.com', '32 267 38 99')
f_four1 = BaseContact('Cyprian', 'Strug',
                      'sylwia53@kuczak-byzdra.com', '+48 507 810 876')
f_five1 = BaseContact('Tymoteusz', 'Maleszka',
                      'wieczerzaknicole@fpuh.pl', '+48 609 683 414')
# print(f_five1)

f_one2 = BusinessContact('Michał', 'Myszk', 'Flasza Sp.k.',
                         'Terminolog', '+48 517 350 851')
f_two2 = BusinessContact(
    'Paweł', 'Kwapis', 'Wieczerzak-Lepa Sp. z o.o.', 'Portier', '606 560 282')
f_three2 = BusinessContact(
    'Borys', 'Cyman', 'Stowarzyszenie Łuszczak', 'Trener', '787 732 062')
f_four2 = BusinessContact(
    'Sara', 'Gula', 'Nędzi Sp. z o.o.', 'Żołnierz', '694 800 592')
f_five2 = BusinessContact(
    'Monika', 'Kudlak', 'Kłosiewicz-Nitkiewicz Sp. z o.o. Sp.k.', 'Architekt krajobrazu', '536 817 956')
# print(f_five2)

new_friends = [f_one, f_two, f_three, f_four, f_five]
# for friend in new_friends:
#    print(friend.first_name, friend.last_name, ":", friend.e_mail)

by_first_name = sorted(new_friends, key=lambda friend: friend.first_name)
# print(by_first_name)
by_last_name = sorted(new_friends, key=lambda friend: friend.last_name)
# print(by_last_name)
by_e_mail = sorted(new_friends, key=lambda friend: friend.e_mail)
# print(by_e_mail)

# print(BusinessCardHolder.contact(f_two))
print(f_two.contact())
print(f_one1.contact())
print(f_three2.contact())

# print(f_one.name_length)
print(f_three.length_check)
print(f_five1.length_check)
print(f_four2.length_check)
