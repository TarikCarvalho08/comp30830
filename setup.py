from setuptools import setup

setup(name='systemInfo',
      version='0.1',
      description='System Information',
      url='',
      author='Tarik Carvalho',
      author_email='tarik.caravalho@ucdconnect.ie',
      license='MIT',
      packages=['fileFolder'],
      entry_points={'console_scripts':['systemInfo=fileFolder.systemInfo:main']},
      zip_safe=False)

