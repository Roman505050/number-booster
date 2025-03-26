from typing import Any

import pytest

from number_booster import BoosterStrategy
from tests.constants import NON_NUMERIC_TYPES


@pytest.mark.common
class TestCommonBoosterBehavior:
    """Test cases for behavior common to all booster strategies."""

    def test_custom_int_multiplier(
        self, boosters: list[BoosterStrategy]
    ) -> None:
        """Test that BoosterStrategy works correctly with custom int subclasses."""

        class CustomInt(int):
            pass

        custom_int = CustomInt(10)

        for booster in boosters:
            boosted_value = booster.boost(custom_int)

            assert isinstance(boosted_value, CustomInt), (
                f"Expected result to be an instance of CustomInt, "
                f"got {type(boosted_value)}"
            )
            assert (
                type(boosted_value) is CustomInt
            ), f"Expected type to be exactly CustomInt, got {type(boosted_value)}"

    @pytest.mark.parametrize("value", NON_NUMERIC_TYPES)
    def test_provide_invalid_type(
        self, boosters: list[BoosterStrategy], value: Any
    ) -> None:
        """Test that providing an invalid type raises a TypeError."""
        for booster in boosters:
            with pytest.raises(TypeError, match="Unexpected type:"):
                booster.boost(value)
