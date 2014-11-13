import morepath


class App(morepath.App):
    pass


def main():
    morepath.autosetup()
    morepath.run(App())
