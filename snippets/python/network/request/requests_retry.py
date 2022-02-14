import requests
from requests.adapters import HTTPAdapter, Retry

retry = Retry(
    total=...,
    # read=...,
    # connect=...,
    backoff_factor=1,
    status_forcelist=[500, ...],
)

session = requests.Session()
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
