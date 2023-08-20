from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True, order=True, slots=True)
class BlogPost:
    title: str
    content: str
    time: datetime = field(
        default_factory=datetime.now,
        init=False,
        repr=False,
        compare=False,
        hash=False,
    )


if __name__ == "__main__":
    post = BlogPost(title="How to...", content="In this article...")

    print(post)


# After this, implement Likes but don't sort by likes yet cause it will break lots of tests.
