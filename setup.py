from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='work_order',
    version=version,
    description='Application to manage work order for the service company',
    author='Aptitude',
    author_email='support@aptitudetech.net',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
