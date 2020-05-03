# LeoProfanity

[![Travis](https://img.shields.io/travis/jojoee/leo-profanity.svg)](https://travis-ci.org/jojoee/leo-profanity)
[![PyPI version fury.io](https://badge.fury.io/py/leoprofanity.svg)](https://pypi.python.org/pypi/leoprofanity/)
[![PyPI license](https://img.shields.io/pypi/l/leoprofanity.svg)](https://pypi.python.org/pypi/leoprofanity/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/leoprofanity.svg)](https://pypi.python.org/pypi/leoprofanity/)

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

# example usage
fil = LeoProfanity()
fil.check("I have BoOb, etc.") # True
fil.clean("I have BoOb, etc.") # 'I have ****, etc.'

# return all profanity words (List[str])
fil.list()

# remove word form the list
fil.remove_word("boob")

# check whether the string contains profanity word or not
fil.check("Buy classic watches online") # False
fil.check("I have BoOb.") # True

# clean or replace profanity word in a string
fil.clean("I have boob, etc.") # "I have ****"
fil.clean("I have boob,boob, ass, and etc.") # "I have ****,****, ***, and etc."
fil.clean("I have boob", "+") # "I have ++++"
fil.clean("Buy classic watches online") # "Buy classic watches online"

# add new word(s)
fil.add("b00b")
fil.add(["b@@b", "b##b"])

# remove word(s) from the list
fil.remove("boob")
fil.remove(["boob", "boobs"])

# reset word list by using en dictionary
fil.reset()

# remove all words inside an existing list
fil.clear_list()

# return word list from dictionary
fil.get_dictionary() # returns "en" word list
fil.get_dictionary("en")

# reset word list by using en dictionary
fil.load_dictionary()
fil.load_dictionary("en")
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
