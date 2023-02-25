# Copyright (C) 2003-present CompatibL. All rights reserved.
#
# This file contains valuable trade secrets and may be copied, stored, used,
# or distributed only in compliance with the terms of a written commercial
# license from CompatibL and with the inclusion of this copyright notice.

import aenc
import pytest

import aemm

# Tests for ForwardRateModels


def test_smoke():
    """Smoke test."""

    # At this point we just ensure that we can create an instance
    # of one class from this package and one class from aenc package
    obj1 = aemm.ForwardRateModel()
    obj2 = aenc.NelsonSiegel()


if __name__ == '__main__':
    pytest.main([__file__])
