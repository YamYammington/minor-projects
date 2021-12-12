import os
import random
from PIL import Image
import os.path

extensions = ["png", "jpg", "jpeg", "jfif", "gif"]

# If your folders and/or subfolders contain files that are NOT: png, jpg, jpeg, jfif or gif: please include those extensions in the variable below.
badextensions = []
folder = os.getcwd()


def main():
    try:
        file1 = random.choice(os.listdir(folder))
        path_to_file = os.path.join(folder, file1)

        if file1.endswith(tuple(extensions)):
            print(f"\n{path_to_file}")
            im1 = Image.open(path_to_file)
            im1.show()
        elif file1.endswith(tuple(badextensions)):
            main()
        else:
            file2 = random.choice(os.listdir(path_to_file))
            path_to_file = os.path.join(path_to_file, file2)

            if path_to_file.endswith(tuple(extensions)):
                print(f"\n{path_to_file}")
                im2 = Image.open(path_to_file)
                im2.show()
            elif path_to_file.endswith(tuple(badextensions)):
                main()
            else:
                file3 = random.choice(os.listdir(path_to_file))
                path_to_file = os.path.join(path_to_file, file3)

                if path_to_file.endswith(tuple(extensions)):
                    print(f"\n{path_to_file}")
                    im3 = Image.open(path_to_file)
                    im3.show()
                elif path_to_file.endswith(tuple(badextensions)):
                    main()
                else:

                    file4 = random.choice(os.listdir(path_to_file))
                    path_to_file = os.path.join(path_to_file, file4)

                    if path_to_file.endswith(tuple(extensions)):
                        print(f"\n{path_to_file}")
                        im4 = Image.open(path_to_file)
                        im4.show()
                    elif path_to_file.endswith(tuple(badextensions)):
                        main()
                    else:
                        file5 = random.choice(os.listdir(path_to_file))
                        path_to_file = os.path.join(path_to_file, file5)

                        if path_to_file.endswith(tuple(extensions)):
                            print(f"\n{path_to_file}")
                            im5 = Image.open(path_to_file)
                            im5.show()
                        elif path_to_file.endswith(tuple(badextensions)):
                            main()
                        else:
                            print("ERROR: An image was not found. Retrying...")
                            main()
    except PermissionError:
        print("ERROR: Access denied. Retrying...")
        main()
    except Exception:
        print("ERROR: Unsupported file type. Retrying...")
        main()

main()
