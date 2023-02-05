import setuptools

with open('./README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('./requirements.txt') as requirements_file:
    requirements = [line.strip() for line in requirements_file.readlines()]

setuptools.setup(
    name="aemm",
    version="0.0.1",
    author="The Project Contributors",
    description="Autoencoder Market Models (AEMM)",
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    url="https://github.com/compatibl/aemm",
    packages=setuptools.find_packages(include=('aemm', 'aemm.*'), exclude=['tests', 'tests.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
