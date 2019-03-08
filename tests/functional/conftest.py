from loggings import logger
from apis import api_request_helper


def pytest_runtest_setup():
    logger.init_logg()
    api_request_helper.init_http_client()


def pytest_runtest_teardown():
    logger.logg("\nteardown extras go here\n")

