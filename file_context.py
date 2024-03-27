"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python


class CodeFileContext:
    """Context for each source code file"""
    __file: str = ""
    __temp_files: dict = {}
    __converted_files: list[str] = []

    def __init__(self, file: str) -> None:
        self.__file = file

    @property
    def file(self):
        """Source code file name with path"""
        return self.__file

    @file.setter
    def file(self, value):
        """Source code file name with path"""
        self.__file = value

    @property
    def temporary_files(self):
        """Temporary files generated during processing"""
        return self.__temp_files

    @temporary_files.setter
    def temporary_files(self, value):
        """Temporary files generated during processing"""
        self.__temp_files = value

    @property
    def converted_files(self):
        """Temporary files generated during processing"""
        return self.__converted_files

    @converted_files.setter
    def converted_files(self, value):
        """Temporary files generated during processing"""
        self.__converted_files = value
