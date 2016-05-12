import morepath
from .model import CustomerCollection, Customer, Root
from .app import App


@App.dump_json(model=Customer)
def dump_customer(self, request):
    return {
        '@type': 'Customer',
        '@id': request.link(self),
        'name': self.name
    }


@App.dump_json(model=CustomerCollection)
def dump_customer_collection(self, request):
    return {
        '@id': request.link(self),
        '@type': 'CustomerCollection',
        'customers': [
            request.link(customer) for customer in self.customers.values()
        ],
        'add': request.link(self),
    }


@App.load_json()
def load_customer(json, request):
    if json['@type'] == 'Customer':
        return Customer(name=json['name'])
    return json


@App.json(model=Customer)
def customer_default(self, request):
    return self


@App.json(model=CustomerCollection)
def customer_collection_default(self, request):
    return self


@App.json(model=CustomerCollection,
          request_method='POST',
          body_model=Customer)
def customer_collection_post(self, request):
    return self.add(request.body_obj)


@App.json(model=Root)
def root_default(self, request):
    return morepath.redirect('/customers')
