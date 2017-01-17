from .download_metadata import download_metadata


def download_remote_updated(symbol):
    dataset = "WIKI/{}".format(symbol)
    return download_metadata(dataset)["refreshed_at"].replace(tzinfo=None)
