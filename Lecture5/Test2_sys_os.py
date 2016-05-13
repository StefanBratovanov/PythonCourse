import sys
import os

# print(sys.platform)
# print(sys.argv)

# print(os.access('.../.../..', os.W_OK))
# print(os.path.dirname('../Lecture5/Tests.py'))
# print(os.path.basename('/Lecture5/Tests.py'))
# print(os.path.exists('../Lecture5/Tests.py'))

for root, dirs, files in os.walk('../Lecture5'):
    print(root, '-----', dirs, '-----', files)
    for fn in files:
        print(os.path.join(root, fn))
