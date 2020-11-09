from base64 import b64encode
from io import BytesIO
from pathlib import Path
from string import Template

import magic
import streamlit.components.v1 as components

_RELEASE = True


def downloader(data: BytesIO, filename: str):
    """Create an instance of a simple file downloader component."""

    def size(data: BytesIO):
        size = len(data.getvalue())
        if size >= 1000000:
            return f"{size/1000000}MB"
        elif size >= 1000:
            return f"{size/1000}KB"
        else:
            return f"{size}B"

    context = {
        "filename": filename,
        "mimetype": magic.from_buffer(data.getvalue(), mime=True),
        "size": size(data),
        "b64": b64encode(data.getvalue()).decode(),
    }

    template_path = Path(__file__).resolve().parent / "downloader.html"
    with open(template_path, "r") as f:
        template = Template(f.read())

    components.html(template.substitute(context), height=45)


if not _RELEASE:
    from io import StringIO

    import streamlit as st

    st.title("Streamlit Downloader Component")

    if f := st.file_uploader(""):
        downloader(f, f.name)
