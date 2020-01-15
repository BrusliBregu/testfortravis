from distutils.core import setup
import setuptools

setup( name = "travelplanner", version = "0.0.1", packages = setuptools.find_packages(exclude=['*test']), install_requires = ['numpy', 'matplotlib', 'pyyaml'])
