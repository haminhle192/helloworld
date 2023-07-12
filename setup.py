# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

packages = []

with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt"),
    encoding="utf-8",
) as f:
    dev_requires = f.read().strip().split("\n")

setup(
    name="Dataloader",
    version="0.0.0",
    description="Dataloader",
    long_description=readme,
    author="Lita",
    author_email="lita@cinnamon.is",
    url="https://github.com/haminhle192/helloworld",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=packages,
    extras_require={
        "dev": dev_requires,
    },
    python_requires=">=3.8",
)
