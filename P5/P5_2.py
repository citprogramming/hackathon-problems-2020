"""
Author: Stephen Driscoll
"""
import sys


def read_grid(input_file):
    line = input_file.readline()
    splits = line.split(' ')
    rows = int(splits[0])
    columns = int(splits[1])

    grid = list()
    for i in range(rows):
        grid.append(list())
        line = input_file.readline()
        for j in range(columns):
            grid[i].append(line[j])

    return grid


def solve(larger, pattern):
    for a in range(len(larger)):
        for b in range(len(larger[0])):
            found = True
            for c in range(len(pattern)):
                for d in range(len(pattern[0])):
                    if len(larger) <= (a + c) or len(larger[0]) <= (b + d) or larger[a + c][b + d] != pattern[c][d]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return True

    return False


def main():
    with open(sys.argv[1], 'r') as input_file:
        num_tests = int(input_file.readline())

        grids, patterns = list(), list()
        for i in range(num_tests):
            grids.append(read_grid(input_file))
            patterns.append(read_grid(input_file))

    results = list()
    for i in range(len(patterns)):
        results.append(solve(grids[i], patterns[i]))

    with open(sys.argv[2], 'w') as output_file:
        for i in range(len(results)):
            if results[i]:
                output_file.write("YES\n")
            else:
                output_file.write("NO\n")

    main()
