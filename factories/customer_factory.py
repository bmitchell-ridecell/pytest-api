import random
from faker import Faker

from entities.customer import Customer
from configs import config

fake = Faker()


class CustomerFactory:
    factory_type = ""

    @staticmethod
    def get_factory(factory_type):
        if factory_type == "carsharing_minimal":
            return MinimalCarSharingCustomerFactory()
        elif factory_type == "carsharing_full":
            return CarSharingCustomerFactory()
        elif factory_type == "ridesharing":
            return RideSharingCustomerFactory()
        else:
            return None


class MinimalCarSharingCustomerFactory(CustomerFactory):
    class Meta:
        model = Customer

    email = "brad+pytest" + config.rand_x_digit_num(5) + "@ridecell.com"
    password = config.get('default_password')
    username = email
    phone_number = config.rand_x_digit_num(10, False)
    first_name = fake.first_name()
    last_name = fake.last_name()
    pin_number = ""


class CarSharingCustomerFactory(CustomerFactory):
    class Meta:
        model = Customer

    customer_id = 0
    phone_number = config.rand_x_digit_num(10, False)
    external_membership_number = "123456789011111"
    has_valid_payment_card = bool(random.getrandbits(1))
    mailing_address_display = fake.address()
    preferred_language = "en_US"
    sum_of_paid_drives = random.randint(0, 100)
    """not actual random user, has to be verified ridecell email and password"""
    email = "brad+pytest" + config.rand_x_digit_num(5) + "@ridecell.com"
    password = config.get('default_password')
    username = email
    first_name = fake.first_name()
    last_name = fake.last_name()


class RideSharingCustomerFactory(CustomerFactory):
    class Meta:
        model = Customer

    customer_id = 0
    username = fake.name()
    phone_number = fake.phone_number()
    mailing_address_display = fake.address()
    email = fake.email()
