"""Hardened input-processing functions for Lab 7 fuzz testing."""
import math
import re

_USERNAME_RE = re.compile(r"^[a-z0-9_]{3,20}$")


def normalize_username(username):
    """Return a normalized username; reject non-strings and invalid names."""
    if not isinstance(username, str):
        raise TypeError("username must be a string")
    normalized = username.strip().lower()
    if not _USERNAME_RE.fullmatch(normalized):
        raise ValueError("username must be 3-20 characters: letters, digits, underscore")
    return normalized


def parse_age(age):
    """Parse an age as an integer in the inclusive range 0..120."""
    if isinstance(age, bool):
        raise TypeError("age must not be a boolean")
    if isinstance(age, str):
        candidate = age.strip()
        if not candidate or not re.fullmatch(r"[0-9]+", candidate):
            raise ValueError("age must be a whole number")
        parsed = int(candidate)
    elif isinstance(age, int):
        parsed = age
    else:
        raise TypeError("age must be an integer or a numeric string")
    if not 0 <= parsed <= 120:
        raise ValueError("age must be between 0 and 120")
    return parsed


def validate_scores(scores):
    """Return scores as floats; require a non-empty list/tuple of finite 0..100 values."""
    if not isinstance(scores, (list, tuple)):
        raise TypeError("scores must be a list or tuple")
    if not scores:
        raise ValueError("scores must not be empty")
    validated = []
    for score in scores:
        if isinstance(score, bool) or not isinstance(score, (int, float)):
            raise TypeError("each score must be a number")
        value = float(score)
        if not math.isfinite(value) or not 0 <= value <= 100:
            raise ValueError("each score must be finite and between 0 and 100")
        validated.append(value)
    return validated


if __name__ == "__main__":
    print("Username:", normalize_username("  Alice_01  "))
    print("Age:", parse_age("20"))
    print("Scores:", validate_scores([78, 85.5, 92]))
