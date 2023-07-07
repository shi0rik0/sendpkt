from pathlib import Path

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="sendpkt",
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
            "sendpkt = sendpkt.main:main",
        ]
    },
)
