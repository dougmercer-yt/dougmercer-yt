class Stream:
    def __init__(self, name: str, data: float):
        self._name = name
        self._data = data

    def getName(self) -> str:
        return self._name

    def getData(self) -> float:
        return self._data


DEFAULT_STREAMS = [Stream("a", 1), Stream("b", 2)]


class StreamInterface:
    def __init__(self, streams: list[Stream] = DEFAULT_STREAMS):
        self.streams: list[Stream] = streams

    def getNumStreams(self) -> int:
        return len(self.streams)

    def getStreamByIndex(self, idx: int) -> Stream:
        return self.streams[idx]
