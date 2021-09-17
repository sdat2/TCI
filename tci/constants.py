# import os/pathlib to manipulate file names.
import os
import pathlib


# Note: constants should be UPPER_CASE
constants_path = pathlib.Path(os.path.realpath(__file__))
SRC_PATH = pathlib.Path(os.path.dirname(constants_path))
PROJECT_PATH = pathlib.Path(os.path.dirname(SRC_PATH))
EXAMPLE_PATH = os.path.join(SRC_PATH, "example")
EXAMPLE_PREFIX = "10000101.atmos_month."


def example_file_path(variable: str) -> str:
    """
    Get example file path

    Args:
        variable (str): Example variable.

    Returns:
        str: Get the string.
    """
    return os.path.join(EXAMPLE_PATH, EXAMPLE_PATH + variable + ".nc")
