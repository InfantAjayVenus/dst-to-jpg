import os

def prober(source_path):
    path_list = []
    for root, dirs, files in os.walk(source_path):
        for file in files:
            if file.lower().endswith(".dst"):
                path_list.append(os.path.join(root, file))
    return path_list
