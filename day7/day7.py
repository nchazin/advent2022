import sys
import aocd
from enum import Enum


if len(sys.argv) > 2 and sys.argv[2] == "submit":
    SUBMIT = True
else:
    SUBMIT = False


class filetypes(Enum):
    dir = 0
    file = 1


def submit(val, part, day, year):
    if SUBMIT:
        aocd.submit(val, part=part, day=day, year=year)


class File:
    def __init__(self, name, type, size=None, parent=None):
        self.name = name
        self.type = type
        self.size = size
        self.parent = parent
        self.children = []

    def __repr__(self):
        return repr(str(self.type) + " " + self.name + " " + str(self.size))

    def get_size(self):
        if self.type == filetypes.file:
            return self.size
        else:
            return self.dir_size()

    def dir_size(self):
        size = 0
        for c in self.children:
            size += c.get_size()
        return size


with open(sys.argv[1]) as f:
    data = f.read()

root = File("/", filetypes.dir)
curdir = None
alldirs = [root]


def build_tree(data):
    datalines = data.split("\n")
    i = 0
    while i < len(datalines):
        line = datalines[i]
        parts = line.split(" ")
        if len(parts) < 2:
            break
        elif parts[1] == "cd":
            i += 1
            if parts[2] == "/":
                curdir = root
            elif parts[2] == "..":
                curdir = curdir.parent
            else:
                found = False
                for item in curdir.children:
                    if item.type == filetypes.dir and item.name == parts[2]:
                        curdir = item
                        found = True
                        break
                if not found:
                    raise RuntimeError("Could not find " + parts[2])
        elif parts[1] == "ls":
            i += 1
            while True:
                line = datalines[i]
                if line == "" or line[0] == "$":
                    break
                size, name = line.split(" ")
                if size == "dir":
                    newfile = File(name, filetypes.dir)
                    alldirs.append(newfile)
                else:
                    newfile = File(name, filetypes.file, int(size))
                newfile.parent = curdir
                curdir.children.append(newfile)
                i += 1
        else:
            raise RuntimeError("Unexpectd line: " + line)


build_tree(data)

dir_sizes = [d.dir_size() for d in alldirs]
smalldirs = [d.dir_size() for d in alldirs if d.dir_size() <= 100000]


submit(sum(smalldirs), "a", 7, 2022)

total_size = root.dir_size()
free_space = 70000000 - total_size
needed_space = 30000000

big_enough = [
    d.dir_size() for d in alldirs if free_space + d.dir_size() >= needed_space
]
big_enough.sort()
submit(big_enough[0], "b", 7, 2022)
