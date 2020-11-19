from marmitasdk.connector import App


def test_greet():
    assert App.getGreeting() == "Hello world."


def test_check():
    assert App.check(True) is False


def test_main():
    assert App.main(None) is None


def test_repr_and_str():
    assert str(App) == "<java class 'marmita.sdk.App'>"
    assert repr(App) == "<java class 'marmita.sdk.App'>"


def test_introspection():
    assert App.class_.getName() == "marmita.sdk.App"
