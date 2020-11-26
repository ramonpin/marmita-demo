from loguru import logger

import marmitasdk.connector  # noqa: F401
from com.orange.marmita.registry.client import RegistryClient


def get_registry_handler(url, timestamp, timestamp_meta):
    return RegistryClient(url, timestamp, timestamp_meta)


def run():
    registry = get_registry_handler("url", 0, 0)
    logger.info("Starting demo...")
    logger.info(f"With registry {registry}")


if __name__ == "__main__":
    run()
