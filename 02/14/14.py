import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename) as f:
    for line in f.read().split('\n')[0:n]:
        print(line)