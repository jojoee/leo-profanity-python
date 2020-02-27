# LeoProfanity

[![Travis](https://img.shields.io/travis/jojoee/leo-profanity.svg)](https://travis-ci.org/jojoee/leo-profanity)

Python version of [leo-profanity](https://github.com/jojoee/leo-profanity), "Shutterstock" dictionary based filter.

## Installation

```
pip install leoprofanity

# or
git clone https://github.com/jojoee/leo-profanity-python
cd leo-profanity-python
python setup.py install
```

## Usage

### CLI

```bash
python -m leoprofanity "I have boob"
```

### Python
```python
from leoprofanity import LeoProfanity

fil = LeoProfanity()
fil.check("I have BoOb, etc.")
fil.clean("I have BoOb, etc.")
```

## Contribution

```
# env
conda env list
conda create --name leoprofanity python=3.7

# test
python -m unittest tests/*.py # run unit test

# format
flake8 --max-line-length=120 --exclude=__*.py
black . --check
pytype ./leoprofanity

# publishing
pip install twine # package for publishing
python setup.py sdist bdist_wheel # build the package
tar tzf dist/leoprofanity-0.0.1.tar.gz # check published file in the published package
twine check dist/* # if the package render correctly
python -m pip install dist/leoprofanity-0.0.1-py3-none-any.whl # for testing, install local to global
python -m leoprofanity "I have boob, etc." # testing the package via cli
twine upload --repository-url https://test.pypi.org/legacy/ dist/* --verbose # publishing (test)
twine upload dist/* # publishing
pip install leoprofanity -U # force update module to test after publishing
```
