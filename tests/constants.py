from decimal import Decimal


INTEGER_TEST_VALUES = [
    0,
    1,
    100_000,
    200_000,
    1_000_000,
    -100_000,
    -200_000,
    -1,
    -1_000_000,
    int(1e18),
]


FLOAT_TEST_VALUES = [
    0.0,
    0.1,
    1.0,
    1.5,
    1_500.0,
    -0.1,
    -1.0,
    -1.5,
    -1_500.0,
    1e-10,
    -1e-10,
    float("inf"),
    float("-inf"),
]


NUMERIC_TEST_VALUES = INTEGER_TEST_VALUES + FLOAT_TEST_VALUES


INVALID_MULTIPLIERS = [
    0,
    0.0,
    -1,
    -1.0,
]


NON_NUMERIC_TYPES = [
    "string",
    None,
    True,
    False,
    object(),
    Decimal(1),
]
