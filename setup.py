import io
import os

from setuptools import setup, find_packages


def read(*names, **kwargs):
    """Read a file."""
    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


PACKAGE = "telecom_carrier"
NAME = "telecom_carrier"
DESCRIPTION = "Telecom Carrier Lab"
AUTHOR = "Haddley Trindade"
AUTHOR_EMAIL = "haddleytrindade@gmail.com"
URL = "https://github.com/hadtrindade/telecom-carrier"
VERSION = "0.0.1"

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="MIT",
    keywords="Telecom carrier lab",
    url=URL,
    description=DESCRIPTION,
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements_dev.txt")},
    packages=find_packages(exclude=["test", "docs"]),
    include_package_data=True,
    python_requires=">=3.8",
    setup_requires=["setuptools>=38.6.0"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
    platforms="any",
)
