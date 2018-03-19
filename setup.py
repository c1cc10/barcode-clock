from setuptools import find_packages, setup

setup(name='barcode-clock',
      version='0.1',
      description='clock whose output is barcode',
      long_description=""" Desktop Clock that outputs date time in barcode format. It can be easily read by one barcode scanner for quickly insert. As barcode format we use 128 """,
      url='https://github.com/c1cc10/barcode-clock',
      author='Francesco Rana',
      author_email='rana@isolved.it',
      license='GPL',
      packages=['barCodeClock'],
      py_modules=["code128_test"],
      install_requires=[
          'PIL',
          'pygame',
      ],
      zip_safe=False)
