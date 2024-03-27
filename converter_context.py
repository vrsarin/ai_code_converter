"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
import time
from langchain_text_splitters import Language
from file_context import CodeFileContext
from llm_types import LlmTypes


class ConverterContext:
    """Context for Converting Code"""
    __ctx_id: str = f"{time.time()}"
    __src_lang: Language
    __dest_lang: Language
    __remove_comments: bool = True
    __temp_folder: str
    __source_folder: str
    __dest_folder: str
    __file_context: CodeFileContext = CodeFileContext("")
    __llm_type: LlmTypes

    @property
    def context_id(self):
        """Source code file name with path"""
        return self.__ctx_id

    @property
    def source(self):
        """Source code file name with path"""
        return self.__src_lang

    @source.setter
    def source(self, value):
        """Source code file name with path"""
        self.__src_lang = value

    @property
    def target(self):
        """Source code file name with path"""
        return self.__dest_lang

    @target.setter
    def target(self, value):
        """Source code file name with path"""
        self.__dest_lang = value

    @property
    def llm(self):
        """Source code file name with path"""
        return self.__llm

    @llm.setter
    def llm(self, value):
        """Source code file name with path"""
        self.__llm = value

    @property
    def remove_comments(self):
        """Source code file name with path"""
        return self.__remove_comments

    @remove_comments.setter
    def remove_comments(self, value):
        """Source code file name with path"""
        self.__remove_comments = value

    @property
    def temporary_folder(self):
        """Source code file name with path"""
        return self.__temp_folder

    @temporary_folder.setter
    def temporary_folder(self, value):
        """Source code file name with path"""
        self.__temp_folder = value

    @property
    def file_context(self):
        """Source code file name with path"""
        return self.__file_context

    @file_context.setter
    def file_context(self, value):
        """Source code file name with path"""
        self.__file_context = value

    @property
    def source_folder(self):
        """Source code file name with path"""
        return self.__source_folder

    @source_folder.setter
    def source_folder(self, value):
        """Source code file name with path"""
        self.__source_folder = value

    @property
    def destination_folder(self):
        """Source code file name with path"""
        return self.__dest_folder

    @destination_folder.setter
    def destination_folder(self, value):
        """Source code file name with path"""
        self.__dest_folder = value

    @property
    def llm_type(self):
        """Source code file name with path"""
        return self.__llm_type

    @llm_type.setter
    def llm_type(self, value):
        """Source code file name with path"""
        self.__llm_type = value
