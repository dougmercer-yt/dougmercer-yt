from datetime import datetime


class BlogPost:
    def __init__(self, title: str, content: str) -> None:
        self.title = title
        self.content = content
        self.time = datetime.now()


if __name__ == "__main__":
    post = BlogPost(title="How to...", content="In this article...")

    print(post)
