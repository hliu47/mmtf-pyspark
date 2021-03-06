from setuptools import setup

mmtfPyspark_packages = ['mmtfPyspark',
                        'mmtfPyspark.datasets',
                        'mmtfPyspark.filters',
                        'mmtfPyspark.io',
                        'mmtfPyspark.mappers',
                        'mmtfPyspark.ml',
                        'mmtfPyspark.utils',
                        'mmtfPyspark.webfilters',
                        'mmtfPyspark.webservices',
                        'mmtfPyspark.interactions'
                        ]

mmtfPyspark_dependencies = ['pyspark==2.3.1',
                            'biopython>=1.71',
                            'msgpack>=0.5.6',
                            'numpy>=1.14.5',
                            'ipywidgets>=7.2.1',
                            'mmtf-python==1.1.2',
                            'requests>=2.19.1',
                            'matplotlib>=2.2.2',
                            'seaborn>=0.8.1',
                            'sympy>=1.1.1',
                            'py3Dmol>=0.7.2',
                            'scipy>=1.1.0',
                            'scikit-learn>=0.19.0',
                            'py4j==0.10.7'
                            ]

LONG_DESCRIPTION = """
**mmtfPyspark** is a python package that provides APIs and sample applications for distributed analysis and scalable mining of 3D biomacromolecular structures, such as the Protein Data Bank (PDB) archive. mmtfPyspark uses Big Data technologies to enable high-performance parallel processing of macromolecular structures.
"""

setup(name='mmtfPyspark',
      version='0.2.6',
      description='Methods for parallel and distributed analysis and mining of the Protein Data Bank using MMTF and Apache Spark',
      long_description=LONG_DESCRIPTION,
      url='https://github.com/sbl-sdsc/mmtf-pyspark',
      author='Mars Huang (Shih-Cheng)',
      author_email='marshuang80@gmail.com',
      license='Apache License 2.0',
      keywords='mmtf spark pyspark protein PDB',
      packages=mmtfPyspark_packages,
      install_requires=mmtfPyspark_dependencies,
      python_requires='>=3.6',
      include_package_data=True,
      test_suite='nose.collector',
      test_require=['nose'],
      classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Science/Research',
                 'Topic :: Scientific/Engineering :: Bio-Informatics',
                 'License :: OSI Approved :: Apache Software License',
                 'Programming Language :: Python :: 3.6'],
      zip_safe=False)
