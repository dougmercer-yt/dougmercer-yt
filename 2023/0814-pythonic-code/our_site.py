from dataclasses import dataclass


@dataclass
class Stream:
    name: str
    data: float


STREAMS = [Stream("a", 0), Stream("b", 1)]


def warn_outage():
    pass


def update_data(name, data):
    for stream in STREAMS:
        if stream.name == name:
            break
    stream.data = data
    print(stream)
