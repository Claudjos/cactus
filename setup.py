import sys
from setuptools import setup, find_packages


NAME = "cactus"
VERSION = "0.0.1"

REQUIRES = []


setup(
    name=NAME,
    version=VERSION,
    description="description",
    author_email="claudjosmail@gmail.com",
    url="",
    keywords=["Azure Function", "Web App"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={},
    include_package_data=False,
    long_description="long description"
)
