from pytest import fixture

from marmitasdk.connector import Dataframe, as_seq


@fixture
def df():
    return Dataframe("customer", as_seq("name", "age", "address"))


def test_dataframe(df):
    assert df.name() == "customer"
    assert df.schema() == as_seq("name", "age", "address")
    assert str(df) == "Dataframe(customer,List(name, age, address))"
    assert repr(df) == "<java object 'marmita.sdk.Dataframe'>"


def test_dataframe_product(df):
    assert Dataframe.apply("customer", as_seq("name", "age", "address")) == df
    assert str(Dataframe.unapply(df).get()) == "(customer,List(name, age, address))"
    assert Dataframe.unapply(df).get()._1() == "customer"
    assert Dataframe.unapply(df).get()._2() == as_seq("name", "age", "address")


def test_introspection(df):
    assert df.getClass().getName() == "marmita.sdk.Dataframe"
