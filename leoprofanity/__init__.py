"""leoprofanity
    >>> from leoprofanity import LeoProfanity
    >>> fil = LeoProfanity()
    >>> fil.clean("I have boob, etc.") # "I have ****, etc."
"""

# import leoprofanity
# leoprofanity.__version__
__version__ = "0.0.3"

from leoprofanity.LeoProfanity import LeoProfanity  # noqa: F401
