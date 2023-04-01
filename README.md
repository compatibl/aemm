# Autoencoder Market Models (AEMM)

## Overview

This package implements autoencoder-based models in Q- and P-measure.
The initial set of models is for interest rates. More asset classes
may be added at a later date.

The package takes specialized autoencoders and classical methods for performing dimension
reduction in quant models of financial markets from `aenc` package (https://pypi.org/project/aenc/).


## Quick Start Guide

Install using:

```shell
pip install aemm
```

## Namespaces

Namespace `aemm.core` implements autoencoder-based market models (AEMM)
and related classical models.

The implementation uses PyTorch and can be easily ported to TensorFlow 2
and other machine learning frameworks that support dynamic computational
graphs.

Namespace `aemm.dummy` includes dummy objects and generators for dummy market
data for testing purposes. To perform testing or training on real
historical or market-implied data, provide your own data files in the same
format as the dummy data files, or use pretrained components.

Namespace `aemm.pretrained` includes pretrained components to avoid lengthy
test execution time. Use flags to ignore pretrained parameters
and perform training from scratch (calculation time will increase).

## Licensing

The code in this project is licensed under Apache 2.0 license.
See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.html) for more information.

## Copyright

Each individual contributor holds copyright over their contributions to the
project. The project versioning is the sole means of recording all such
contributions and copyright details. Specifying corporate affiliation or
work email along with the commit shall have no bearing on copyright ownership
and does not constitute copyright assignment to the employer. Submitting a
contribution to this project constitutes your acceptance of these terms.

Because individual contributions are often changes to the existing code,
copyright notices in project files must specify The Project Contributors and
never an individual copyright holder.

## Publications and Links

1. Alexander Sokol, Autoencoder Market Models for Interest Rates, SSRN Working Paper https://ssrn.com/abstract=4300756
2. This project on GitHub: https://github.com/compatibl/aemm
3. Autoencoders for financial markets on GitHub: https://github.com/compatibl/aenc

