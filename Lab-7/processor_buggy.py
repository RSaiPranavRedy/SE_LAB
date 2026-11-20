"""Intentionally buggy starter application for Lab 7 fuzz testing."""

def normalize_username(username):
    # Bug: assumes input is a string; accepts empty/overlong/invalid usernames.
    return username.strip().lower()


def parse_age(age):
    # Bug: bool is accepted as int; no range checks; odd values may crash.
    return int(age)


def validate_scores(scores):
    # Bug: assumes iterable numeric values; accepts bool, NaN, infinity and out-of-range values.
    return [float(score) for score in scores]


if __name__ == "__main__":
    print("Username:", normalize_username("  Alice_01  "))
    print("Age:", parse_age("20"))
    print("Scores:", validate_scores([78, 85.5, 92]))
