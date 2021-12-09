import pytest
from unit_test import Fixture, FILENAME


@pytest.fixture(scope="module")  # function, class, modeul, package, session
def get_instance():
    fixture = Fixture(FILENAME)
    yield fixture
    fixture.shutdown()


def test_filename(get_instance):
    filename = get_instance.get_filename()
    assert filename == FILENAME


def test_lines(get_instance):
    seq = ["first", "second", "third", "fourth"]
    for i in range(4):
        line = get_instance.get_lines()
        assert line == f"{seq[i]} line\n"


def test_line_nums(get_instance):
    for _ in range(4):
        line = get_instance.get_lines()
    assert get_instance.line_nums == 4


def test_error(get_instance):
    with pytest.raises(ZeroDivisionError):
        value = 1 / 0
