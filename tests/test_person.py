from pytest import fixture
from marmitasdk.connector import Person


@fixture
def person():
    return Person("Ramón", 48)


def test_person(person):
    assert person.name() == "Ramón"
    assert person.age() == 48
    assert person.action() is True
    assert person.get_older(10) == 58


def test_person_by_name():
    person = Person.byName("Luis")
    assert person.name() == "Luis"
    assert person.age() == 0
    assert person.action() is False


def test_person_by_age():
    person = Person.byAge(25)
    assert person.name() == "A 25 years old"
    assert person.age() == 25
    assert person.action() is True


def test_repr_and_str(person):
    assert str(person) == "Person(Ramón, 48)"
    assert repr(person) == "<java object 'marmita.sdk.Person'>"


def test_introspection(person):
    assert person.getClass().getName() == "marmita.sdk.Person"
