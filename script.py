import os
from prober import prober
from converter import write_png, add_bg

source_path = os.path.join(os.getcwd(), 'source-files')

file_paths = prober(source_path)

print(f"Found {len(file_paths)} files")

with open('paths.txt', 'w') as file:
    file.write('\n'.join(file_paths))

for index in range(len(file_paths)):
    path = file_paths[index]
    dest_file = path.replace('.dst', '.png').replace('source-files', 'dest-files')
    print(f'{str(index + 1).rjust(len(str(len(file_paths))), "0")}/{len(file_paths)}: Coverting {path} to {dest_file}')
    write_png(path, dest_file)
    add_bg(dest_file)