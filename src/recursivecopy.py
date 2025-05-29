import os
import shutil

def recursive_copy(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for filename in os.listdir(source):
        from_path = os.path.join(source, filename)
        dest_path = os.path.join(destination, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_copy(from_path, dest_path)