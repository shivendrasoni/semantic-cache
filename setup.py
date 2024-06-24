import os
import setuptools

# Read version from environment variable or default to "0.0.1"
VERSION = os.getenv("RELEASE_VERSION", "0.0.1")
NAME = "vector-cache"

# Read long description from README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Read the list of requirements from requirements.txt
with open("./requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()


setuptools.setup(
    name=NAME,  # This is the name of the package
    version=VERSION,  # The initial release version
    author="Shivendra Soni",  # Full name of the author
    description="A streamlined Python library that enhances LLM query performance through semantic caching, making responses faster and more cost-effective.",
    long_description=long_description,  # Long description read from the readme file
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),  # List of all python modules to be installed
    project_urls={
        "Source Code": "https://github.com/shivendrasoni/vector-cache",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires='>=3.9',  # Minimum version requirement of the package
    py_modules=["vector-cache"],  # Name of the python package
    package_dir={'': 'src'},  # Directory of the source code of the package
    install_requires=requirements  # Install dependencies from requirements.txt
)
