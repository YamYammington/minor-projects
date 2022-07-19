import os, sys


def main(folder):
    ext = []

    for file in os.listdir(folder):
        extension = file.split(".")[-1]
        if extension not in ext:
            print(extension)
            ext.append(extension)

    print(ext)


if __name__ == "__main__":
    try:
        location = argv[1]
    except IndexError:
        location = os.getcwd()
        
    main(location)
    input("Press Enter to continue...")
