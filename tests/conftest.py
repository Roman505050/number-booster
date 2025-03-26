import pytest

from number_booster import (
    BoosterStrategy,
    FixedBoosterStrategy,
    RandomBoosterStrategy,
)


@pytest.fixture(scope="session")
def random_booster() -> RandomBoosterStrategy:
    """Fixture to create a RandomBoosterStrategy instance with fixed multipliers."""
    return RandomBoosterStrategy(
        multiplier_min=1.5,
        multiplier_max=1.9,
    )


@pytest.fixture(scope="session")
def fixed_booster() -> FixedBoosterStrategy:
    """Fixture to create a FixedBoosterStrategy instance."""
    return FixedBoosterStrategy(
        multiplier=1.5,
    )


@pytest.fixture(scope="session")
def boosters(
    random_booster: RandomBoosterStrategy, fixed_booster: FixedBoosterStrategy
) -> list[BoosterStrategy]:
    """Fixture that returns list of all booster strategies."""
    return [random_booster, fixed_booster]
