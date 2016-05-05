class Customer(object):
    def __init__(self, name):
        self.id = None  # we will set it after creation
        self.name = name


class CustomerCollection(object):
    def __init__(self):
        self.customers = {}
        self.id_counter = 0

    def get(self, id):
        return self.customers.get(id)

    def add(self, customer):
        self.customers[self.id_counter] = customer
        # here we set the id
        customer.id = self.id_counter
        self.id_counter += 1
        return customer


# no real database, just keep things in memory for this demo
customer_collection = CustomerCollection()


# a simple root model so we can have a view for /
class Root(object):
    pass
