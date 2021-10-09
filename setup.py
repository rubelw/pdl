from __future__ import absolute_import, division, print_function
from setuptools import setup, find_packages
import sys
from os import path
from io import open

DESCRIPTION = ('People Data Labs Query Tool')

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup_requires = (
    ['pytest-runner'] if any(x in sys.argv for x in ('pytest','test','ptr')) else []
)


setup(
    name='peopledatalabs',
    version='0.1.10',
    author='Will Rubel',
    author_email='willrubel@gmail.com',
    description=DESCRIPTION,
    keywords='People Data Labs',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/rubelw/pdl',
    project_urls={
        'Documentation': 'https://github.com/rubelw/pdl',
        'Bug Reports':
        'https://github.com/rubelw/pdl/issues',
        'Source Code': 'https://github.com/rubelw/pdl'
    },
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=required,
    entry_points={
         'console_scripts': [  # This can provide executable scripts
             'pdl=peopledatalabs:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
         ]
     }
)
