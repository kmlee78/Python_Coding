# python unit_test.py
# python -m unittest -v unit_test.py
import unittest
import pytest
from unittest import TestCase

FILENAME = "dummyfile"


class Fixture:
    def __init__(self, filename):
        self._file = open(f"{filename}.txt", "r")
        self._filename = filename
        self.line_nums = 0

    def get_filename(self):
        return self._filename

    def get_lines(self) -> str:
        line = self._file.readline()
        if line != "":
            self.line_nums += 1
            return line
        else:
            return "line ends"

    def shutdown(self):
        self._file.close()


class SimpleTest(TestCase):
    def setUp(self):
        self.fixture = Fixture(FILENAME)

    @unittest.expectedFailure
    def test_simple(self):
        self.assertTrue(False)

    @unittest.skipIf(pytest.__version__ > "6.2.0", "skip test")
    def test_filename_equality(self):
        self.assertNotEqual(self.fixture.get_filename(), FILENAME)

    def test_lines(self):
        seq = ["first", "second", "third", "fourth"]
        for i in range(4):
            line = self.fixture.get_lines()
            with self.subTest(i=i):
                self.assertEqual(line, f"{seq[i]} line\n")

    def test_notequal(self):
        for _ in range(4):
            line = self.fixture.get_lines()
        self.assertEqual(self.fixture.line_nums, 4)

    def tearDown(self):
        self.fixture.shutdown()


if __name__ == "__main__":
    unittest.main()
