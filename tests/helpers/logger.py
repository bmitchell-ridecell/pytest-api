import logging
import http.client as http_client

def logg(output):
    print(output)

def init_logg():
    logging.basicConfig()
    # Enable HTTP debugging
    http_client.HTTPConnection.debuglevel = 1

    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True
    print("\n---- initialized logger for module tests ----\n")
