import pytest
from tests.helpers import logger
from tests.helpers import api_request_helper
import config


def pytest_runtest_setup():
    logger.init_logg()
    api_request_helper.init_http_client()


def pytest_runtest_teardown():
    logger.logg("\nteardown extras go here\n")

