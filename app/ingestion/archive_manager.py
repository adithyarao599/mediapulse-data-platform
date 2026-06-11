import shutil


def archive_file(source, destination):

    shutil.copy2(source, destination)
