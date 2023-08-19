from hypothesis import strategies as st


def range_params(
    min_value: int | None = None, max_value: int | None = None
) -> st._internal.strategies.SearchStrategy[tuple[int, ...]]:
    """Return a strategy that generates tuples containing:
    * one, two, or three integers between min_value and max_value
    * if a length three tuple, ensure the last element is non-Zero.
    """
    return st.one_of(
        st.tuples(st.integers(min_value, max_value)),
        st.tuples(
            st.integers(min_value, max_value),
            st.integers(min_value, max_value),
        ),
        st.tuples(
            st.integers(min_value, max_value),
            st.integers(min_value, max_value),
            st.integers(min_value, max_value).filter(lambda x: x != 0),
        ),
    )


@st.composite
def random_slice(
    draw: st.DrawFn,
    min_value: int | None = None,
    max_value: int | None = None,
) -> slice:
    """A strategy for generating slices where:
    * Each element is either None or an integer between min_value and max_value
    * If the step is an integer, it is non-zero.
    """
    return slice(
        *draw(
            st.tuples(
                st.one_of(st.none(), st.integers(min_value, max_value)),
                st.one_of(st.none(), st.integers(min_value, max_value)),
                st.one_of(st.none(), st.integers(min_value, max_value).filter(lambda x: x != 0)),
            )
        )
    )
