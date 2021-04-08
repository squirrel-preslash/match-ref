from setuptools import setup
import os

with open(os.path.join(os.path.dirname(__file__), "README.md")) as file:
    readme = file.read()

setup(
    name="match-ref",
    version="1.0.0",
    description="Use top-level variable references in match cases",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/squirrel-preslash/match-ref",
    author="Squirrel-Preslash",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10"
    ],
    packages=["matchref"]
)

