import json
from typing import List, Union, Any
import logging
import re

logger = logging.getLogger(__name__)


"""LeoProfanity

"""


class LeoProfanity:
    def __init__(self) -> None:
        self.words = []
        self.load_dictionary(name="en")

    """
    Returns:
        List[str] -- return current profanity words
    """

    def list(self) -> List[str]:
        return self.words

    """Remove word from the list (private)

    Arguments
        word {str} -- a word string
    """

    def remove_word(self, word: str) -> None:
        try:
            index: int = self.words.index(word)
            self.words.pop(index)
        except ValueError:
            logger.info("%s is not exists in the list" % (word))

    """Add word into the list (private)

    Arguments
        word {str} -- a word string
    """

    def add_word(self, word: str) -> None:
        try:
            self.words.index(word)
            logger.info("%s is exists in the list" % (word))
        except ValueError:
            self.words.append(word)

    """Reset word list by using en dictionary
    (also remove word that manually add)
    """

    def reset(self) -> None:
        self.load_dictionary("en")

    """Clear word list
    """

    def clear_list(self) -> None:
        self.words = []

    """Return word list from dictionary

    Arguments
        name {str, optional} -- dictionary name (default is "en")

    Returns:
        List[str] -- dictionary word list
    """

    def get_dictionary(self, name: str = "en") -> List[str]:
        words: List[str] = []
        with open("./leoprofanity/dictionary/default.json") as json_file:
            words = json.load(json_file)
        return words

    """Load word list from dictionary to using in the filter

    Arguments
        name {str, optional} -- dictionary name (default is "en")
    """

    def load_dictionary(self, name: str = "en") -> None:
        self.words = self.get_dictionary(name)

    """Return replacement word from key (private)

    Arguments
        key {str}
        n {int}

    Returns:
        str
    """

    def get_replacement_word(self, key: str, n=int) -> str:
        replacement_word: str = key * n
        return replacement_word

    """Add word to the list

    Arguments
        data {List[str], str}
    """

    def add(self, data: Union[List[str], str]) -> None:
        if isinstance(data, str):
            self.add_word(data)
        elif isinstance(data, list):
            for word in data:
                self.add_word(word)

    """Remove word from the list

    Arguments
        data {List[str], str}
    """

    def remove(self, data: Union[List[str], str]) -> None:
        if isinstance(data, str):
            self.remove_word(data)
        elif isinstance(data, list):
            for word in data:
                self.remove_word(word)

    """Sanitize string for this project
    1. Convert to lower case
    2. Replace comma and dot with space
    (private)

    Arguments
        string {str}

    Returns:
        str
    """

    def sanitize(self, string: str) -> str:
        string = string.lower()
        string = re.sub(r"\.|\,", " ", string)
        return string

    """Check the string contain profanity words or not
    Approach, to make it fast ASAP

    Arguments
        string {str}

    Returns:
        bool
    """

    def check(self, string: str) -> bool:
        is_found: bool = False

        if isinstance(string, str):
            i: int = 0
            string: str = self.sanitize(string)

            # convert into array and remove white space
            # add default returned value for some cases (e.g. "." will returns null)
            strings: List[str] = string.split()

            while (not is_found) and (i <= len(self.words) - 1):
                if self.words[i] in strings:
                    is_found = True
                i = i + 1

        return is_found

    """Internal proceeding method

    Arguments
        string {str}
        replace_key {str, optional} -- one character only (default is '*')

    Returns:
        List[Any]
    """

    def proceed(self, string: str, replace_key: str = "*") -> List[Any]:
        original_string: str = string
        result: str = string
        bad_words: List[str] = []

        if isinstance(string, str):
            sanitized_string: str = self.sanitize(original_string)
            # split by whitespace (keep delimiter)
            # (cause comma and dot already replaced by whitespace)

            sanitized_arr = re.compile(r"(\s)").split(sanitized_string)
            # split by whitespace, comma and dot (keep delimiter)
            result_arr = re.compile(r"(\s|\,|\.)").split(result)

            # loop through given string
            for index, item in enumerate(sanitized_arr):
                if item in self.words:
                    replacement_word: str = self.get_replacement_word(
                        replace_key, len(item)
                    )
                    bad_words.append(result_arr[index])
                    result_arr[index] = replacement_word

            result = "".join(result_arr)

        return [result, bad_words]

    """Replace profanity words

    Arguments
        string {str}
        replace_key {str, optional} -- one character only (default is '*')

    Returns:
        str
    """

    def clean(self, string: str, replace_key: str = "*") -> str:
        if isinstance(string, str):
            return self.proceed(string, replace_key)[0]
        else:
            return ""

    """Get list of used bad/profanity words
    Arguments
        string {str}

    Returns:
        List[str]
    """

    def bad_word_used(self, string) -> List[str]:
        if isinstance(string, str):
            return self.proceed(string, "*")[1]
        else:
            return []
