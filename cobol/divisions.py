"""
Author: Vivek Sarin
License: MIT
"""
#! /usr/bin/env python

from enum import Enum


class CobolDivisions(Enum):
    """Enum for Cobol Divisions"""
    START = 0
    IDENTIFICATION = 1
    ENVIRONMENT = 2
    DATA = 3
    PROCEDURE = 4
    STOP = 5
