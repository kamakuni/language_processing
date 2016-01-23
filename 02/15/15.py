import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename,'r') as f:
    for (_,line) in zip(range(0,n),reversed(f.read().split('\n'))):
        print(line)