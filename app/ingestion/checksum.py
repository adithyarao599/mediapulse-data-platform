import hashlib


def generate_checksum(file_path):

    with open(file_path, "rb") as file:

        content = file.read()

    return hashlib.md5(content).hexdigest()
