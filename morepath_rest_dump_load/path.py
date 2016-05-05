from .app import App
from .model import Customer, CustomerCollection, Root, customer_collection


@App.path(model=CustomerCollection, path='customers')
def get_customer_collection():
    return customer_collection


@App.path(model=Customer, path='customers/{id}',
          converters={'id': int})
def get_customer(id):
    return customer_collection.get(id)


@App.path(model=Root, path='')
def get_root():
    return Root()
