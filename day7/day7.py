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



class File():
    def __init__(self, name, type, size=None, parent=None):
        self.name=name
        self.type=type
        self.size=size
        self.parent=parent
        self.children = []

    def __repr__(self):
        return repr(str(self.type) + " "+  self.name + " " +  str(self.size))

with open(sys.argv[1]) as f:
    data = f.read()

root = File("/", filetypes.dir)
curdir = None

def build_tree(data):
    datalines = data.split('\n')
    i = 0
    while i < len(datalines):
        line = datalines[i]
        if line == "":
            break
        if line == '$ cd /':
            curdir = root
            i = 1
            continue
        elif line == '$ ls':
            i += 1
            while i < len(datalines):
                line = datalines[i]
                if line == "" or  line[0] == '$':
                    break
                else:
                    size, name = line.split(" ")
                    if size == 'dir':
                        newfile = File(name, filetypes.dir)
                    else:
                        newfile = File(name, filetypes.file, int(size))
                    newfile.parent = curdir
                    print(f"adding {newfile} to {curdir}")
                    curdir.children.append(newfile)
                i += 1
        elif '$ cd' in line:
            print(f"cd {line}")
            _, _, dirname = line.split(" ")
            if dirname == '..':
                print(f"changing to {curdir.parent}")
                curdir = curdir.parent
            else:
                for f in curdir.children:
                    if f.name == dirname:
                        if f.type == filetypes.dir:
                            print(f"changing to {f}")
                            curdir = f
                            break
                        else:
                            print(f"{f} is not a directory!")
            i += 1
        else:
            print(f"how dfd we get here with{line}")


build_tree(data)


def sizedir(dir):
    total_size = 0
    for child in dir.children:
        if child.type == filetypes.file:
            total_size += child.size
        else:
            total_size += sizedir(child)
    return total_size

def parse_tree():
    nodes = [root]
    dirs = {}
    while len(nodes) > 0:
        cur = nodes.pop()
        dirs[cur.name] = sizedir(cur)
        for child in cur.children:
            if child.type ==filetypes.dir:
                nodes.append(child)

    return dirs
dirs = parse_tree()

size = 0
for k,v  in dirs.items():
    print(f"{k} {v}")
    if v <= 100000:
        print(f"      adding {v}")
        size += v
print(size)
size = 0
for k,v in dirs.items():
    if k != '/':
        size += v
print(size)

def print_tree(depth, node):
    print (' '*depth, '-', end="")
    print(node,)
    for k in node.children:
        if k.name == 'd':
            import pdb; pdb.set_trace()
        if k.type == filetypes.dir:
            print_tree(depth+1, k)
        else:
            print_tree(depth, k)

print_tree(0, root)    


submit(size, "a", 7, 2022)
