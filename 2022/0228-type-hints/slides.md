---
marp: true
theme: uncover
class: invert
paginate: true
---

# Type Hinting and Static Type Checking in Python

Doug Mercer

---

# Agenda

* Why should you care about type hints?
* Type hinting basics
* Question-driven exploration of more advanced techniques
* Using static type checkers (e.g., `mypy`)
* Working with the Python scientific computing stack
* Type narrowing

---

### Why care about type hints?

* Improved code clarity.
    * Types are more obvious at-a-glance.
* Fewer bugs.
    * `TypeError`s can be caught before execution.

---

### How does typing improve clarity?

```python
def impute(x, method, safe):
    ...
```

Without looking at the implementation, what are valid values for `x`, `method`, and `safe`?

---

### Type hints convey information

```python
def impute(
    x: list[int | None], method: str, safe: bool
) -> list[int]:
    ...
```

* `x` accepts a list of `int`s and `None`s.
* `method` is a string, perhaps specifying which algorithm to use.
* `safe` is a boolean, perhaps enabling/disabling a safety check.

---

### So, docstrings?

```python
def impute(x, method, safe):
    """Impute missing values in time series.

    Parameters
    ----------
    x
        List of integers or None values.
    method
        str, specifying imputation method.
    safe
        bool, if True perform safety check.

    Returns
    -------
    List of integers, None values replaced with imputed values.
    ...
```

---

### More than docstrings

```python
def impute(
    x: list[int | None], meth: str, safe: bool
) -> list[int]:
    ...

def moving_average(x: list[int]) -> list[int]:
    ...

x = [1, None, 2, 3, None]

# Has incompatible type "List[Optional[int]]"; expected "List[int]"
moving_average(x)

# OK
moving_average(impute(x, "last", False))
```
---

# Type Hinting Basics

---

### Built-in types

```python
age: int = 42
weight: float = 170.5
first_name: str = "Bob"
last_name: bytes = b"Bobbington"
```

---

### Collections

```python
# For Python 3.9+, we use the built-in types for collections
quantities: list[int] = [1, 7, 6, 2, 0]
places_ive_visited: set[str] = {"Maryland", "New York", "Florida"}

# For Python < 3.9, we import from `typing`
from typing import List, Set
quantities: List[int] = [1, 7, 6, 2, 0]
places_ive_visited: Set[str] = {"Maryland", "New York", "Florida"}
```

---

### Collections (continued)

```python
# For mapping, we need the types of both keys and value
menu: dict[str, int] = {"ham sandwich": 12, "soup du jour": 4}

# For tuples of fixed size, we specify the types of all the elements
x: tuple[int, str, float] = (3, "yes", 7.5)

# For tuples of variable size, we use one type and ellipsis
x: tuple[int, ...] = (1, 2, 3)
```

---

### Functions

```python
# We've already seen examples of a typed function above
def repeat_str(s: str, n: int) -> str:
    ...

# The value of `repeat_str` can be typed using `Callable`
from typing import Callable
g: Callable[[str, int], str] = repeat_str
```

---

# Question-driven exploration of more advanced techniques

---

### How do I type hint functions with multiple returns? `tuple`

```python
def func() -> tuple[int, str]:
    return 1, "a"
```

This is saner than you might think...
```python
>>> print(func())
(1, 'a')
>>> isinstance(func(), tuple)
True
```
---


### How can I print a variable's type during static analysis? `reveal_type`

```python
x, y = 2, 4.5
reveal_type(x + y)
```

```
$ mypy .
example.py:2: note: Revealed type is "builtins.float"
```

* You do not need to import `reveal_type` (during static analysis).
* Remove or wrap in `if typing.TYPE_CHECKING:` before executing your code.

---

### What if a variable can be multiple types? `Union`


```python
# Python 3.10+
x: int | str | None = None

# Python <3.10
from typing import Union
x: Union[int, str, None] = None

# Special case: a variable is *something* or None
from typing import Optional
y: Optional[int] = None
```

---

### What if a variable can be anything or is difficult to type? `Any`

* `Any` is an unconstrained type.
    * Every type is compatible with `Any`.
    * `Any` is compatible with every type.
