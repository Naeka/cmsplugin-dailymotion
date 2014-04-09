from setuptools import setup, find_packages

version = '1.0'

setup(
    name='cmsplugin-dailymotion',
    version=version,
    description='Dailymotion plugin for Django-CMS',
    author='Naeka',
    author_email='contact@naeka.fr',
    url='https://github.com/naeka/cmsplugin-dailymotion',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    ],
)
