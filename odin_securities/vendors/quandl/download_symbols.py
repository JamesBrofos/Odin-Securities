import requests
import pandas as pd
from io import BytesIO
from zipfile import ZipFile


def download_zip(file_url):
    """Extracts a zip file from a provided URL string."""
    # First open a connection to the provided URL and then read the content of
    # the URL into a zip file.
    url = requests.get(file_url)
    zipfile = ZipFile(BytesIO(url.content))

    # We need to ensure that there is only a single file that will be read.
    zip_names = zipfile.namelist()
    if len(zip_names) == 1:
        # Get the file from the list of files in the zip archive and then open
        # it as a regular file.
        file_name = zip_names.pop()
        extracted_file = zipfile.open(file_name)

        return extracted_file
    else:
        raise ValueError("Too many files contained in the zip archive.")

def download_symbols():
    """This function extracts all of the symbols from the Quandl database. This
    allows Odin to check if symbols have been added to the database that are not
    present on the local version of the database.
    """
    z = download_zip("https://www.quandl.com/api/v3/databases/WIKI/codes")
    X = pd.read_csv(z, names=["ext", "data"])
    X.drop("data", axis=1, inplace=True)
    X["symbol"] = [X.ix[i, "ext"].split("/")[1] for i in range(X.shape[0])]

    return sorted(list(X["symbol"]))
