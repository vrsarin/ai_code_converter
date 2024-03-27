"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
from abc import ABC, abstractmethod

from converter_context import ConverterContext


class SplitterBase(ABC):
    """Abstract base class for spllitters"""
    files: list[str] = []

    @abstractmethod
    def split(self, context: ConverterContext):
        """Abstract Method for splitting"""
        pass
