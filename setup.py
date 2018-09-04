import setuptools
import re


APP_NAME = "proxycrawl"

# Get long description
with open("README.md", "r") as fh:
    long_description = fh.read()

# Get the version
version_regex = r'__version__ = ["\']([^"\']*)["\']'
with open('proxycrawl/__init__.py', 'r') as f:
    text = f.read()
    match = re.search(version_regex, text)

    if match:
        VERSION = match.group(1)
    else:
        raise RuntimeError("No version number found!")


setuptools.setup(
    name=APP_NAME,
    version=VERSION,
    author="Shu Yan",
    author_email="yanshu.usc@gmail.com",
    description="An easy-to-use Python library for using proxycrawl(https://proxycrawl.com/).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SYAN83/proxycrawl",
    packages=setuptools.find_packages(exclude=['tests']),
    python_requires=">=3.5",
    install_requires=[
        "requests>=2.11.1",
        "aiohttp>=2.3",
        "scrapy"
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
