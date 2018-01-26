from setuptools import setup

setup(name='barcode-clock',
      version='0.1',
      description='clock whose output is barcode',
      url='https://github.com/c1cc10/barcode-clock',
      author='Francesco Rana',
      author_email='rana@isolved.it',
      license='GPL',
      packages=['barCodeClock'],
      install_requires=[
          'PIL',
          'pygame',
      ],
      zip_safe=False)
