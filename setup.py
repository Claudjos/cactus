import sys
from setuptools import setup, find_packages


NAME = "pycactus"
VERSION = "0.0.1"

REQUIRES = ["azure-functions"]


setup(
    name=NAME,
    version=VERSION,
    description="Adapter to run an Azure Function Application with a WSGI Web Server.",
    author="Claudjos",
    author_email="claudjosmail@gmail.com",
    url="https://github.com/Claudjos/cactus",
    keywords=["Azure Function", "Web App"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={},
    include_package_data=False,
    long_description="Adapter to run an Azure Function Application with a WSGI Web Server."
)
