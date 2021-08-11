from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
name = "ns2trace",
version = "1.0.0",
author = "Abhinav Dubey",
author_email = "abhinavbhardwaj510@gmail.com",
packages=['ns2trace'],
description = "Trace File Analyser for NS2 Trace Files",
long_description=long_description,
long_description_content_type="text/markdown",
url = "https://github.com/abhinav-bhardwaj/ns2trace",
download_url = "https://github.com/abhinav-bhardwaj/ns2trace",
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Topic :: Scientific/Engineering :: Information Analysis",
],
package_dir = {"": "src" },
install_requires=['awk>=1.2.1'],
packages = find_packages(where="src"),
python_requires = ">=2.7.18",
)
