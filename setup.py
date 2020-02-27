import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

requirements = []
dev_requirements = [
    "black",
    "flake8",
    "pytype",
]

# This call to setup() does all the work
setup(
    name="leoprofanity",
    version="0.0.1",
    description="Profanity filter, based on Shutterstock dictionary",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jojoee/leo-profanity-python",
    author="Nathachai Thongniran",
    author_email="inid3a@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["leoprofanity"],
    include_package_data=False,
    install_requires=[],
    extras_require={"dev": dev_requirements},
    entry_points={"console_scripts": ["leoprofanity=leoprofanity.__main__:main"]},
)
