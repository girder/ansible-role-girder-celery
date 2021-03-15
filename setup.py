from setuptools import find_packages, setup

setup(
    name='test-project',
    license='Apache 2.0',
    install_requires=[
        'celery',
    ],
    packages=find_packages(),
)
