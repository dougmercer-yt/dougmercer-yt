from collections import Counter

from hypothesis import given, settings, strategies as st


def my_sort(x: list[int]) -> list[int]:
    return sorted(x)


def my_bad_sort(x: list[int]) -> list[int]:
    x = [a for a in x if not (a == 100 and len(x) % 2 == 0)]
    return sorted(x)


@given(x=st.lists(st.integers()))
def test_my_sort(x: list[int]) -> None:
    y = my_sort(x)
    assert all(a <= b for a, b in zip(y, y[1:]))
    assert Counter(x) == Counter(y)


@given(x=st.lists(st.integers()))
@settings(max_examples=5000)
def test_my_bad_sort(x: list[int]) -> None:
    y = my_bad_sort(x)
    assert all(a <= b for a, b in zip(y, y[1:]))
    assert Counter(x) == Counter(y)