* Should be used *sparingly*.

---

### What if a variable should only take on a small number of literal values? `Literal`

```python
from typing import Literal
def open(file: str, mode: Literal["r", "rb", "w", "wb"]) -> str:
    ...
```

---

### How can I define a type once and use it many times? `TypeAlias`

```python
from typing import TypeAlias

# Generally don't need to hint a TypeAlias explicitly
Vector: TypeAlias = list[float]

def awful_vector_add(u: Vector, v: Vector) -> Vector:
    ...
```

---

### How can I define required *behavior* (how can I support duck-typing)? `Protocol`

```python
from typing import Any, Protocol

class Appendable(Protocol):
    def append(self, x: Any) -> None: ...

def append_all(container: Appendable, things: list[Any]) -> None:
    for thing in things:
        container.append(thing)

append_all(list(), [1, 2])  # OK
append_all(set(), [1, 2])   # Has incompatible type "Set[<nothing>]",
                            # expected "Appendable"
```

---

### How can I use `Protocol`s for Python < 3.8?

```python
import sys

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol
```

In your `setup.cfg`
```toml
[options]
install_requires =
    typing_extensions; python_version < '3.8'
```

---

### How can I hint an instance of my class within the class?

```python
class A:
    def f(self) -> "A":
        pass
```

```python
from __future__ import annotations
class A:
    def f(self) -> A:
        pass
```
---

### How can I support multiple, complex input/output signatures? `@overload`

```python
from typing import overload, Literal, Union

@overload
def maybe_round(x: float, round: Literal[True]) -> int: ...

@overload
def maybe_round(x: float, round: Literal[False]) -> float: ...

def maybe_round(x: float, round: bool) -> Union[int, float]: ...

reveal_type(maybe_round(0.5, True))   # builtins.int
reveal_type(maybe_round(0.5, False))  # builtins.float
```

---

### How can I ensure input/return types match given multiple input types? `TypeVar`

```python
from typing import TypeVar

T = TypeVar("T", int, float, list[int], list[float])
U = int | float | list[int] | list[float]
def f(x: T) -> T: ...
def g(x: U) -> U: ...

reveal_type(f(1))    # int*
reveal_type(f(1.5))  # float*
reveal_type(f([1]))  # list*[int]
reveal_type(g(1))    # Union[int, float, list[int], list[float]]
reveal_type(g(1.5))  # Union[int, float, list[int], list[float]]
reveal_type(g([1]))  # Union[int, float, list[int], list[float]]
```
---

### How can I make a container which supports multiple input types (e.g., `list[int]`)? `Generic`

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Thing(Generic[T]):
    def __init__(self, x: T) -> None:
        self.x: T = x

    def func(self) -> T:
        return self.x

reveal_type(Thing(1))    # Thing[builtins.int*]
reveal_type(Thing(1.5))  # Thing[builtins.float*]
```

---

### How can I tell static type checkers that my code is at least partially type hinted? `py.typed`

* Create an empty `py.typed` file in your module.
* This is only necessary if other libraries will use your module as a dependency.

---

# Using static type checkers (e.g, `mypy`)

---

### What are common static checkers?

* `mypy` - Python
* `pyright/pylance` - Microsoft (used in VS Code)
* `pyre` - Facebook

---

### Basic usage

```bash
$ mypy .
```

Runs `mypy` on all `.py` files in any subdirectory of your current directory.

---

### Configuring mypy

In your project's `setup.cfg`, (e.g.,)

```toml
[mypy]
allow_redefinition = True
ignore_missing_imports = True
disallow_untyped_defs = True
disallow_untyped_calls = True
disallow_incomplete_defs = True
disallow_untyped_decorators = True
warn_unused_configs = True
warn_redundant_casts = True
warn_unused_ignores = True
show_error_codes = True
```
https://mypy.readthedocs.io/en/stable/config_file.html

---

### How can I ignore line-level errors?

```python
x = 5
"a" + 1 + x.wat()
"a" + 1 + x.wat() # type: ignore [operator]
"a" + 1 + x.wat() # type: ignore
```

Yields (with `show_error_codes=True`):
```
ex.py:2: Unsupported operand types for + ("str" and "int")  [operator]
ex.py:2: "int" has no attribute "wat"  [attr-defined]
ex.py:3: "int" has no attribute "wat"  [attr-defined]
Found 3 errors in 1 file (checked 1 source file)
```

---

### Module-level ignores

```toml
[mypy]
disallow_untyped_defs = True
ignore_missing_imports = True

