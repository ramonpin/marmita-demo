package marmita.sdk

// Just some demo classes

case class Dataframe(name: String, schema: Seq[String])

class Person(val name: String, val age: Int) {

    var action: Boolean = true
    def get_older(by: Int): Int = age + by
    override def toString() = f"Person(${name}, ${age})"

}

object Person {

    def byName(name: String) = {
        val thePerson = new Person(name, 0)
        thePerson.action = false
        thePerson
    }

    def byAge(age: Int) = new Person(f"A ${age} years old", age)

}

object App {
    def getGreeting: String = "Hello world."
    def main(args: Array[String]): Unit = println(App.getGreeting)
    def check(b: Boolean): Boolean = !b
}
