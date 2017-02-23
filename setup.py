
from setuptools import setup, find_packages

setup(name = "The_Boids", version = "0.1.0", packages = find_packages(exclude=['*test']), scripts = ['scripts/boids'], install_requires = ['numpy', 'matplotlib'], include_package_data = True)