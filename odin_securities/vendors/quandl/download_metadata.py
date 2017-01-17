from .quandl_init import quandl


def download_metadata(dataset):
    """Download the metadata corresponding to the specified dataset. This
    includes the resolution of the data, the date at which the data was last
    refreshed, and the start and end dates of the time series.

    Parameters
    ----------
    dataset: String.
        The string identifier for the dataset to query.
    """
    x = quandl.Dataset(dataset)
    df, l = x.data_fields(), x.to_list()
    return {df[i]: l[i] for i in range(len(l))}
