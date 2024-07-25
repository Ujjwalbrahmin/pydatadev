from setuptools import setup, find_packages

setup(
    name='pydatadev',
    version='0.0.1',
    description='PyDataDev is envisioned as a utility package for software engineers.' + \
                'working in Big data and Backend, infra and distributed systems.',
    url='https://github.com/Ujjwalbrahmin/pydevutil/',
    author='Ujjwal Brahmin',
    author_email='ujjwalbrahmin@gmail.com',
    license='MIT License',
    packages=find_packages(include=[
        'pydatadev',
        'pydatadev.*'
    ]),
    install_requires=[
        'simplejson==3.19.1',
        'pytest==8.3.1',
        'pytest-mock==3.14.0'
    ],
    python_requires='>=3.10',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Plugins',
        'Framework :: AWS CDK',
        'Framework :: Apache Airflow',
        'Framework :: AsyncIO',
        'Framework :: Pytest',
        'Framework :: Sphinx',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: BSD :: OpenBSD',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: File Formats',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Mocking',
        'Topic :: Software Development :: Testing :: Unit',
        'Topic :: Software Development :: Version Control',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
        'Typing :: Typed'
    ],
)
