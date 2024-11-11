#!/usr/bin/env python
# /// script
# requires-python = ">=3.8"
# dependencies = [
#     "fast-html",
# ]
# ///
from fasthtml.common import *

app, rt = fast_app()

@rt('/')
def get(): return Div(P('Hello'), hx_get="/change")

serve()