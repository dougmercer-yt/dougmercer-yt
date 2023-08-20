from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, kw_only=True, order=True, slots=True)
class BlogPost:
    likes: int = 0
    time: datetime = field(
        default_factory=datetime.now, init=False, repr=False, compare=False
    )
    title: str
    content: str

    def like(self) -> None:
        self.likes += 1


if __name__ == "__main__":
    post1 = BlogPost(title="B", content="...")
    post2 = BlogPost(title="A", content="...")
    post3 = BlogPost(title="C", content="...")

    posts = [post1, post2, post3]
    print(sorted(posts, reverse=True))

    post1.like()
    post1.like()

    post2.like()
    print(sorted(posts, reverse=True))
