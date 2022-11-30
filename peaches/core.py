"""
core: base class for configuring projects
Corey Rayburn Yung <coreyrayburnyung@gmail.com>
Copyright 2020-2022, Corey Rayburn Yung
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
    Settings (camina.Dictionary, ashford.SourceFactory): stores configuration 
        settings after either loading them from disk or by the passed arguments.

ToDo:
       
       
"""
from __future__ import annotations
import abc
from collections.abc import Hashable, Mapping, MutableMapping, Sequence
import configparser
import contextlib
import dataclasses
import importlib
import importlib.util
import pathlib
from typing import Any, ClassVar, Optional, Type, Union

import ashford
import camina


@dataclasses.dataclass
class Parser(abc.ABC):
    """

    Args:
        
        
    """
    name: str
    terms: Optional[tuple[str, ...]] = tuple()
    match: Optional[str] = 'complete'
    scope: Optional[str] = 'both'
    divider: Optional[str] = ''

    """ Required Subclass Methods """
    
    @abc.abstractmethod
    def apply(self, settings: Settings) -> Any:
        """Applies the parser to a Settings instance.

        Args:
            settings (Settings): configuration settings to parse.

        Returns:
            Any: information derived from parsing.
            
        """
        pass
    
    """ Private Nethods """

    
    def _search_both(self, settings: Settings) -> Any:
        """Applies the parser to a Settings instance.

        Args:
            settings (Settings): configuration settings to parse.

        Returns:
            Any: information derived from parsing.
            
        """
        pass
    
    def _search_inner(self, settings: Settings) -> Any:
        """Applies the parser to a Settings instance.

        Args:
            settings (Settings): configuration settings to parse.

        Returns:
            Any: information derived from parsing.
            
        """
        pass

    def _search_outer(self, settings: Settings) -> Any:
        """Applies the parser to a Settings instance.

        Args:
            settings (Settings): configuration settings to parse.

        Returns:
            Any: information derived from parsing.
            
        """
        pass
           