import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

__version__ = "0.1.0"

# This call to setup() does all the work
setup(
    name="pythaiid",
    version=__version__,
    description="Verify and random Thai Nationality ID",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jojoee/pythaiid",
    author="Nathachai Thongniran",
    author_email="inid3a@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pythaiid"],
    include_package_data=False,
    install_requires=[],
    entry_points={"console_scripts": ["pythaiid=pythaiid.__main__:main"]},
)
