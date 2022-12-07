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

    def get_size(self):
        if self.type == filetypes.file:
             return self.size
        else:
             return self.dir_size()

    def dir_size(self):
        size = 0
        for c in self.children:
            size += c.get_size()
        print(f"dir: {self.name} size: {size}")
        return size
        
with open(sys.argv[1]) as f:
    data = f.read()

root = File("/", filetypes.dir)
curdir = None
alldirs = [root]

def build_tree(data):
    datalines = data.split('\n')
    i = 0
    while i < len(datalines):
        line = datalines[i]
        parts = line.split(' ')
        if len(parts) < 2:
            break
        elif parts[1] == 'cd':
            i += 1
            print(line)
            if parts[2] == '/':
                curdir = root
                print(f"cd to {curdir}")
            elif parts[2] == '..':
                curdir = curdir.parent
                print(f".. to {curdir}")
            else:
                found = False
                print(parts[2])
                print(curdir)
                for item in curdir.children:
                    if item.type == filetypes.dir and item.name == parts[2]:
                        curdir = item
                        found = True
                        break
                if not found:
                    raise RuntimeError("Could not find " + parts[2])
        elif parts[1] == 'ls':
            i+=1
            while True:
                line = datalines[i]
                if line == "" or  line[0] == '$':
                    break
                size, name = line.split(" ")
                if size == 'dir':
                    newfile = File(name, filetypes.dir)
                    alldirs.append(newfile)
                else:
                    newfile = File(name, filetypes.file, int(size))
                print(f"adding {newfile} to {curdir}")
                newfile.parent = curdir
                curdir.children.append(newfile)
                i += 1
        else:
            raise RuntimeError("Unexpectd line: " + line)
                

build_tree(data)

def sizedir(dir):
    total_size = 0
    for child in dir.children:
        if child.type == filetypes.file:
            total_size += child.size
        else:
            total_size += sizedir(child)
    return total_size
dir_sizes = [d.dir_size() for d in alldirs]
smalldirs = [d.dir_size() for d in alldirs if d.dir_size() <= 100000]

def parse_tree():
    nodes = [root]
    dirs = {}
    proc = 0
    while len(nodes) > 0:
        proc +=1 
        cur = nodes.pop()
        dirs[cur.name] = cur.get_size()
        for child in cur.children:
            if child.type ==filetypes.dir:
                nodes.append(child)

    print(f"procs: {proc}")
    return dirs

dirs = parse_tree()

size = 0
for k,v  in dirs.items():
    if v <= 100000:
        print(f"      adding {k}")
        size += v
print(size)



def print_tree(depth, node):
    print (' '*depth +  '- ', end="")
    print(node,)
    for k in node.children:
        print_tree(depth+2, k)
#print_tree(0, root)    
print(sum(smalldirs))


#print(size)
submit(sum(smalldirs), "a", 7, 2022)
