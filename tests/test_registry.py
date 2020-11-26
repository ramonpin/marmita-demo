import marmitasdk.connector   # noqa: F401
from marmitasdk.main import get_registry_handler


def test_registry():
    registry = get_registry_handler("url", 0, 0)
    assert registry is not None
