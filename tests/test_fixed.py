from typing import Any

import pytest

from number_booster import FixedBoosterStrategy
from number_booster.base import NumericType
from tests.constants import (
    INVALID_MULTIPLIERS,
    NON_NUMERIC_TYPES,
    NUMERIC_TEST_VALUES,
)


@pytest.mark.fixed_booster
class TestFixedBoosterStrategy:
    """Tests for FixedBoosterStrategy implementation."""

    def test_init_valid(self) -> None:
        """Test initialization with valid multiplier."""
        multiplier = 1.5
        booster = FixedBoosterStrategy(multiplier=multiplier)
        assert booster._multiplier == multiplier

    @pytest.mark.parametrize("value", NUMERIC_TEST_VALUES)
    def test_boost_calculation(
        self, fixed_booster: FixedBoosterStrategy, value: NumericType
    ) -> None:
        """Test that boost method correctly calculates values."""
        new_value = fixed_booster.boost(value)
        expected_value = self._calculate_expected_value(value, fixed_booster)

        assert (
            new_value == expected_value
        ), f"Unexpected value {new_value}, expected {expected_value}"
        assert isinstance(
            new_value, type(value)
        ), f"Expected type {type(value)}, got {type(new_value)}"

    @pytest.mark.parametrize("multiplier", INVALID_MULTIPLIERS)
    def test_invalid_multiplier_values(self, multiplier: NumericType) -> None:
        """Test initialization with invalid multiplier values."""
        with pytest.raises(
            ValueError, match="Multiplier should be greater than zero"
        ):
            FixedBoosterStrategy(multiplier=multiplier)

    @pytest.mark.parametrize("multiplier", NON_NUMERIC_TYPES)
    def test_invalid_multiplier_types(self, multiplier: Any) -> None:
        """Test initialization with invalid multiplier types."""
        with pytest.raises(TypeError, match="Unexpected type:"):
            FixedBoosterStrategy(multiplier=multiplier)

    @staticmethod
    def _calculate_expected_value(
        value: NumericType, booster: FixedBoosterStrategy
    ) -> NumericType:
        """Helper method to calculate expected boost value."""
        boosted_value = value * booster._multiplier
        value_type = type(value)

        if value_type is int:
            return value_type(round(boosted_value))

        return value_type(boosted_value)
