# streamlit-downloader
A basic widget for displaying a download link with streamlit.

## Installation
You can install this package using pip:

```pip install https://github.com/jamincan/streamlit-downloader/releases/download/0.0.1/streamlit_downloader-0.0.1.tar.gz```

This package depends on python-magic. Windows users should also install python-magic-bin using:

```pip install python-magic-bin```

## Usage
This widget receives a byte stream and filename and generates a download link in your streamlit app.

### Example:

```
from io import BytesIO

import streamlit as st
from streamlit_downloader import downloader

with open("example.txt", "rb") as fh:
    data = BytesIO(fh.read())

downloader(data, "example.txt")
```
