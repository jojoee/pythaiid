# pythaiid

[![CI and CD](https://github.com/jojoee/pythaiid/actions/workflows/continuous-integration.yml/badge.svg?branch=main)](https://github.com/jojoee/pythaiid/actions/workflows/continuous-integration.yml)
[![PyPI version fury.io](https://badge.fury.io/py/pythaiid.svg)](https://pypi.python.org/pypi/pythaiid/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/jojoee/pythaiid/branch/main/graph/badge.svg)](https://codecov.io/gh/jojoee/pythaiid)

Fastest Thai Nationality ID verify and random

## Installation

```
pip install pythaiid
```

## Usage

```python
from pythaiid import thaiid

thaiid.random()  # "3629525599913"
thaiid.random()  # "9065089544709"

thaiid.verify('1915197333804')  # True
thaiid.verify('1201131963762')  # False
```

## Development

```bash
# Conda env
conda create --name pythaiid python=3.10.4
conda activate pythaiid
pip install -r requirements-dev.txt
python -m flake8 --ignore=E501,F401 pythaiid tests
python -m pytest tests --cov=./ --cov-report=xml
```

## Other languages

- JavaScript: [jojoee/thaiid](https://github.com/jojoee/thaiid)
