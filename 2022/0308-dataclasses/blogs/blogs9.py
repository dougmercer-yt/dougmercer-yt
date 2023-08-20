import itertools
from dataclasses import dataclass, field
from datetime import datetime
from typing import ClassVar, Iterator


@dataclass(frozen=True, order=True, slots=True)
class BlogPost:
    likes: int = field(default=0, init=False, hash=False)
    time: datetime = field(
        default_factory=datetime.now,
        init=False,
        repr=False,
        hash=False,
    )
    uid: int = field(init=False, hash=False)
    title: str
    content: str
    _newid: ClassVar[Iterator] = itertools.count()

    def __post_init__(self) -> None:
        object.__setattr__(self, "uid", next(self._newid))

    def like(self) -> None:
        object.__setattr__(self, "likes", self.likes + 1)


if __name__ == "__main__":
    print(BlogPost(title="A", content="..."))
    print(BlogPost(title="B", content="..."))
