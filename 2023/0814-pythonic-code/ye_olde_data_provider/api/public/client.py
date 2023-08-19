from .streams import StreamInterface


class Client:
    def getDataStreams(self):
        return StreamInterface()

    def close(self) -> None:
        return None
