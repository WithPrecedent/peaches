"""
matchers: 
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
from collections.abc import (
    Collection, Container, Hashable, Iterable, Mapping, MutableMapping, 
    MutableSequence, Sequence, Set)
import dataclasses
import functools
import inspect
import pathlib
import types
from typing import Any, Optional, Type, Union

import camina


""" Contents Matchers """
  
@functools.singledispatch
def contains(
    item: object,
    contents: Union[Type[Any], tuple[Type[Any], ...]]) -> bool:
    """Returns whether 'item' contains the type(s) in 'contents'.

    Args:
        item (object): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.
        
    Raises:
        TypeError: if 'item' does not match any of the registered types.
        
    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    raise TypeError(f'item {item} is not supported by {__name__}')

@contains.register(Mapping)    
def dict_contains(
    item: Mapping[Hashable, Any], 
    contents: tuple[Union[Type[Any], tuple[Type[Any], ...]],
                    Union[Type[Any], tuple[Type[Any], ...]]]) -> bool:
    """Returns whether dict 'item' contains the type(s) in 'contents'.

    Args:
        item (Mapping[Hashable, Any]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    return (
        serial_contains(item = item.keys(), contents = contents[0])
        and serial_contains(item = item.values(), contents = contents[1]))

@contains.register(MutableSequence)   
def list_contains(
    item: MutableSequence[Any],
    contents: Union[Type[Any], tuple[Type[Any], ...]]) -> bool:
    """Returns whether list 'item' contains the type(s) in 'contents'.

    Args:
        item (MutableSequence[Any]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    return serial_contains(item = item, contents = contents)

@contains.register(Set)   
def set_contains(
    item: Set[Any],
    contents: Union[Type[Any], tuple[Type[Any], ...]]) -> bool:
    """Returns whether list 'item' contains the type(s) in 'contents'.

    Args:
        item (Set[Any]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    return serial_contains(item = item, contents = contents)

@contains.register(tuple)   
def tuple_contains(
    item: tuple[Any, ...],
    contents: Union[Type[Any], tuple[Type[Any], ...]]) -> bool:
    """Returns whether tuple 'item' contains the type(s) in 'contents'.

    Args:
        item (tuple[Any, ...]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    if isinstance(contents, tuple) and len(item) == len(contents):
        technique = parallel_contains
    else:
        technique = serial_contains
    return technique(item = item, contents = contents)

@contains.register(Sequence)   
def parallel_contains(
    item: Sequence[Any],
    contents: tuple[Type[Any], ...]) -> bool:
    """Returns whether parallel 'item' contains the type(s) in 'contents'.

    Args:
        item (Sequence[Any]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    return all(isinstance(item[i], contents[i]) for i in enumerate(item))

@contains.register(Container)       
def serial_contains(
    item: Container[Any],
    contents: Union[Type[Any], tuple[Type[Any], ...]]) -> bool:
    """Returns whether serial 'item' contains the type(s) in 'contents'.

    Args:
        item (Container[Any]): item to examine.
        contents (Union[Type[Any], tuple[Type[Any], ...]]): types to check for
            in 'item' contents.

    Returns:
        bool: whether 'item' holds the types in 'contents'.
        
    """
    return all(isinstance(i, contents) for i in item)


def match_complete(self, setting: dict[Hashable, Any]) -> Any:
    """Applies the parser to a Settings instance.

    Args:
        setting (dict[Hashable, Any]): configuration setting to parse.

    Returns:
        Any: information derived from parsing.
        
    """
    pass

def match_prefix(
    item: Any, 
    terms: Sequence[str], 
    divider: Optional[str] = '') -> bool:
    """Applies the parser to 'item'.

    Args:
        item (Any: configuration setting to parse.

    Returns:
        Any: information derived from parsing.
        
    """
    for term in terms:
        prefix = term + divider
        if item.startswith(prefix):
            return True
    return False

def match_suffix(self, setting: dict[Hashable, Any]) -> Any:
    """Applies the parser to a Settings instance.

    Args:
        setting (dict[Hashable, Any]): configuration setting to parse.

    Returns:
        Any: information derived from parsing.
        
    """
    pass
