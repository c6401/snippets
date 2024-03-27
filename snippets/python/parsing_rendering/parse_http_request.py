def parse_http_request(blob):
    head, _, body = blob.partition('\n\n')
    request_line, *lines = head.splitlines()
    method, path, *_ = request_line.split(' ')
    headers = {h: v for h, v in (l.split(': ') for l in lines)}
    return method, path, headers, body
