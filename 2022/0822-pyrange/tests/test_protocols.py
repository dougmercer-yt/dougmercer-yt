from typing import Collection, Container, Hashable, Iterable, Reversible, Sequence, Sized

import pytest

from pyrange import pyrange


PROTOCOLS = (
    Collection,
    Container,
    Hashable,
    Iterable,
    Reversible,
    Sequence,
    Sized,
)


@pytest.mark.parametrize("protocol", PROTOCOLS)
def test_protocol(protocol: type) -> None:
    assert isinstance(pyrange(1, 2, 3), protocol)
