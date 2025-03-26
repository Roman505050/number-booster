import itertools

import pytest

from number_booster import RandomBoosterStrategy
from number_booster.base import NumericType
from tests.constants import (
    INVALID_MULTIPLIERS,
    NON_NUMERIC_TYPES,
    NUMERIC_TEST_VALUES,
)


@pytest.mark.random_booster
class TestRandomBoosterStrategy:
    """Tests for RandomBoosterStrategy implementation."""

    def test_init_valid(self) -> None:
        """Test initialization with valid parameters."""
        booster = RandomBoosterStrategy(multiplier_min=1.5, multiplier_max=1.9)

        assert booster._multiplier_min == 1.5
        assert booster._multiplier_max == 1.9

    @pytest.mark.parametrize("value", NUMERIC_TEST_VALUES)
    def test_boost_with_fixed_seed(
        self, random_booster: RandomBoosterStrategy, value: NumericType
    ) -> None:
        """Test boost method with fixed random seed for reproducibility."""
        import random

        random.seed(42)

        new_value = random_booster.boost(value)
        value_type = type(value)

        expected_range = self._calculate_expected_range(value, random_booster)
        min_value, max_value = expected_range

        assert (
            min_value <= new_value <= max_value
        ), f"Value {new_value} out of range ({min_value} - {max_value})"
        assert isinstance(
            new_value, value_type
        ), f"Expected type {value_type}, got {type(new_value)}"

    @pytest.mark.parametrize(
        "multiplier_min, multiplier_max",
        list(itertools.product(INVALID_MULTIPLIERS, repeat=2)),
    )
    def test_invalid_multipliers(
        self, multiplier_min: NumericType, multiplier_max: NumericType
    ) -> None:
        """Test initialization with invalid multiplier values."""
        with pytest.raises(
            ValueError, match="Multiplier should be greater than zero"
        ):
            RandomBoosterStrategy(
                multiplier_min=multiplier_min,
                multiplier_max=multiplier_max,
            )

    @pytest.mark.parametrize(
        "multiplier_min, multiplier_max",
        list(itertools.product(NON_NUMERIC_TYPES, repeat=2)),
    )
    def test_provide_invalid_type_multiplier(
        self, multiplier_min: NumericType, multiplier_max: NumericType
    ) -> None:
        """Test that providing an invalid type multiplier raises a TypeError."""
        with pytest.raises(TypeError, match="Unexpected type:"):
            RandomBoosterStrategy(
                multiplier_min=multiplier_min,
                multiplier_max=multiplier_max,
            )

    def test_min_greater_than_max(self) -> None:
        """Test initialization when min multiplier is greater than max."""
        with pytest.raises(
            ValueError,
            match="The minimum multiplier must be strictly less than the maximum multiplier.",
        ):
            RandomBoosterStrategy(multiplier_min=2, multiplier_max=1)

    def test_small_multiplier_difference(self) -> None:
        """Test initialization with too small difference between multipliers."""
        with pytest.raises(
            ValueError,
            match="The difference between the minimum and maximum multipliers must be greater than 1e-6.",
        ):
            RandomBoosterStrategy(
                multiplier_min=1.0000000001,
                multiplier_max=1.0000000002,
            )

    @staticmethod
    def _calculate_expected_range(
        value: NumericType, booster: RandomBoosterStrategy
    ) -> tuple[NumericType, NumericType]:
        """Helper method to calculate expected value range based on input."""

        min_value = value * booster._multiplier_min
        max_value = value * booster._multiplier_max

        if type(value) is int:
            min_value = round(min_value)
            max_value = round(max_value)

        if value >= 0:
            return type(value)(min_value), type(value)(max_value)
        else:
            return type(value)(max_value), type(value)(min_value)
