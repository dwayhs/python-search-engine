from search_indexer import (__author__,
                            __email__,
                            __version__,
                            __project__,
                            __description__)


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def load_from(filename):
    with open(filename) as requirements:
        return requirements.read().splitlines()


setup(
    name=__project__,
    version=__version__,
    description=__description__,
    long_description='',
    author=__author__,
    author_email=__email__,
    packages=[
        'py_search_engine'
    ],
    package_dir={
        'py_search_engine': __project__
    },
    install_requires=load_from('requirements.txt')
)
