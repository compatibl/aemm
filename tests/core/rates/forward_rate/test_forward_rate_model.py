# Copyright (C) 2023-present The Project Contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
