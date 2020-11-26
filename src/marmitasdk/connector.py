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

if not jpype.isJVMStarted():
    logger.info("Initializing marmita connector...")

    # Load needed jars from current dir
    _base = f"{os.path.dirname(__file__)}"
    _jars_dir = f"{_base}/jars"
    _jars = list(map(lambda f: f"{_jars_dir}/{f}", os.listdir(_jars_dir)))

    # Log ClassPath composition
    logger.info("ClassPath:")
    for jar in _jars:
        logger.info(f"    {jar}")

    # Bootstrap a JVM
    _jvmPath = jpype.getDefaultJVMPath()
    logger.info(f"JVM used {_jvmPath}")
    jpype.startJVM(_jvmPath, f"-Dlog4j.configurationFile={_base}/log4j/log4j2.xml", classpath=_jars)
