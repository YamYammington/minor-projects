from os import listdir
from os.path import join, isdir
from random import choice
from subprocess import call
from sys import argv

FAIL = '\033[91m'
ENDC = '\033[0m'
OKCYAN = '\033[96m'
extensions = ("png", "jpg", "jpeg", "jfif", "gif", "PNG", "JPG", "JPEG", "JFIF", "GIF")


def search_file(filepath):
    chosen_file = join(filepath, choice(listdir(filepath)))
    match chosen_file:
        case chosen_file if isdir(chosen_file):
            search_file(chosen_file)
        case chosen_file if chosen_file.endswith(data.extensions):
            print(f"{data.ENDC}{chosen_file}")
            call([chosen_file], shell=True)
        case _:
            search_file(filepath)


if __name__ == "__main__":
    folder = argv[1]
    search_file(folder)
