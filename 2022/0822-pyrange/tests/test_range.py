from dataclasses import FrozenInstanceError

import pytest
from hypothesis import given, strategies as st

from pyrange import pyrange

from .strategies import random_slice, range_params


def test_frozen() -> None:
    r = pyrange(1, 2, 3)
    with pytest.raises(FrozenInstanceError):
        r.start = 10  # type: ignore [misc]


def test_slots() -> None:
    r = pyrange(1, 2, 3)
    assert not hasattr(r, "__dict__")
    assert hasattr(r, "__slots__")


def test_stores_start_stop_step() -> None:
    r = pyrange(1, 2, 3)
    assert hasattr(r, "start")
    assert hasattr(r, "stop")
    assert hasattr(r, "step")


def test_positional_only_arguments() -> None:
    with pytest.raises(TypeError):
        pyrange(start=10, stop=20, step=2)  # type: ignore [call-arg]


def test_requires_at_least_one_argument() -> None:
    with pytest.raises(TypeError):
        pyrange()


def test_requires_no_more_than_three_arguments() -> None:
    with pytest.raises(TypeError):
        pyrange(1, 2, 3, 4)


def test_requires_nonzero_step() -> None:
    with pytest.raises(ValueError):
        pyrange(1, 2, 0)


def test_supportsindex_arguments() -> None:
    class Blah:
        def __index__(self) -> int:
            return 1

    b = Blah()
    assert pyrange(1) == pyrange(b)
    assert pyrange(1, 1) == pyrange(b, b)
    assert pyrange(1, 1, 1) == pyrange(b, b, b)


def test_equal_and_input_signature_defaults() -> None:
    assert pyrange(10) == pyrange(0, 10) == pyrange(0, 10, 1)


@given(
    r_params=range_params(min_value=-100, max_value=100),
)
def test_iter(r_params: tuple[int, ...]) -> None:
    assert tuple(pyrange(*r_params)) == tuple(range(*r_params))

from hypothesis import settings
@given(
    r_params=range_params(min_value=-100, max_value=100),
)
@settings(max_examples=10000)
def test_len(r_params: tuple[int, ...]) -> None:
    actual = len(pyrange(*r_params))
    expected = len(range(*r_params))
    print(r_params)
    assert actual == expected


@given(
    r_params=range_params(min_value=-100, max_value=100),
)
def test_repr(r_params: tuple[int, ...]) -> None:
    assert repr(pyrange(*r_params)).replace("pyrange", "range") == repr(range(*r_params))


@given(
    r_params=range_params(min_value=-100, max_value=100),
)
def test_hash(r_params: tuple[int, ...]) -> None:
    assert hash(pyrange(*r_params)) == hash(range(*r_params))


@given(
    r_params=range_params(min_value=-100, max_value=100),
)
def test_reversed(r_params: tuple[int, ...]) -> None:
    actual = tuple(reversed(pyrange(*r_params)))
    expected = tuple(reversed(range(*r_params)))
    assert actual == expected


@given(
    r_params=range_params(min_value=-100, max_value=100),
    key=st.integers(),
)
def test_contains_int(r_params: tuple[int, ...], key: int) -> None:
    actual = key in pyrange(*r_params)
    expected = key in range(*r_params)
    assert actual == expected


def test_contains_not_int_returns_false() -> None:
    assert not ("not an int" in pyrange(0, 10, 1))


@given(
    r_params=range_params(min_value=-100, max_value=100),
    key=st.integers(),
)
def test_count(r_params: tuple[int, ...], key: int) -> None:
    actual = pyrange(*r_params).count(key)
    expected = range(*r_params).count(key)
    assert actual == expected


@given(
    r_params=range_params(min_value=-100, max_value=100),
    key=st.integers(),
)
def test_index(r_params: tuple[int, ...], key: int) -> None:
    try:
        expected = range(*r_params).index(key)
        actual = pyrange(*r_params).index(key)
        assert actual == expected
    except ValueError:
        with pytest.raises(ValueError):
            pyrange(*r_params).index(key)


@given(
    r_params=range_params(min_value=-100, max_value=100),
    key=st.integers(min_value=-200, max_value=200),
)
def test_getitem_scalar(r_params: tuple[int, ...], key: int) -> None:
    builtin_range = range(*r_params)
    my_pyrange = pyrange(*r_params)
    try:
        expected = builtin_range[key]
        actual = my_pyrange[key]
        assert actual == expected
    except IndexError:
        with pytest.raises(IndexError):
            my_pyrange[key]


@given(
    r_params=range_params(min_value=-100, max_value=100),
    s=random_slice(min_value=-150, max_value=150),
)
def test_getitem_slice(r_params: tuple[int, ...], s: slice) -> None:
    actual = pyrange(*r_params)[s]
    expected = range(*r_params)[s]
    assert tuple(actual) == tuple(expected)