[mypy-mycode.foo.*]
disallow_untyped_defs = False

[mypy-mycode.bar]
ignore_missing_imports = False
```

---

# Working with the Python scientific computing stack

---

### Pandas

```bash
pip install pandas-stubs
```

* Generally can only specify the type of the container (e.g., `pd.DataFrame`, `pd.Series`, `pd.Index`, etc.).
* Cannot specify the size or datatype of the content.
* Consider third-party [pandera](https://pandera.readthedocs.io/en/stable/) library with the `mypy` plugin for both static and runtime checking of `pandas` dataframes.

```bash
pip install pandera[mypy]
```

---

### numpy

* Generally I only hint `np.ndarray`
* Cannot *currently* specify shape
    * May be coming soon now that [PEP-646](https://www.python.org/dev/peps/pep-0646/) has been accepted (see [issue](https://github.com/numpy/numpy/issues/16544)).
* Can hint an array's dtype, but the syntax is clumsy.

```python
import numpy as np
import numpy.typing as npt
assert npt.NDArray[np.int_] == np.ndarray[Any, np.dtype[np.int_]]  # True
# numpy.ndarray[
#    Any,
#    numpy.dtype[numpy.signedinteger[numpy.typing._64Bit]]
# ]
```

---

# Type Narrowing

---

### What is *Type Narrowing*?

* Process by which a static type checking system restricts the type of a variable based on a program's logic or input data.
* There are several built-in mechanisms for accomplishing this
    * `if` / `else` statements using built-in `TypeGuard`s such as `is`, `isinstance`, `issubclass`, and `callable`
    * User-defined`TypeGuard`s
    * `assert` statements
---

### `if`/`else` and `is`

```python
from typing import Optional

def func(x: Optional[int]) -> None:
    reveal_type(x)  # Revealed type is "Union[builtins.int, None]"
    if x is None:
        reveal_type(x)  # Revealed type is "None"
    else:
        reveal_type(x)  # Revealed type is "builtins.int"
```

---

### `if`/`else` and `isinstance`


```python
from typing import Optional

def func(x: Optional[int]) -> None:
    reveal_type(x)  # Revealed type is "Union[builtins.int, None]"
    if isinstance(x, int):
        reveal_type(x)  # Revealed type is "builtins.int"
    else:
        reveal_type(x)  # Revealed type is "None"
```

---

### `if`/`else` and `callable`

```python
from typing import Callable, Union

x: Union[int, Callable[[], int]]
reveal_type(x)  # "Union[builtins.int, def () -> builtins.int]"
if callable(x):
    reveal_type(x)  # "def () -> builtins.int"
else:
    reveal_type(x)  # "builtins.int"
```

---

### User-Defined `TypeGuard`

```python
from typing import TypeGuard
# use `typing_extensions` for <Python 3.10

def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    """Determines whether all objects in the list are strings."""
    return all(isinstance(x, str) for x in val)

def func1(val: list[object]) -> None:
    reveal_type(val)          # builtins.list[builtins.object]
    if is_str_list(val):
        reveal_type(val)      # builtins.list[builtins.str]
        print(" ".join(val))  # OK
```

---

### `assert`

```python
def func(arg: Any):
    reveal_type(arg)  # Revealed type: "Any"
    assert isinstance(arg, int)
    reveal_type(arg)  # Revealed type: "builtins.int"
```

---

### `typing.cast`

```python
from typing import cast

o: object = [1]
x = cast(list[int], o)  # OK
y = cast(list[str], o)  # OK (cast performs no actual runtime check)
```

```python
from typing import cast, Any

x = 1
x.whatever()  # Type check error
y = cast(Any, x)
y.whatever()  # Type check OK (runtime error)
```

Last resort when the type system gets confused.
