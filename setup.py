from distutils.core import setup
setup(
  name='xpath_generator',
  packages=['xpath_generator'],
  version='0.2',
  description="Generate Xpath list after giving tag, attribute and attribute' value.",
  author='Terry Hung',
  author_email='terryhung1228@gmail.com',
  url='https://github.com/Terryhung/Xpath_Generator',
  download_url='https://github.com/Terryhung/Xpath_Generator/archive/master.zip',
  keywords=['xpath', 'generator'],
  install_requires=['bs4', 'requests'],
  classifiers=[],
)
