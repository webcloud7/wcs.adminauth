import base64
import os.path


def b64encode(source):
    source = source.encode("utf-8")
    return base64.b64encode(source).decode("utf-8")


def get_data(filename):
    """Return content from a file in the test data folder"""
    filename = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(filename) as file_:
        return file_.read()
