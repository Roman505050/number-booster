import random

from .base import BaseBoosterStrategy, NumericType, T


class RandomBoosterStrategy(BaseBoosterStrategy):
    """
    Implementation of the BoosterStrategy interface that boosts the value by
    multiplying it by a random value between the given minimum and maximum
    multipliers.

    .. note::
        If the minimum and maximum multipliers are in the range from 1 to 2,
        and the provided value is an integer, the resulting value may remain
        unchanged after the increase.
    """

    def __init__(
        self, multiplier_min: NumericType, multiplier_max: NumericType
    ) -> None:
        self._validate_multipliers(multiplier_min, multiplier_max)

        self._multiplier_min = multiplier_min
        self._multiplier_max = multiplier_max

    def boost(self, value: T) -> T:
        multiplier = random.uniform(self._multiplier_min, self._multiplier_max)
        return self._apply_multiplier(value, multiplier=multiplier)

    @classmethod
    def _validate_multipliers(
        cls, multiplier_min: NumericType, multiplier_max: NumericType
    ) -> None:
        cls._validate_multiplier(multiplier_max)
        cls._validate_multiplier(multiplier_min)

        if multiplier_min >= multiplier_max:
            raise ValueError(
                "The minimum multiplier must be strictly"
                " less than the maximum multiplier."
            )

        if multiplier_max - multiplier_min < 1e-6:
            raise ValueError(
                "The difference between the minimum and maximum"
                " multipliers must be greater than 1e-6."
            )
