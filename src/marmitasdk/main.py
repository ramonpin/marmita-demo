from loguru import logger

import marmitasdk.connector  # noqa FA403
from marmitasdk.connector import as_seq
from marmitasdk.connector import Person, Dataframe, App


def run():
    # Custom class with companion object
    person = Person.byName("Ramón")
    logger.info(person)

    # Case class
    df = Dataframe("customers", as_seq("name", "age", "address"))
    logger.info(df)

    # Object
    greet = App.getGreeting()
    logger.info(greet)


if __name__ == "__main__":
    run()
