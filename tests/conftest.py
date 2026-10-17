import pytest
from src.common.crypto import CryptoService


@pytest.fixture
def crypto_service() -> CryptoService:
    """Fixture providing an instance of CryptoService with default test key."""
    return CryptoService()
