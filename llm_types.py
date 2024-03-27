"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python
from enum import Enum


class LlmTypes(Enum):
    """Enumeration for LLM Types"""
    LLAMA2 = 1
    OPENAI = 2
    MISTRAL = 3
    FALCON = 4
