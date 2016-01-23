import sys

n = int(sys.argv[1])
filename = sys.argv[2]

with open(filename,'r') as f:
    lines = f.read().split('\n');
    for line in lines[len(lines) - (n + 1):len(lines)]:
        print(line)