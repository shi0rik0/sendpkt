from pathlib import Path

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="hello_world",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(Path(__file__).parent / "requirements.txt")
        )
    ],
    entry_points={
        "console_scripts": [
            "hello-world = hello_world.main:main",
        ]
    },
)
