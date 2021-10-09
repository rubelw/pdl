import setuptools

from peopledatalabs import __version__


setuptools.setup(
    name='peopledatalabs',
    version=__version__
    author='Will Rubel',
    author_email='willrubel@gmail.com',
    description='People Data Labs Query Tool',
    keywords='People Data Labs',
    long_description='People Data Labs Query Tool',
    url='https://github.com/rubelw/pdl',
    project_urls={
        'Documentation': 'https://github.com/rubelw/pdl',
        'Bug Reports':
        'https://github.com/rubelw/pdl/issues',
        'Source Code': 'https://github.com/rubelw/pdl',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    include_package_data=True,
    packages=setuptools.find_packages(where='src'),
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
    install_requires=[
        'requests'
    ],
    entry_points={
         'console_scripts': [  # This can provide executable scripts
             'pdl=peopledatalabs:main',
    # You can execute `run` in bash to run `main()` in src/examplepy/__init__.py
         ]
     }
)
