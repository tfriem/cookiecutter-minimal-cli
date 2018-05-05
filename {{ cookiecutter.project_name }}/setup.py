from setuptools import setup

setup(name='{{ cookiecutter.project_slug }}',
      version='0.1',
      author='{{ cookiecutter.author }}',
      author_email='{{ cookiecutter.author_email }}',
      packages=['{{ cookiecutter.project_slug }}'],
      install_requires=[],
      entry_points={
          'console_scripts': ['{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.command_line:main']
      })
