from distutils.core import setup
from setuptools import find_packages

setup(
    name='sentry-log',
    version='0.1.0',
    packages=find_packages(exclude=['test', 'test.*']),
    url='https://github.com/lavab/sentry-log',
    author='pzduniak',
    author_email='piotr@zduniak.net',
    description='Integration helper for Sentry and Lavatrace',
    requires=['sentry'],
    entry_points={
        'sentry.apps': [
            'pluginname = sentry_log'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    license='MIT license',
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ]
)