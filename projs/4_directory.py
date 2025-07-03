import os
import argparse

def files_extensions(dir):
    if not os.path.isdir(dir):
        print("directory doesn't exist")
        return

    try:
        for el in os.listdir(dir):
            path = os.path.join(dir, el)
            if os.path.isfile(path):
                name, extension = os.path.splitext(el)
                ext = extension.lower().strip(".") or "no_extension"
                target_dir = os.path.join(dir, ext)

                try:
                    if not os.path.exists(target_dir):
                        os.mkdir(target_dir)
                except:
                    print(f"error creating directory")

                new_path = os.path.join(target_dir, el)
                try:
                    os.rename(path, new_path)
                except:
                    print(f"error moving file")
    except:
        print(f"directory components doesn't accessible")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="input directory name")
    args = parser.parse_args()

    files_extensions(args.directory)

if __name__ == "__main__":
    main()