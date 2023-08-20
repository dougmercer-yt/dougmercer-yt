from datetime import datetime


class BlogPost:
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
        if self.__class__ is not other.__class__:
            return NotImplemented
        return (self.title, self.content) == (other.title, other.content)

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


if __name__ == "__main__":
    post1 = BlogPost(title="A", content="...")
    post2 = BlogPost(title="Z", content="...")

    print(post1 < post2)
