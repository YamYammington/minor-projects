from os import listdir, getcwd
from os.path import join, isdir
from random import choice
from subprocess import call
from sys import argv

extensions = ("png", "jpg", "jpeg", "jfif", "gif")


def search_file(filepath):
    chosen_file = join(filepath, choice(listdir(filepath))).lower()
    if isdir(chosen_file):
        search_file(chosen_file)
    elif chosen_file.endswith(extensions):
        print(chosen_file)
        call([chosen_file], shell=True)
   else:
        search_file(filepath)


if __name__ == "__main__":
    try:
        folder = argv[1]
    except IndexError:
        folder = getcwd()
        
    search_file(folder)
