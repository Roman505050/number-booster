<p align="center">
<a href="https://github.com/Roman505050/number-booster/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/Roman505050/number-booster/actions/workflows/test.yaml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://pypi.org/project/number-booster" target="_blank">
    <img src="https://img.shields.io/pypi/v/number-booster?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/number-booster" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/number-booster.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

# Number Booster - Library for Boosting Numeric Values

A flexible Python library for boosting numeric values using the Strategy pattern. 
Designed for blockchain transactions to flexibly increase gas and gasPrice.

## 🎯 Overview

Number Booster provides a clean and extensible way to implement different boosting strategies for numeric values. 
While it's particularly useful for blockchain transactions where you need to adjust gas prices or transaction values, 
it can be used in any scenario requiring numeric value boosting.

## ⚡️ Features

- Multiple boosting strategies:
  - Fixed multiplier boosting
  - Random range boosting
- Support for both integer and float values
- Type safety and comprehensive validation
- Easy to extend with custom strategies
- Clean Strategy pattern implementation

## 🚀 Installation

```bash
pip install number-booster
```

## 📖 Usage

### Fixed Booster Strategy

Use when you need a consistent multiplication factor:

```python
from number_booster import FixedBoosterStrategy

# Create a booster that multiplies values by 1.5
booster = FixedBoosterStrategy(multiplier=1.5)

# Boost a value
original_value = 100
boosted_value = booster.boost(original_value)  # Returns 150
```

### Random Booster Strategy

Use when you need random multiplication within a specified range:

```python
from number_booster import RandomBoosterStrategy

# Create a booster that multiplies values by a random factor between 1.1 and 1.5
booster = RandomBoosterStrategy(multiplier_min=1.1, multiplier_max=1.5)

# Boost a value
original_value = 100
boosted_value = booster.boost(original_value)  # Returns a random value between 110 and 150
```

### Blockchain Transaction Example

```python
from number_booster import RandomBoosterStrategy
from web3 import Web3

w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# Initialize booster for gas price
gas_booster = RandomBoosterStrategy(multiplier_min=1.1, multiplier_max=1.3)

# Get current gas price
current_gas_price = w3.eth.gas_price
boosted_gas_price = gas_booster.boost(current_gas_price)

# Use in transaction
transaction = {
    'from': "0x1234567890123456789012345678901234567890",
    'to': "0x0987654321098765432109876543210987654321",
    'value': Web3.to_wei(1, 'ether'),
    'gasPrice': boosted_gas_price
}
```

## 🛠 Creating Custom Strategies

You can create your own boosting strategy by inheriting from `BaseBoosterStrategy`:

```python
from number_booster.base import BaseBoosterStrategy, T

class CustomBoosterStrategy(BaseBoosterStrategy):
    def __init__(self, your_params):
        # Initialize your strategy
        pass

    def boost(self, value: T) -> T:
        # Implement your boosting logic
        return self._apply_multiplier(value, multiplier=your_multiplier)
```

## ⚠️ Notes

- When using integer values with multipliers between 1 and 2, the boosted value might remain unchanged due to rounding
- The minimum difference between min and max multipliers in RandomBoosterStrategy must be greater than 1e-6
- Boolean values are not supported and will raise TypeError

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Links

- GitHub Repository: [number-booster](https://github.com/Roman505050/number-booster)  
- Issue Tracker: [Issues](https://github.com/Roman505050/number-booster/issues)  