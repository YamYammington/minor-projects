import os, sys


def main(folder):
    ext = []

    for file in os.listdir():
        extension = file.split(".")[-1]
        if extension not in ext:
            print(extension)
            ext.append(extension)

    print(ext)


if __name__ == "__main__":
    location = argv[1] if argv[1] else os.getcwd()
    main(location)
    input("Press Enter to continue...")
