
import os, sys

try:
    from setuptools import setup
    from setuptools import find_packages
except:
    from distutils.core import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def read_requirements(fname):
    f = open(os.path.join(os.path.dirname(__file__), fname))
    return filter(lambda f: f != '', map(lambda f: f.strip(), f.readlines()))

setup(
    zip_safe = False,
    name = "cms-bootstrap-templates",
    version = "1.1.0",
    author = "Charles Hathaway",
    author_email = "chathaway@logrit.com",
    description = "This package provides a variety of Django CMS templates designed using Twitter Bootstrap",
    keywords = "",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires = read_requirements('libraries.txt'),
    test_suite = "dummy",
    include_package_data=True,
)
