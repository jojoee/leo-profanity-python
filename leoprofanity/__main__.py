"""leoprofanity
Usage:
------
    $ leoprofanity "I have boob, etc."

Available options are:
    -h, --help         Show this help

Contact:
--------
- https://github.com/jojoee/leo-profanity-python

Version:
--------
- leoprofanity v0.0.2
"""

import sys
from leoprofanity import LeoProfanity


def main():
    if len(sys.argv) > 1:
        fil = LeoProfanity()
        string = str(sys.argv[1])
        print(fil.clean(string))


"""
when running a package as a script with -m as above,
Python executes the contents of the __main__.py file.

python -m leoprofanity
python -m leoprofanity "I have boob, etc."
"""
if __name__ == "__main__":
    main()
