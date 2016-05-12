import morepath
import morepath_rest_dump_load
from morepath_rest_dump_load import App
from webtest import TestApp as Client


def setup_module(module):
    morepath.disable_implicit()
    morepath.scan(morepath_rest_dump_load)
    morepath.commit(App)


def test_customers():
    c = Client(App())

    collection_response = c.get('/customers')
    assert collection_response.json == {
        "customers": [],
        "add": "http://localhost/customers",
        "@id": "http://localhost/customers",
        "@type": "CustomerCollection"
    }


def test_customer():
    c = Client(App())

    response = c.post_json('/customers', {'@type': 'Customer', 'name': 'Lisa'})

    new_customer_response = {
        "@id": "http://localhost/customers/0",
        "@type": "Customer",
        "name": "Lisa"
    }
    assert response.json == new_customer_response

    response = c.get('/customers/0')
    assert response.json == new_customer_response

    c.post_json('/customers', {'@type': 'Other', 'name': 'Anne'}, status=422)


def test_root():
    c = Client(App())

    c.get('/', status=302)
