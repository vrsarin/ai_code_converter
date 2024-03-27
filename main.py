"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python

from langchain_text_splitters import Language

from converter_manager import ConverterManager
from llm_types import LlmTypes

convert = ConverterManager.get_converter(Language.COBOL, LlmTypes.OPENAI)

convert.transform("./.examples", "./.output/", True)
