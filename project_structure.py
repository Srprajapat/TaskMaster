import os

def print_directory_structure(start_path, prefix=''):
    for item in sorted(os.listdir(start_path)):
        path = os.path.join(start_path, item)
        print(prefix + '|-- ' + item)
        if os.path.isdir(path):
            print_directory_structure(path, prefix + '|   ')

# Usage
print_directory_structure('WORKSPACE')
