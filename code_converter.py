"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python

from abc import ABC, abstractmethod
import os

from converter_context import ConverterContext
from file_context import CodeFileContext


class CodeConverter(ABC):
    """Base Class for Converting Code"""
    _ctx: ConverterContext = ConverterContext()

    @abstractmethod
    def _prepare(self, context: ConverterContext):
        pass

    @abstractmethod
    def _analyze(self, context: ConverterContext):
        pass

    @abstractmethod
    def _generate_code(self, context: ConverterContext):
        pass

    def transform(self, src_folder: str, dest_folder: str, remove_comments: bool):
        """Initiates the transformation of provided source code"""
        self._ctx.source_folder = src_folder
        self._ctx.destination_folder = dest_folder
        self._ctx.remove_comments = remove_comments
        self._ctx.temporary_folder = os.path.join(
            self._ctx.destination_folder, "temp", self._ctx.context_id)
        if os.path.exists(src_folder):
            for file in os.listdir(src_folder):
                self._ctx.file_context = CodeFileContext(
                    os.path.join(src_folder, file))
                self._prepare(self._ctx)
                self._analyze(self._ctx)
                self._generate_code(self._ctx)
