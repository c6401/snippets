import curlparser
import httpx


def request_curl(string):
    request = curlparser.parse(string)

    response = httpx.request(
        method=request.method,
        url=request.url,
        headers={k: v.strip() for k, v in request.headers.items()},
        data=request.data,
    )
    return response
