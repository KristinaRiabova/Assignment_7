import argparse

parser = argparse.ArgumentParser(description="Hello")
parser.add_argument("path", type=str)
parser.add_argument("medals",type=str, default="-medals")
parser.add_argument("country", type=str)
parser.add_argument("year", type=int)
parser.add_argument("-output", type=str)
args = parser.parse_args()
path = args.path
country = args.country
year = args.year
print(args)

with open(path, 'r') as file:
    lines = file.readlines()
    lineForSplit = ""
    newLines = []
    for i in range(0, len(lines)):
        lineForSplit = str(lines[i].split('\t'))
        newLines.append(lineForSplit)

print(newLines)

