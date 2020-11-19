"""
This module extracts from main code the boilerplate code needed
to boostrap JVM integration with jpype. It must be imported as
the first import for any module that uses JVM classes. To avoid
linter errors we must use:

    import connector  # noqa FA403

With this the rest of the python code can be written in a
completly standard way without warnings.

We are sure all code runs on the same JVM because python ensures
each module is loaded just once.
"""
import os
from loguru import logger

import jpype
import jpype.imports

logger.info("Initializing marmita connector...")

# Load needed jars from current dir
base = f"{os.path.dirname(__file__)}/jars"
jars = list(map(lambda f: f"{base}/{f}", os.listdir(base)))

# Log ClassPath composition
logger.info("ClassPath:")
for jar in jars:
    logger.info(f"    {jar}")

# Bootstrap a JVM
jpype.startJVM(classpath=jars)

# Import needed components
from java.util import ArrayList  # noqa F405
from marmita.sdk.PythonUtils import toSeq as _to_seq  # noqa F405
from marmita.sdk.PythonUtils import toList as _to_list  # noqa F405
from marmita.sdk.PythonUtils import toJavaList as _to_jlist  # noqa F405
from marmita.sdk import Person, Dataframe, App  # noqa F405


# Utility functions
def as_seq(*args):
    """
    Creates a Scala Seq from arguments list
    """
    return _to_seq(ArrayList(args))


def as_list(*args):
    """
    Creates a List Seq from arguments list
    """
    return _to_list(ArrayList(args))


def as_jlist(seq):
    """
    Creates a JList from a Scala Seq
    """
    return _to_jlist(seq)
