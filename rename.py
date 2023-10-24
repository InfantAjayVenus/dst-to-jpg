import os

with open('paths.txt', 'r') as file:
    file_paths = file.read().splitlines()
    for path in file_paths:
        if path.endswith('.DST'):
            os.rename(path, path.replace('.DST', '.dst'))