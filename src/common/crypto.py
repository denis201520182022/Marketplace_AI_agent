import base64
import json
import os
from typing import Any, Dict, Optional, Union
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


class CryptoError(Exception):
    """Base exception for cryptographic operations."""
    pass


class DecryptionError(CryptoError):
    """Raised when decryption fails or authentication tag is invalid."""
    pass


class CryptoService:
    """
    Cryptographic service for symmetric AES-256-GCM encryption of sensitive data
    such as seller marketplace API tokens and OAuth credentials.
    """

    def __init__(self, master_key: Optional[str] = None):
        """
        Initializes CryptoService with 32-byte key.
        Accepts: 64-char hex string, urlsafe-base64, or raw 32-byte string/bytes.
        """
        raw_key = master_key or os.getenv(
            "SECRET_KEY_ENCRYPTION",
            "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
        )
        self.key = self._normalize_key(raw_key)
        self.aesgcm = AESGCM(self.key)

    @staticmethod
    def _normalize_key(raw_key: Union[str, bytes]) -> bytes:
        if isinstance(raw_key, str):
            # Check if 64-char hex
            if len(raw_key) == 64:
                try:
                    return bytes.fromhex(raw_key)
                except ValueError:
                    pass
            # Check if base64
            try:
                decoded = base64.urlsafe_b64decode(raw_key.encode("utf-8"))
                if len(decoded) == 32:
                    return decoded
            except Exception:
                pass
            raw_bytes = raw_key.encode("utf-8")
        else:
            raw_bytes = raw_key

        if len(raw_bytes) != 32:
            raise ValueError(
                f"AES-256 requires exactly 32 bytes (256 bits). Received {len(raw_bytes)} bytes."
            )
        return raw_bytes

    def encrypt_string(self, plaintext: str) -> str:
        """
        Encrypts plaintext string with AES-256-GCM.
        Returns base64 encoded string: base64(12_byte_nonce + ciphertext_with_tag).
        """
        if not plaintext:
            return ""
        nonce = os.urandom(12)  # 96-bit nonce for AES-GCM
        ciphertext = self.aesgcm.encrypt(nonce, plaintext.encode("utf-8"), None)
        combined = nonce + ciphertext
        return base64.urlsafe_b64encode(combined).decode("utf-8")

    def decrypt_string(self, encrypted_payload: str) -> str:
        """
        Decrypts base64 encoded payload produced by encrypt_string.
        Raises DecryptionError on failure.
        """
        if not encrypted_payload:
            return ""
        try:
            raw = base64.urlsafe_b64decode(encrypted_payload.encode("utf-8"))
            if len(raw) < 28:  # 12 bytes nonce + 16 bytes auth tag minimum
                raise DecryptionError("Payload too short to be valid AES-GCM ciphertext.")
            nonce = raw[:12]
            ciphertext = raw[12:]
            decrypted_bytes = self.aesgcm.decrypt(nonce, ciphertext, None)
            return decrypted_bytes.decode("utf-8")
        except Exception as e:
            if isinstance(e, DecryptionError):
                raise
            raise DecryptionError(f"Decryption failed: {str(e)}") from e

    def encrypt_dict(self, data: Dict[str, Any]) -> str:
        """Serializes dictionary to JSON and encrypts it."""
        serialized = json.dumps(data, ensure_ascii=False)
        return self.encrypt_string(serialized)

    def decrypt_dict(self, encrypted_payload: str) -> Dict[str, Any]:
        """Decrypts payload and parses JSON dictionary."""
        decrypted_str = self.decrypt_string(encrypted_payload)
        return json.loads(decrypted_str)

    @staticmethod
    def mask_token(token: Optional[str], prefix: str = "", visible_tail: int = 4) -> str:
        """
        Safely masks tokens for logging and audit traces.
        Example: 'eyJhbGciOiJIUz...' -> 'wb_token_***5a1c'
        """
        if not token:
            return ""
        clean_token = token.strip()
        if len(clean_token) <= visible_tail:
            return f"{prefix}_***" if prefix else "***"
        tail = clean_token[-visible_tail:]
        if prefix:
            return f"{prefix}_***{tail}"
        return f"***{tail}"


default_crypto = CryptoService()
