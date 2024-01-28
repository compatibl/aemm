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

from dataclasses import dataclass, field
from typing import Union

from cl.aemm.models.model_key import ModelKey
from cl.aemm.models.model_measure import ModelMeasure
from cl.aemm.models.model_type import ModelType


@dataclass
class Model(ModelKey):
    """Common base of all model implementations irrespective of type."""

    model_type: Union[str, ModelType] = field(default=None)
    """Enumeration for the model type."""

    model_measure: Union[str, ModelMeasure] = field(default=None)
    """Enumeration for the model measure (Q or P)."""
