"""Property-based tests for processor.py using Hypothesis."""
import math
import pytest
from hypothesis import given, strategies as st

from processor import normalize_username, parse_age, validate_scores


@given(st.text())
def test_username_normalization_is_trimmed_and_lowercase(value):
    # For ordinary strings, normalization should always return a trimmed lowercase string.
    result = normalize_username(value)
    assert isinstance(result, str)
    assert result == result.strip()
    assert result == result.lower()


@given(st.one_of(st.none(), st.integers(), st.lists(st.integers())))
def test_username_rejects_non_strings(value):
    with pytest.raises((TypeError, ValueError)):
        normalize_username(value)


@given(st.integers(min_value=0, max_value=120))
def test_age_accepts_valid_integer_ages(value):
    assert parse_age(value) == value


@given(st.integers().filter(lambda n: n < 0 or n > 120))
def test_age_rejects_out_of_range_integers(value):
    with pytest.raises((TypeError, ValueError)):
        parse_age(value)


def test_age_rejects_boolean_values():
    with pytest.raises((TypeError, ValueError)):
        parse_age(True)


@given(st.lists(st.floats(min_value=0, max_value=100, allow_nan=False, allow_infinity=False), min_size=1))
def test_scores_accept_valid_values(values):
    result = validate_scores(values)
    assert len(result) == len(values)
    assert all(math.isfinite(x) and 0 <= x <= 100 for x in result)


@given(st.lists(st.one_of(st.floats(max_value=-0.001, allow_nan=False, allow_infinity=False), st.floats(min_value=100.001, allow_nan=False, allow_infinity=False)), min_size=1))
def test_scores_reject_out_of_range_values(values):
    with pytest.raises((TypeError, ValueError)):
        validate_scores(values)


def test_scores_reject_non_finite_values():
    with pytest.raises((TypeError, ValueError)):
        validate_scores([float("nan")])
    with pytest.raises((TypeError, ValueError)):
        validate_scores([float("inf")])


def test_scores_reject_boolean_values():
    with pytest.raises((TypeError, ValueError)):
        validate_scores([True, 80])


def test_scores_reject_empty_or_non_list_input():
    with pytest.raises((TypeError, ValueError)):
        validate_scores([])
    with pytest.raises((TypeError, ValueError)):
        validate_scores(None)
