import data_provider
import our_site

with data_provider.Client() as client:
    for stream in client.streams:
        our_site.update_data(stream.name, stream.data)
