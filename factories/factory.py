from factories import customer_factory


def create_random_customer(factory_type):
    random_customer = customer_factory.CustomerFactory().get_factory(factory_type)
    return random_customer
