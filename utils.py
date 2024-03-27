"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python

import os


def load_file(source_file: str):
    """Load text from file"""
    with open(source_file, 'r', encoding='utf-8') as file:
        return file.read()


def save_to_file(content: str, file_name: str):
    """Save file to disk"""
    os.makedirs(os.path.dirname(file_name), exist_ok=True)
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(content)
        f.write('\n\n')
