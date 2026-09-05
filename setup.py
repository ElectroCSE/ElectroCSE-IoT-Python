"""
Packaging metadata.

setup.py rather than a bare pyproject.toml on purpose: this package will be
installed on Raspberry Pi OS, where the system Python and pip are often several
years old, and `pip install .` against a PEP 517-only project on an old pip
fails with an error about build backends that tells a student nothing useful.
A setup.py still works everywhere, including there.
"""

from pathlib import Path

from setuptools import find_packages, setup

README = Path(__file__).parent / "README.md"

setup(
    name="electrocse-iot",
    version="0.0.1",
    description="Python client for the ElectroCSE IoT dashboard",
    long_description=README.read_text(encoding="utf-8") if README.exists() else "",
    long_description_content_type="text/markdown",
    author="ElectroCSE",
    author_email="info@electrocse.com",
    url="https://github.com/electrocse/ElectroCSE-IoT-Python",
    project_urls={
        "Dashboard": "https://iot.electrocse.com",
        "Arduino library": "https://github.com/electrocse/ElectroCSE-IoT",
        "Support": "https://support.electrocse.com",
    },
    license="MIT",
    packages=find_packages(exclude=("tests", "tests.*")),
    # 3.7 is what Raspberry Pi OS Buster shipped, and there are a lot of those
    # boards still in classrooms. Nothing planned here needs anything newer.
    python_requires=">=3.7",
    install_requires=[
        # The only hard dependency, and it is the one every Pi already has.
        "requests>=2.25",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Hardware",
    ],
)
