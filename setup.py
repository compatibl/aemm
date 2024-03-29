import setuptools

with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('./install_requirements.txt') as install_requirements:
    install_requires = [line.strip() for line in install_requirements.readlines()]

setuptools.setup(
    name='aemm',
    version='0.0.2',
    author='The Project Contributors',
    description='Autoencoder Market Models (AEMM)',
    license='Apache Software License',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=install_requires,
    url='https://github.com/compatibl/aemm',
    project_urls={
        'Source Code': 'https://github.com/compatibl/aemm',
    },
    packages=setuptools.find_namespace_packages(
        where='.', include=['cl.aemm', 'cl.aemm.*'], exclude=['tests', 'tests.*']
    ),
    package_dir={'': '.'},
    classifiers=[
        # Alpha - will attempt to avoid breaking changes but they remain possible
        'Development Status :: 3 - Alpha',

        # Audience and topic
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Software Development',
        'Topic :: Scientific/Engineering',

        # License
        'License :: OSI Approved :: Apache Software License',

        # Supported Python versions
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',

        # Operating system
        'Operating System :: OS Independent',
    ],
)
