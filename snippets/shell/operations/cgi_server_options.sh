python -c "from http.server import HTTPServer,CGIHTTPRequestHandler;CGIHTTPRequestHandler.do_OPTIONS=lambda self:self.do_GET();HTTPServer(('0.0.0.0',8888),CGIHTTPRequestHandler).serve_forever()"
