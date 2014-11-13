import morepath


class App(transaction_app):
    pass


def main():
    morepath.autosetup()
    morepath.run(App())
