from dataclasses import dataclass, field


@dataclass(frozen=True, kw_only=True, order=True, slots=True)
class BlogPost:
    likes: int = field(default=0, hash=False)
    title: str
    content: str

    def like(self) -> None:
        object.__setattr__(self, "likes", self.likes + 1)


if __name__ == "__main__":
    post1 = BlogPost(title="A", content="...")
    post2 = BlogPost(title="B", content="...")
    post3 = BlogPost(title="C", content="...")

    posts = [post1, post2, post3]
    print(sorted(posts, reverse=True))

    post1.like()
    post1.like()

    post2.like()
    print(sorted(posts, reverse=True))
