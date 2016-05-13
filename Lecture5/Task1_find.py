import os
import sys


def find_file(dirs, file_name):
    for root, directory, files in os.walk(dirs):
        print(root, '-----', directory, '-----', files)
        if file_name in files:
            print(os.path.join(root, file_name))


if len(sys.argv) < 3:
    print("Not enough params")
else:
    find_file(dirs=sys.argv[1], file_name=sys.argv[2])


# python Task1_find.py /Lecture5 Tests.py
