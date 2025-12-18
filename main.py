from faker import Faker
import logging

class BaseContact:
    def __init__(self, first_name, last_name, email_address, private_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone = private_phone
        self.email_address = email_address

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email_address} {self.private_phone}'
    
    def contact(self):
        print(f'Wybieram numer {self.private_phone} i dzwnonie do {self.first_name} {self.last_name}')
    
    @property
    def label_length(self):
        return len(f'{self.first_name}{self.last_name}')



class BusinessContact(BaseContact):
    def __init__(self, company_name, position, company_phone, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.company_phone = company_phone


    def __str__(self):
        return super().__str__() + ' ' + f'{self.company_name} {self.position} {self.company_phone}'
    
    def contact(self):
        print(f'Wybieram numer {self.company_phone} i dzwnonie do {self.first_name} {self.last_name}')



def create_contacts(contact_type, number):
    fake = Faker()
    contact_cards = []
    if number > 0:
        for i in range(number):
            if contact_type == 'base':
                contact_card = BaseContact(
                    first_name = fake.first_name(),
                    last_name = fake.last_name(),
                    email_address = fake.email(),
                    private_phone = fake.phone_number().replace('x', '').replace('.', '')
                )
                contact_cards.append(contact_card)
            elif contact_type == 'business':
                contact_card = BusinessContact(
                    first_name = fake.first_name(),
                    last_name = fake.last_name(),
                    company_name = fake.company(),
                    position = fake.job(),
                    email_address = fake.email(),
                    private_phone = fake.phone_number().replace('x', '').replace('.', ''),
                    company_phone = fake.phone_number().replace('x', '').replace('.', '')
                )
                contact_cards.append(contact_card)
            else:
                logging.error('Inappropriate contact type!')
                return 'Error'
    else:
        logging.error('Number must be greater than zero!')
        return 'Error'
    return contact_cards
    
def display_cards(list_with_cards):
    for card in list_with_cards:
        print(card)




if __name__ == '__main__':

    ############### TESTING BusinessContact #########################
    print('############### TESTING BusinessContact #########################')

    list_with_5_business_contacts = create_contacts('business', 5)
    display_cards(list_with_5_business_contacts)
    print("----------- Sorted by first name -------------")
    cards_sorted_by_fn = sorted(list_with_5_business_contacts, key=lambda business_card: business_card.first_name)
    display_cards(cards_sorted_by_fn)
    print("----------- Sorted by last name -------------")
    cards_sorted_by_ln = sorted(list_with_5_business_contacts, key=lambda business_card: business_card.last_name)
    display_cards(cards_sorted_by_ln)
    print("----------- Sorted by email address -------------")
    cards_sorted_by_email = sorted(list_with_5_business_contacts, key=lambda business_card: business_card.email_address)
    display_cards(cards_sorted_by_email)
    print("-----------------------------------------------")
    # testing dynamic attribut '_label_length'
    print('-------- testing dynamic attribut label_length ----------')
    for card in list_with_5_business_contacts:
        print(f'{card} || {len(card.first_name)} + {len(card.last_name)} = {card.label_length}')
    print("-----------------------------------------------")
    for card in list_with_5_business_contacts:
        card.contact()


    ############### TESTING BaseContact #########################
    print('############### TESTING BaseContact #########################')

    list_with_3_base_contacts = create_contacts('base', 3)
    display_cards(list_with_3_base_contacts)
    print("----------- Sorted by first name -------------")
    cards_sorted_by_fn = sorted(list_with_3_base_contacts, key=lambda business_card: business_card.first_name)
    display_cards(cards_sorted_by_fn)
    print("----------- Sorted by last name -------------")
    cards_sorted_by_ln = sorted(list_with_3_base_contacts, key=lambda business_card: business_card.last_name)
    display_cards(cards_sorted_by_ln)
    print("----------- Sorted by email address -------------")
    cards_sorted_by_email = sorted(list_with_3_base_contacts, key=lambda business_card: business_card.email_address)
    display_cards(cards_sorted_by_email)
    print("-----------------------------------------------")
    # testing dynamic attribut '_label_length'
    print('-------- testing dynamic attribut label_length ----------')
    for card in list_with_3_base_contacts:
        print(f'{card} || {len(card.first_name)} + {len(card.last_name)} = {card.label_length}')
    print("-----------------------------------------------")
    for card in list_with_3_base_contacts:
        card.contact()

    print("-----------------------------------------------")
    ### Test - inappropriate contact type ###
    print('### Test - inappropriate contact type ###')
    create_contacts('hello', 3)

    print("-----------------------------------------------")
    ### Test - 0 cards ###
    print('### Test - 0 cards ###')
    create_contacts('business', 0)