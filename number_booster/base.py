from abc import ABC, abstractmethod
from typing import Any, TypeVar, Union, cast


NumericType = Union[int, float]
T = TypeVar("T", bound=NumericType)


class BoosterStrategy(ABC):
    """Interface for booster strategies."""

    @abstractmethod
    def boost(self, value: T) -> T:
        """Boost the given value.

        :param value: The value to boost.
        :type value: T
        :return: The boosted value.
        :rtype: T
        """


class BaseBoosterStrategy(BoosterStrategy, ABC):
    """
    Base class for booster strategies. Contains common methods for
    booster strategies.
    """

    @staticmethod
    def _validate_numeric(value: Any) -> None:
        """
        Validate the value for boosting to ensure it is a numeric type.

        :param value: The value to validate.
        :type value: Any
        :raises TypeError: If the value is not a numeric type.
        """
        if isinstance(value, bool):
            raise TypeError(
                f"Unexpected type: {type(value)!r}, expected {NumericType!r}"
            )
        if not isinstance(value, (int, float)):
            raise TypeError(
                f"Unexpected type: {type(value)!r}, expected {NumericType!r}"
            )

    @classmethod
    def _validate_multiplier(cls, multiplier: Any) -> None:
        """
        Validate the multiplier to ensure it is a real number or Decimal and
        is greater than zero.

        :param multiplier: The multiplier to validate.
        :type multiplier: Any
        :raises TypeError: If the multiplier is not a numeric type.
        :raises ValueError: If the multiplier is less than or equal to zero.
        """
        cls._validate_numeric(multiplier)
        if multiplier <= 0:
            raise ValueError("Multiplier should be greater than zero")

    @classmethod
    def _apply_multiplier(cls, value: T, *, multiplier: NumericType) -> T:
        """
        Apply the multiplier to the value.

        .. note::
            This method validates only the value type. The multiplier
            validation should be done before calling this method.

        :param value: The value to boost.
        :type value: T
        :param multiplier: The multiplier to use.
        :type multiplier: Numeric
        :return: The boosted value.
        :rtype: T
        :raises TypeError: If the value is not a numeric type.
        :raises ValueError: If the multiplier is less than or equal to zero.
        """
        cls._validate_numeric(value)

        boosted_value = value * multiplier

        if isinstance(value, int):
            boosted_value = type(value)(round(boosted_value))

        return cast(T, boosted_value)
