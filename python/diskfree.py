from os import path
from shutil import disk_usage

print([i / 1000000 for i in disk_usage(path.realpath('c:/'))])
print([i / 1000000 for i in disk_usage(path.realpath('d:/'))])
print([i / 1000000 for i in disk_usage(path.realpath('/'))])
print(disk_usage(path.realpath('/')))
