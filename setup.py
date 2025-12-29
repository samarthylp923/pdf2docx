"""
Setup configuration for pdf2docx converter package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="pdf2docx-converter",
    version="0.1.0",
    description="A simple PDF to DOCX converter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Samarthy",
    url="https://github.com/samarthylp923/pdf2docx",
    py_modules=["converter", "cli"],
    install_requires=[
        "pdf2docx>=0.5.6",
        "python-docx>=0.8.11",
        "PyMuPDF>=1.23.0",
    ],
    entry_points={
        "console_scripts": [
            "pdf2docx=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office/Business :: Office Suites",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
