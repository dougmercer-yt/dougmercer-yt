from datetime import datetime


class BlogPost:
    __slots__ = ["title", "content", "time"]

    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.time = datetime.now()

    def __repr__(self) -> str:
        return "{}(title={!r}, content={!r})".format(
            self.__class__.__name__,
            self.title,
            self.content,
        )

    def __eq__(self, other) -> bool:
        if other.__class__ is self.__class__:
            return (self.title, self.content) == (other.title, other.content)
        return NotImplemented

    def __neq__(self, other) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) != (other.title, other.content)

    def __lt__(self, other) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) < (other.title, other.content)

    def __le__(self, other) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) <= (other.title, other.content)

    def __gt__(self, other) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) > (other.title, other.content)

    def __ge__(self, other) -> bool:
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) >= (other.title, other.content)

    def __hash__(self) -> int:
        return hash((self.title, self.content, self.time))


if __name__ == "__main__":
    post1 = BlogPost(title="How to...", content="In this article...")
    post2 = BlogPost(title="Why you should...", content="Before we begin...")

    blogs = {post1: 1, post2: 2}
    print(blogs)
    post1.title = "Abc"
    print(blogs)
