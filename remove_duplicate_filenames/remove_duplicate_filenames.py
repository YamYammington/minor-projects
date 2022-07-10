import os, sys

# fill these variables in or use command line arguments
folder1 = ""
folder2 = ""

OKCYAN = '\033[96m'
FAIL = '\033[91m'
ENDC = '\033[0m'
count = 0
errors = 0
os.system('color')


def main(f1, f2):
    global count, errors
    for file1 in os.listdir(f1):
        print(f"{OKCYAN}Handling file {file1}{ENDC}")
        for file2 in os.listdir(f2):
            if file1 == file2:
                path1 = os.path.join(f1, file1)
                count += 1
                try:
                    os.remove(path1)
                except OSError as e:
                    errors += 1
                    print(f"{FAIL}Could not remove {path1}; {e}{ENDC}")
                else:
                    print(f"Removed {path1}")
                break
        else:
            print("No duplicate.")


if __name__ == "__main__":
    if folder1 and folder2:
        main(folder1, folder2)
    else:
        main(sys.argv[1], sys.argv[2])
    input(f"Press Enter to exit. Removed {count} files, with {errors} errors.")
