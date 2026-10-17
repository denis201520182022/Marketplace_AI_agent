import pytest
import secrets
from src.common.crypto import CryptoService, DecryptionError


def test_crypto_roundtrip_string():
    service = CryptoService()
    plaintext = "super_secret_wb_api_token_1234567890"
    encrypted = service.encrypt_string(plaintext)

    assert encrypted != plaintext
    assert isinstance(encrypted, str)

    decrypted = service.decrypt_string(encrypted)
    assert decrypted == plaintext


def test_crypto_roundtrip_dict():
    service = CryptoService()
    creds = {
        "client_id": "ozon_seller_123",
        "api_key": "api_sec_abcdef123456",
        "platform": "ozon",
    }
    encrypted = service.encrypt_dict(creds)
    decrypted = service.decrypt_dict(encrypted)

    assert decrypted == creds
    assert decrypted["client_id"] == "ozon_seller_123"


def test_crypto_custom_32_byte_key():
    custom_hex_key = secrets.token_hex(32)
    service = CryptoService(master_key=custom_hex_key)

    plaintext = "custom_secret_key_message"
    encrypted = service.encrypt_string(plaintext)
    assert service.decrypt_string(encrypted) == plaintext


def test_crypto_invalid_key_length():
    with pytest.raises(ValueError):
        CryptoService(master_key="too_short_key")


def test_crypto_corrupted_payload_fails():
    service = CryptoService()
    plaintext = "sensitive_data"
    encrypted = service.encrypt_string(plaintext)

    # Corrupt last character
    corrupted = encrypted[:-2] + ("A" if encrypted[-2] != "A" else "B") + encrypted[-1:]
    with pytest.raises(DecryptionError):
        service.decrypt_string(corrupted)


def test_crypto_mask_token():
    token = "wb_live_token_abcdef12345"
    masked = CryptoService.mask_token(token, prefix="wb_token", visible_tail=4)
    assert masked == "wb_token_***2345"

    short_token = "123"
    assert CryptoService.mask_token(short_token, prefix="ozon") == "ozon_***"
