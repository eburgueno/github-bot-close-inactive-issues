from setuptools import setup, find_packages
import os

VERSION = '0.0.1'

scripts = [os.path.join("scripts", file) for file in ["github_rate_limit.py", "github_close_inactive_issues.py"]]
package_data = {"github_bot":["logging.conf"]}

setup(name='github-bot',
      version=VERSION,
      description='Bot for managing GitHub repositories',
      url='https://github.com/bstriner/github-bot',
      author='Ben Striner',
      author_email='btriner@gmail.com',
      license='',
      packages=find_packages(),
      scripts=scripts,
      package_data=package_data,
      install_requires=[
          'PyGithub'
      ]
      )