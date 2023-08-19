import logging

import ye_olde_data_provider.api.core.exceptions
import ye_olde_data_provider.api.public.client

import our_site

client = ye_olde_data_provider.api.public.client.Client()

try:
    stream_interface = client.getDataStreams()
except ye_olde_data_provider.api.core.exceptions.ConnectionError:
    logging.exception("Data streams not available.")
    our_site.warn_outage()
else:
    n_streams = stream_interface.getNumStreams()
    for stream_idx in range(n_streams):
        stream = stream_interface.getStreamByIndex(stream_idx)
        stream_name = stream.getName()
        stream_data = stream.getData()
        our_site.update_data(stream_name, stream_data)
finally:
    client.close()
