import setuptools
from src import __version__

setuptools.setup(name='nocha',
      version=__version__,
      description='nocha is a tool that makes it easier to swap versions of node with',
      url='https://github.com/FaizChishtie/nocha',
      author='Faizaan Chishtie',
      author_email='faizchishtie@gmail.com',
      packages=setuptools.find_packages(),
      python_requires='>=2.7',
      entry_points={'console_scripts': ['nocha = src.__main__:main']},
      keywords=['nocha'])
