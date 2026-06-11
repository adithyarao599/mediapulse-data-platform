from datetime import datetime


def generate_version():

    return datetime.now().strftime("%Y%m%d%H%M%S")
