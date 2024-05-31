import logging
from cifpy.utils.prompt import log_save_file_message


def log_save_file_message(caplog):
    file_type = "Histogram"
    file_path = "/path/to/histogram.png"

    # Check that the log message as expected
    with caplog.at_level(logging.INFO):
        log_save_file_message(file_type, file_path)
    assert f"{file_type} has been saved in {file_path}." == caplog.text
