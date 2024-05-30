# error_messages.py
from enum import Enum


class GeneralError(Enum):
    INVALID_TYPE = "The formula/label must be a string."
    EMPTY_STRING_INPUT = "The formula/label cannot be empty."
    NON_ALPHABETIC_START = (
        "The first character must be alphabetic after trimming."
    )
    NON_MATCHING_ELEMENT = (
        "No matching element was parsed from the site label."
    )
    INVALID_CIF_BLOCK = "The CIF block should not be None."


class StringParserError(Enum):
    INVALID_PARSED_ELEMENT = (
        "The element was not correctly parsed from the site label."
    )


class CifParserError(Enum):
    INVALID_LOOP_TAGS = (
        "The returned loop tags do not match the expected tags."
    )
    WRONG_LOOP_VALUE = "Wrong number of values in loop _atom_site_*"
    MISSING_COORDINATES = (
        "Missing fractional coordinates in the loop values."
    )


class FileError(Enum):
    FILE_NOT_FOUND = "The file at {file_path} was not found."
    FILE_IS_EMPTY = "The file at {file_path} is empty."
