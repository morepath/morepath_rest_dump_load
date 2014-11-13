import os
from setuptools import setup, find_packages

setup(name='morepath_rest',
      version='0.1dev',
      description="Morepath REST Demo",
      author="Martijn Faassen",
      author_email="faassen@startifact.com",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'morepath >= 0.8',
        ],
      entry_points= {
        'console_scripts': [
            'morepath_rest = morepath_rest.main:main',
            ]
        },
      )
