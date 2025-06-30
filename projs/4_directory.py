import os
import argparse

def files_extensions(dir):
    if not os.path.isdir(dir):
        return "directory doesn't exist"

    for el in os.listdir(dir):
        path = os.path.join(dir, el)
        if os.path.isfile(path):
            name, extension = os.path.splitext(el)
            ext = extension.lower().strip(".")
            target_dir = os.path.join(dir, ext)
            if not os.path.exists(target_dir):
                os.mkdir(target_dir)

            new_path = os.path.join(target_dir, el)
            os.rename(path, new_path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="input directory name")
    args = parser.parse_args()
    files_extensions(args.directory)

if __name__ == "__main__":
    main()
