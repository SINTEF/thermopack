from distutils.core import setup
import warnings

warnings.warn('ThermoPack is now part of the ThermoTools project, being maintained at '
              'https://github.com/thermotools/thermopack', DeprecationWarning)

yn = input('Are you sure you wish to continue with this deprecated version? (Y/n)')
if yn != 'Y':
      exit(0)

setup(name='pyctp',
      version='1.0.0',
      description='pycThermopack',
      author='Morten Hammer',
      author_email='hammer.morten@sintef.no',
      url='https://github.com/SINTEF/thermopack',
      packages=['pyctp'],
      package_data={'pyctp':['libthermopack.*']}
)

