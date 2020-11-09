import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="streamlit_downloader",
    version="0.0.1",
    author="Jeremy Haak",
    author_email="jamincan@gmail.com",
    description="A basic static widget for displaying a download link with streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamincan/streamlit-downloader",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
        "python-magic >= 0.4",
    ],
)
