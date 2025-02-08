from setuptools import setup

setup(
    name='my_project',
    version='0.0.1',
    packages=['good_inventory'],
    entry_points={
        'console_scripts': [
            'my_project=good_inventory.main:main',
        ],
    },
)


