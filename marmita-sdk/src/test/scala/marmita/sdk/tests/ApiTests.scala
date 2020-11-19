package marmita.sdk.tests

import marmita.sdk.Person
import marmita.sdk.Dataframe

import org.junit.Assert.assertThat
import org.junit.Test
import org.hamcrest.CoreMatchers._

class ApiTests {

    @Test
    def testPerson() = {
        val person = new Person("Ramón", 48)
        assertThat(person.name, is("Ramón"))
        assertThat(person.age, is(48))
        assertThat(person.action, is(true))
        assertThat(person.get_older(10), is(58))
    }

    @Test
    def testPersonByName() = {
        val personByName = Person.byName("Luis")
        assertThat(personByName.name, is("Luis"))
        assertThat(personByName.age, is(0))
        assertThat(personByName.action, is(false))
    }

    @Test
    def testPersonByAge() = {
        val personByName = Person.byAge(34)
        assertThat(personByName.name, is("A 34 years old"))
        assertThat(personByName.age, is(34))
        assertThat(personByName.action, is(true))
    }

    @Test
    def testDataframe() = {
        val df = Dataframe("customers", Seq("name", "age", "address"))
        assertThat(df.name, is("customers"))
        assertThat(df.schema, is(Seq("name", "age", "address")))
    }

}
