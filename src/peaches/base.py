"""
base: base classes for peaches representations
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2020-2023, Corey Rayburn Yung
License: Apache-2.0

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

Contents:
    Representation (object): data for a data type's representation.
         
ToDo:
    Completely rewrite. Consider removing class entirely (or moving it to a 
        separate module like Inspector in 'observe' subpackage).
    Clean up and add DocStrings.
    Add a textwrap option when VERTICAL is False.
    
"""
from __future__ import annotations
from collections.abc import (
    Hashable, Iterable, Mapping, MutableMapping, MutableSequence, Sequence)
import dataclasses
import inspect
from types import FunctionType
from typing import Any, Optional, Type

import camina


LINE_BREAK: str = '\n'
WHITESPACE: str = ' '
TAB: int = 3
INDENT: str = WHITESPACE * TAB
MAX_WIDTH: int = 40
MAX_LENGTH: int = 20
INCOMPLETE: str = '...'
VERTICAL: bool = True


@dataclasses.dataclass
class Representation(object):
    """Contains formating information for different data types.
    
    Args:
        name (str): name of data type to be used in the str returned by 
            'beautify'.
        method (FunctionType): the function to use to beautify the particular
            data type.
        start (str): starting bracket for listing the contents of the data type.
            Defaults to ''.
        end (str): ending bracket for listing the contents of the data type.
            Defaults to ''.           
    
    """
    name: str
    method: FunctionType
    start: str = ''
    end: str = ''
