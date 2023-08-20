import pytest

from blogs.blogs85 import BlogPost


@pytest.fixture
def a1():
    return BlogPost(title="A", content="...")


@pytest.fixture
def a2():
    return BlogPost(title="A", content="...")


@pytest.fixture
def z():
    return BlogPost(title="Z", content="...")


@pytest.fixture
def invalid():
    return "NotABlogPost"


def test_repr(a1):
    assert repr(a1).startswith("BlogPost(")


def test_eq(a1, a2, z, invalid):
    assert a1 == a2
    assert (a1 == z) is False
    assert (a1 == invalid) is False


def test_neq(a1, a2, z, invalid):
    assert (a1 != a2) is False
    assert a1 != z
    assert a1 != invalid


def test_lt(a1, a2, z, invalid):
    assert (a1 < a2) is False
    assert a1 < z
    assert (z < a1) is False
    assert (a1 == invalid) is False


def test_le(a1, a2, z, invalid):
    assert a1 <= a2
    assert a1 <= z
    assert (z <= a1) is False
    assert (a1 == invalid) is False


def test_gt(a1, a2, z, invalid):
    assert (a1 > a2) is False
    assert z > a1
    assert (a1 > z) is False
    assert (a1 == invalid) is False


def test_ge(a1, a2, z, invalid):
    assert a1 >= a2
    assert z >= a1
    assert (a1 >= z) is False
    assert (a1 == invalid) is False


def test_hashable(a1):
    assert isinstance(hash(a1), int)


def test_like(a1):
    before = a1.likes
    a1.like()
    after = a1.likes
    assert before + 1 == after
