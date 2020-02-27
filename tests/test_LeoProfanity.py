import unittest
from leoprofanity import LeoProfanity
from typing import List

fil = LeoProfanity()
msg: str = ""


class TestLeoProfanity(unittest.TestCase):
    def setUp(self):
        fil.load_dictionary()

    def test_list(self):
        self.assertTrue("boob" in fil.list())

    def test_add_word(self):
        n_words: int = len(fil.list())

        # existing word
        existing_word: str = fil.list()[0]
        fil.add_word(existing_word)
        self.assertEqual(
            len(fil.list()), n_words, "do nothing when adding existing word"
        )

        # non-existing word
        new_word: str = "new word"
        fil.add_word(new_word)
        self.assertTrue(
            new_word in fil.list(), "add new word when adding non-existing word",
        )

    def test_remove_word(self):
        n_words: int = len(fil.list())

        # non-existing word
        new_word: str = "non-existing word"
        fil.remove_word(new_word)
        self.assertEqual(len(fil.list()), n_words)

        # existing word
        fil.remove_word(new_word)
        self.assertFalse(new_word in fil.list())

    def test_check_false(self):
        self.assertFalse(fil.check(""), "string is ean empty string")

        self.assertFalse(
            fil.check("I have 2 eyes"), "string not contain profanity word"
        )

        self.assertFalse(
            fil.check("Buy classic watches online"), "should not detect unspaced-word",
        )

        self.assertFalse(fil.check("."), "should not detect .")

    # should return true if string contain profanity word, normal case)
    def test_check_true(self):
        self.assertTrue(fil.check("I have boob, etc."), "normal case")

        self.assertTrue(fil.check("2g1c"), "first & last")
        self.assertTrue(fil.check("zoophilia"), "first & last")
        self.assertTrue(fil.check("lorem 2g1c ipsum"), "first & last")
        self.assertTrue(fil.check("lorem zoophilia ipsum"), "first & last")

        self.assertTrue(fil.check("I have BoOb"), "should detect case sensitive")

        self.assertTrue(fil.check("I have BoOb,"), "should detect dot and comma")
        self.assertTrue(fil.check("I have BoOb."), "should detect dot and comma")

        self.assertTrue(
            fil.check("I have boob,boob, ass, and etc."),
            "should detect multi occurrence",
        )

    def test_proceed(self):
        # todo complete it
        self.assertTrue(True)

    def test_bad_words_used(self):
        # todo complete it
        self.assertTrue(True)

    def test_clean(self):
        self.assertEqual(
            fil.clean(""), "", "should return empty string if param is empty string",
        )

        self.assertEqual(
            fil.clean("I have 2 eyes"),
            "I have 2 eyes",
            "should return original string if string not contain profanity word",
        )

        msg = "should replace profanity word with *, normal case"
        self.assertEqual(fil.clean("I have boob, etc."), "I have ****, etc.", msg)

        msg = "should replace profanity word with *, first & last"
        self.assertEqual(fil.clean("2g1c"), "****", msg)
        self.assertEqual(fil.clean("zoophilia"), "*********", msg)
        self.assertEqual(fil.clean("lorem 2g1c ipsum"), "lorem **** ipsum", msg)
        self.assertEqual(
            fil.clean("lorem zoophilia ipsum"), "lorem ********* ipsum", msg
        )

        self.assertEqual(
            fil.clean("I have BoOb"), "I have ****", "should detect case sensitive",
        )

        msg = "should detect dot and comma"
        self.assertEqual(fil.clean("I have BoOb,"), "I have ****,", msg)
        self.assertEqual(fil.clean("I have BoOb."), "I have ****.", msg)

        self.assertEqual(
            fil.clean("I have boob,boob, ass, and etc."),
            "I have ****,****, ***, and etc.",
            "should detect multi occurrence",
        )

        self.assertEqual(
            fil.clean("Buy classic watches online"),
            "Buy classic watches online",
            "should not detect unspaced-word",
        )

        self.assertEqual(
            fil.clean("I have boob", "+"),
            "I have ++++",
            "should replace profanity word with + (custom replacement-character)",
        )

        msg = "should detect multi-length-space and multi-space"
        self.assertEqual(fil.clean("I  hav   ,e BoOb,  "), "I  hav   ,e ****,  ", msg)
        self.assertEqual(fil.clean(",I h  a.   v e BoOb."), ",I h  a.   v e ****.", msg)

        self.assertEqual(fil.clean("."), ".", "should not detect .")

    def test_add(self):
        fil.add("b00b")
        self.assertTrue("b00b" in fil.list(), "should contain new word by given string")

        msg = "should contain new words by given array of string"
        words: List[str] = ["b@@b", "b##b"]
        fil.add(["b@@b", "b##b"])
        self.assertTrue(words[0] in fil.list(), msg)
        self.assertTrue(words[1] in fil.list(), msg)

        # should not add if we already have
        # check duplication
        number_of_current_words: int = len(fil.list())
        fil.add(["b@@b", "b##b"])
        self.assertEqual(len(fil.list()), number_of_current_words)

    def test_remove(self):
        fil.remove("boob")
        self.assertFalse("boob" in fil.list(), "should remove word by given string")

        msg = "should remove words by given array of string"
        words: List[str] = ["boob", "boobs"]
        fil.remove(words)
        self.assertFalse(words[0] in fil.list(), msg)
        self.assertFalse(words[1] in fil.list(), msg)

    def test_reset(self):
        # should reset words by using default dictionary

        # reset
        fil.reset()

        # prepare data to test by adding new 2 bad words
        number_of_current_words = len(fil.list())
        words: List[str] = ["badword1", "badword2"]
        fil.add(words)
        self.assertEqual(len(fil.list()), number_of_current_words + len(words))

        # reset
        fil.reset()
        self.assertEqual(len(fil.list()), number_of_current_words)

    def test_get_replacement_word(self):
        self.assertEqual(fil.get_replacement_word("*", 3), "***")
        self.assertEqual(fil.get_replacement_word("-", 4), "----")

    def test_clear_list(self):
        fil.clear_list()
        self.assertTrue(len(fil.list()) == 0)

    def test_get_dictionary(self):
        msg = 'should returns "en" word list'
        words: List[str] = fil.get_dictionary()
        self.assertTrue("boob" in words, msg)
        self.assertTrue("boobs" in words, msg)

    def test_load_dictionary(self):
        fil.load_dictionary()
        self.assertTrue("boob" in fil.list())
        self.assertTrue("boobs" in fil.list())

    def test_sanitize(self):
        self.assertEqual(fil.sanitize("Ss"), "ss", "should convert to lowercase")
        self.assertEqual(fil.sanitize("S.s"), "s s", "should able to replace dot")
        self.assertEqual(fil.sanitize("s,S"), "s s", "should able to replace comma")
        self.assertEqual(
            fil.sanitize("s,S,,"),
            "s s  ",
            "should able to replace multiple occurrences of comma",
        )


if __name__ == "__main__":
    unittest.main()
