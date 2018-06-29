from distutils.core import setup

setup(
    # Application name:
    name="dataFormatter",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="vishwanathAV",
    author_email="vishwanathavin@gmail.com",

    # Packages
    packages=["dataFormatter"],

    # Include additional files into the package
    include_package_data=True,

    # Details
    url="http://pypi.python.org/pypi/dataFormatter_v010/",

    #
    # license="LICENSE.txt",
    description="Changes the datatype of the variables and realigns it",

    # long_description=open("README.txt").read(),

    # Dependent packages (distributions)
    install_requires=[
        "pandas",
    ],
)