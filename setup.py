from setuptools import setup

setup(name='cvlib',
      version='0.2.4',
      description='A high level, easy to use, open source computer vision library for python',
      long_description='A high level, easy to use, open source computer vision library for python',
      url='https://github.com/veverkap/cvlib.git',
      author='Arun Ponnusamy',
      author_email='hello@veverka.net',
      license='MIT',
      packages=['cvlib'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['numpy', 'progressbar', 'requests', 'pillow', 'imageio',
                        'imutils']
      )
