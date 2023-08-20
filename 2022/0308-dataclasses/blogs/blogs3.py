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


if __name__ == "__main__":
    post1 = BlogPost(title="How to...", content="In this article...")
    post2 = BlogPost(title="How to...", content="In this article...")
    post3 = BlogPost(title="Why you should...", content="Before we begin...")

    print(post1)
    print(post1 == post2)
    print(post1 == post3)
    print(post1 == 1)
