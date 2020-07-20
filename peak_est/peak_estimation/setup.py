# Import needed function from setuptools
from setuptools import setup

# Create proper setup to be used by pip
setup(name='peak_estimation',
      version='0.0.1',
      description='Detect true peaks in a distribution.',
      author='Julia MacMillan',
      packages=['peak_estimation'],
      install_requires=['matplotlib >= 3.0.0',
                        'numpy == 1.15.4',
                        'pandas <= 0.22.0',
                        'pycodestyle'])
