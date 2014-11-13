from .model import CustomerCollection, Customer, Root
from .main import App


@App.dump_json(model=Customer)
def dump(self, request):
    return {
        '@type': 'Customer',
        '@id': self.id,
        'name': self.name
     }


@App.load_json()
def load(json, request):
    if json['@type'] == 'Customer':
        return Customer(name=json['name'])
    return json


@App.json(model=Customer)
def customer_default(self, request):
    return self


@App.json(model=CustomerCollection)
def customer_collection_default(self, request):
    return [
        request.link(customer) for customer in self.customers.values()
    ]


@App.json(model=CustomerCollection,
          request_method='POST',
          body_model=Customer)
def customer_collection_post(self, request):
    return self.add(request.body_obj)


@App.json(model=Root)
def root_default(self, request):
    return redirect('/customers')
