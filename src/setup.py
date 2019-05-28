from setuptools import setup

setup(name='nocha',
      version='0.1.0',
      description='nocha is a tool that makes it easier to swap versions of node with',
      url='https://github.com/FaizChishtie/nocha',
      author='Faizaan Chishtie',
      author_email='faizchishtie@gmail.com',
      entry_points = {'console_scripts': ['nocha = main']},
      keywords = ['nocha'])
