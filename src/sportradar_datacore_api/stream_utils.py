"""Helpers for decoding DataCore streaming payloads."""

import base64
import json
import zlib

from sportradar_datacore_api.errors import UnexpectedResponseError
from sportradar_datacore_api.stream_models import StreamMessage


def decode_compressed_data(encoded_data: str) -> object:
    """Decode a base64-encoded zlib-compressed JSON payload."""
    try:
        compressed_data = base64.b64decode(encoded_data.encode("utf-8"))
    except ValueError as exc:
        raise UnexpectedResponseError("Invalid base64 compressedData payload.") from exc

    try:
        decoded_text = zlib.decompress(compressed_data).decode("utf-8")
    except (zlib.error, UnicodeDecodeError) as exc:
        raise UnexpectedResponseError("Invalid zlib compressedData payload.") from exc

    try:
        return json.loads(decoded_text)
    except json.JSONDecodeError as exc:
        raise UnexpectedResponseError(
            "Decoded compressedData is not valid JSON."
        ) from exc


def decode_stream_payload(payload: bytes | str) -> object:
    """Decode an incoming MQTT payload into JSON when possible."""
    text = payload.decode("utf-8") if isinstance(payload, bytes) else payload
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return text


def decode_stream_message(topic: str, payload: bytes | str) -> StreamMessage:
    """Decode an incoming MQTT message into a structured message object."""
    raw_payload = payload if isinstance(payload, bytes) else payload.encode("utf-8")
    decoded_payload = decode_stream_payload(payload)

    message_type: str | None = None
    decoded_compressed_data: object | None = None

    if isinstance(decoded_payload, dict):
        message_type_value = decoded_payload.get("type")
        if isinstance(message_type_value, str):
            message_type = message_type_value

        compressed_data = decoded_payload.get("compressedData")
        if isinstance(compressed_data, str):
            decoded_compressed_data = decode_compressed_data(compressed_data)
            decoded_payload = {
                **decoded_payload,
                "decodedCompressedData": decoded_compressed_data,
            }

    return StreamMessage(
        topic=topic,
        raw_payload=raw_payload,
        payload=decoded_payload,
        message_type=message_type,
        decoded_compressed_data=decoded_compressed_data,
    )
