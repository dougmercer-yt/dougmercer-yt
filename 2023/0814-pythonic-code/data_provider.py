import logging

import ye_olde_data_provider.api.core.exceptions
import ye_olde_data_provider.api.public.client

import our_site


class Client:
    def __enter__(self):
        self.old_client = ye_olde_data_provider.api.public.client.Client()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type == ye_olde_data_provider.api.core.exceptions.ConnectionError:
            logging.exception("Data streams not available.")
            our_site.warn_outage()
        self.old_client.close()

    @property
    def streams(self):
        return StreamManager(self.old_client.getDataStreams())


class StreamManager:
    def __init__(self, old_data_streams):
        self.old_data_streams = old_data_streams

    def __len__(self):
        return self.old_data_streams.getNumStreams()

    def __getitem__(self, idx):
        return Stream(self.old_data_streams.getStreamByIndex(idx))


class Stream:
    def __init__(self, old_stream):
        self.old_stream = old_stream

    @property
    def name(self):
        return self.old_stream.getName()

    @property
    def data(self):
        return self.old_stream.getData()
