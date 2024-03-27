"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
import os
from langchain_text_splitters import Language
from cobol.divisions import CobolDivisions
from cobol.prompts import CobolPrompts
from cobol.splitter import CobolSplitter
from code_converter import CodeConverter
from converter_context import ConverterContext
from llm_manager import LlmManager
from llm_types import LlmTypes
from splitter_base import SplitterBase
from utils import load_file


class CobolConverter(CodeConverter):
    """implementation for Cobol Source Code"""
    __splitter: SplitterBase = None

    def __init__(self, llm_type: LlmTypes, target: Language = Language.JAVA) -> None:
        super()._ctx.source = Language.COBOL
        super()._ctx.target = target
        super()._ctx.llm_type = llm_type

    def _prepare(self, context: ConverterContext):
        context.file_context.temporary_files = {
            f"{CobolDivisions.ENVIRONMENT}": f"{context.temporary_folder}/environment.cbl",
            f"{CobolDivisions.DATA}": f"{context.temporary_folder}/data.cbl",
            f"{CobolDivisions.PROCEDURE}": f"{context.temporary_folder}/procedure.cbl",
        }
        self.__splitter = CobolSplitter(context)
        self.__splitter.split(context)

    def _analyze(self, context: ConverterContext):
        llm = LlmManager(context)
        # Extract Data from Data Division
        llm.extract_information_chunked(prompt=CobolPrompts.DATA.value,
                                        file_name=os.path.join(
                                            context.destination_folder, "data.md"),
                                        content=load_file(context.file_context.temporary_files[f"{CobolDivisions.DATA}"]))

        # Extract pseudo code
        for file in self._ctx.file_context.converted_files:
            file_content = load_file(file)
            llm.extract_information(prompt=CobolPrompts.PROCEDURE.value,
                                    file_name=os.path.join(
                                        context.destination_folder, "procedure.md"),
                                    content=file_content)

    def _generate_code(self, context: ConverterContext):
        """Generate the technical documents for the given source code"""
        llm = LlmManager(context)

        # print(os.path.join(context.destination_folder, "procedure.md"))

        # content = load_file(os.path.join(
        #     context.destination_folder, "procedure.md"))

        # llm.extract_information_chunked(prompt=CobolPrompts.CODE, file_name=os.path.join(
        #     context.destination_folder, f"{context.target}.txt"), content=content)
