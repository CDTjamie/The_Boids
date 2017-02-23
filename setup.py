
from setuptools import setup, find_packages

setup(name = "The_Boids",
      version = "0.1.0", 
      description = "refactored Python flocking code",
      author = "Jamie Potter",
      packages = find_packages(exclude=['*test']), 
      scripts = ['scripts/boids'], 
      install_requires = ['numpy', 'matplotlib', 'pyyaml', 'pyrandom'], 
      include_package_data = True)