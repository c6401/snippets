#!/usr/bin/env -S uv run
# /// script
# dependencies = ["fastapi", "fastcore", "python-multipart", "uvicorn"]
# ///
import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Response
from fastcore.xml import Body, Html, Script, to_xml

class FTR(Response):
    media_type = "text/html"
    def render(self, content) -> bytes:
        return to_xml(content).encode("utf-8")

app = FastAPI()

@app.get("/")
async def index():
    return FTR(Html(Script(src='https://cdn.jsdelivr.net/npm/htmx@0.0.2/htmx.min.js'), Body('Hello')))

uvicorn.run(app, port=8080)
