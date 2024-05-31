import pytest
import logging
from cifpy.utils.error_messages import GeneralError, StringParserError
from cifpy.utils.string_parser import (
    get_atom_type_from_label,
    get_string_to_formatted_float,
    trim_string,
    clean_parsed_structure,
)


@pytest.mark.parametrize(
    "site_label, expected",
    [
        ("Co4(2)", "Co"),
        ("FeIII", "Fe"),
        ("Fe(III)", "Fe"),
        ("Mg12", "Mg"),
        ("OI", "O"),
        ("O3", "O"),
        ("Co2", "Co"),
        ("Fe12k", "Fe"),
        ("Rh3A", "Rh"),
        ("Si3B", "Si"),
    ],
)
def test_get_atom_type(site_label, expected):
    assert get_atom_type_from_label(site_label) == expected


def test_get_atom_type_with_error():
    assert (
        get_atom_type_from_label("OI") != "H"
    ), StringParserError.INVALID_PARSED_ELEMENT.value

    with pytest.raises(ValueError) as e:
        get_atom_type_from_label("1Fe")
    assert str(e.value) == GeneralError.NON_ALPHABETIC_START.value

    with pytest.raises(ValueError) as e:
        get_atom_type_from_label("")
    assert str(e.value) == GeneralError.EMPTY_STRING_INPUT.value

    with pytest.raises(TypeError) as e:
        get_atom_type_from_label(123)
    assert str(e.value) == GeneralError.INVALID_TYPE.value


@pytest.mark.parametrize(
    "value_string, expected",
    [
        ("123(45)", 123),  # With parentheses
        (" 123 (45) ", 123),  # With parentheses and spaces
        ("67.89(12)", 67.89),  # Decimal number with parentheses
        ("45", 45.0),  # No parentheses
        ("100", 100.00),  # No parentheses, simple integer
        ("4500.00", 4500.00),  # No parentheses, decimal
        ("0(99)", 0),  # Zero with parentheses
        (
            "-123.456(789)",
            -123.456,
        ),  # Negative decimal with parentheses
    ],
)
def test_remove_string_braket(value_string, expected):
    assert get_string_to_formatted_float(value_string) == expected


@pytest.mark.parametrize(
    "value_string, expected",
    [
        ("U Rh In", "URhIn"),
        ("Er~11~ Co~4~ In~9~", "Er11Co4In9"),
        ("Er~8~ Co In~3~", "Er8CoIn3"),
    ],
)
def test_clean_parsed_formula(value_string, expected):
    assert trim_string(value_string) == expected


@pytest.mark.parametrize(
    "value_string, expected",
    [
        ("ZrNiAl,hP9,189", "ZrNiAl"),
        ("Pr~8~CoGa~3~,hP24,186", "Pr8CoGa3"),
        ("Nd~11~Pd~4~In~9~,oS48,65", "Nd11Pd4In9"),
    ],
)
def test_clean_parsed_structure(value_string, expected):
    assert clean_parsed_structure(value_string) == expected
