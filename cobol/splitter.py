"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
import os
from cobol.divisions import CobolDivisions
from converter_context import ConverterContext
from splitter_base import SplitterBase


class CobolSplitter(SplitterBase):
    """Cobol Splitter"""

    __envi_file: str = ""
    __data_file: str = ""
    __proc_file: str = ""

    def __init__(self, context: ConverterContext) -> None:

        self.__clean_dir(context.temporary_folder)

# --------------------------------------------------
# Private methods
# --------------------------------------------------

    def __clean(self, file: str):
        if os.path.exists(file) is True:
            os.remove(file)

    def __clean_dir(self, folder: str):
        if os.path.exists(folder):
            for file in os.listdir(folder):
                self.__clean(f"{folder}/{file}")

    def __save(self, file: str, content: str):
        os.makedirs(os.path.dirname(file), exist_ok=True)
        with open(file, 'a', encoding="utf-8") as f:
            f.write(content)

    def __process_line(self, division: CobolDivisions, content: str):
        match division:
            case CobolDivisions.START:
                self.__save(self.__envi_file, content)
                self.__save(self.__data_file, content)
                self.__save(self.__proc_file, content)
            case CobolDivisions.IDENTIFICATION:
                self.__save(self.__envi_file, content)
                self.__save(self.__data_file, content)
                self.__save(self.__proc_file, content)
            case CobolDivisions.ENVIRONMENT:
                self.__save(self.__envi_file, content)
            case CobolDivisions.DATA:
                self.__save(self.__data_file, content)
            case CobolDivisions.PROCEDURE:
                self.__save(self.__proc_file, content)

    def __split_by_divisions(self, context: ConverterContext):

        divisions = ["IDENTIFICATION DIVISION", "ENVIRONMENT DIVISION",
                     "DATA DIVISION", "PROCEDURE DIVISION"]

        with open(context.file_context.file, 'r', encoding='utf-8') as file:
            lines: list[str] = file.readlines()
            current_division: CobolDivisions = CobolDivisions.START
            for idx, line in enumerate(lines):

                if context.remove_comments is True and len(line) >= 7 and line[6] != "*":
                    found_division_start = next(
                        iter([i for i in divisions if i in line]), None)
                    match found_division_start:
                        case "IDENTIFICATION DIVISION":
                            current_division = CobolDivisions.IDENTIFICATION
                        case "ENVIRONMENT DIVISION":
                            current_division = CobolDivisions.ENVIRONMENT
                        case "DATA DIVISION":
                            current_division = CobolDivisions.DATA
                        case "PROCEDURE DIVISION":
                            current_division = CobolDivisions.PROCEDURE
                    print(idx, current_division)
                    self.__process_line(current_division, line)
                else:
                    if context.remove_comments is True:
                        print(idx, "comment line found, ignoring it")
                    else:
                        print(idx, "comment line found ")
            current_division = CobolDivisions.STOP

    def __split_by_sections(self, context: ConverterContext):
        section_idx = 0
        with open(self.__proc_file, 'r', encoding='utf-8') as file:
            lines: list[str] = file.readlines()
            current_section: str = "START"
            section_filename = ""
            header_text: str = ""
            for idx, line in enumerate(lines):
                if context.remove_comments is True and len(line) >= 7 and line[6] != "*":
                    if "SECTION." in line.upper():
                        current_section = line.upper().strip(" \t\n\r").replace("SECTION.", "").strip()
                        section_idx += 1
                        section_filename = os.path.join(
                            context.temporary_folder, f"procedure_section_{section_idx}_{current_section}.CBL")
                        context.file_context.converted_files.append(
                            section_filename)
                        self.__save(section_filename, header_text)
                        self.__save(section_filename, line)
                        print(f"Starting new section {current_section}")
                    else:
                        if current_section == "START":
                            header_text += line
                            print("File Header found")
                        else:
                            self.__save(section_filename, line)
                else:
                    print(idx, "comment line found")

# --------------------------------------------------
# Public methods
# --------------------------------------------------

    def split(self, context: ConverterContext):
        self.__envi_file = context.file_context.temporary_files[f"{CobolDivisions.ENVIRONMENT}"]
        self.__data_file = context.file_context.temporary_files[f"{CobolDivisions.DATA}"]
        self.__proc_file = context.file_context.temporary_files[f"{CobolDivisions.PROCEDURE}"]
        self.__split_by_divisions(context)
        self.__split_by_sections(context)
