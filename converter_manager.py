"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
from langchain_text_splitters import Language

from cobol.converter import CobolConverter
from llm_types import LlmTypes


class ConverterManager:
    """Source Converter Manager"""

    @staticmethod
    def get_converter(source: Language, llm_type: LlmTypes, target: Language = Language.JAVA):
        """Get Proper Converter"""
        converter = None
        match source:
            case Language.COBOL:
                converter = CobolConverter(target=target, llm_type=llm_type)
            case _:
                raise NotImplementedError("Not implemented")
        return converter
