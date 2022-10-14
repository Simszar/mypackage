from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['test*']),
    licence='EDS',
    description='Explore Data Science package tutorial example',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='Simphiwe Sithole',
    author_email='sssithole@hotmail.com'
)