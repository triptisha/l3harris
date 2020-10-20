# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in l3harris/__init__.py
from l3harris import __version__ as version

setup(
	name='l3harris',
	version=version,
	description='L3Harris ISP Ecommerce Website',
	author='Rahi Systems Pvt Ltd',
	author_email='vigneshwaran.a@rahisystems.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
