from setuptools import setup, find_packages
 
setup(
  name='progress_bar',
  version='0.1',
  url='https://github.com/pjt3591oo/progress_bar',
  license='MIT',
  author='JeongTae Park',
  author_email='pjt3591oo@gmail.com',
  description='progress bar for loading',
  packages=["progress_bar"],
  long_description=open('README.md').read(),
  zip_safe=False
  # setup_requires=['nose>=1.0']
  # test_suite='nose.collector'
)