import re
import logging
from cifpy.utils import formula
from cifpy.utils.error_messages import GeneralError


def get_atom_type_from_label(site_label: str) -> str:
    """
    Return the element from the given label.
    """
    validated_label = formula.get_validated_formula_label(site_label)
    if not isinstance(validated_label, str):
        raise TypeError(GeneralError.INVALID_TYPE.value)
    if not validated_label:
        raise ValueError(GeneralError.EMPTY_STRING_INPUT.value)
    if not validated_label[0].isalpha():
        raise ValueError(GeneralError.NON_ALPHABETIC_START.value)

    logging.debug("This is a debug log.")
    parts = re.split(r"[()]", validated_label)
    for part in parts:
        # Attempt to extract the atom type
        match = re.search(r"([A-Z][a-z]*)", part)
        if match:
            return match.group(1)


def trim_remove_braket(value_string: str) -> float:
    """
    Remove parentheses from a value string and convert to float.
    """
    value_string = value_string.strip()

    return (
        float(value_string.split("(")[0])
        if "(" in value_string
        else float(value_string)
    )


def clean_parsed_formula(formula):
    """
    Remove "~", " ", and "'" characters from the parsed formula.
    """
    return formula.replace("~", "").replace(" ", "").replace("'", "")


def clean_parsed_structure(structure_type):
    """
    Split the parsed structure text and remove "~".
    """
    return structure_type.split(",")[0].replace("~", "")
