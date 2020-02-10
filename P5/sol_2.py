'''
Author: Stephen Driscoll
'''
import sys
def read_input(file_name):
    lines = int(sys.stdin.readline())
    num_tests = int(sys.stdin.readline())

    grids = list()
    patterns = list()
    for i in range(num_tests):
        grids.append(read_grid(sys.stdin.readline()))
        patterns.append(read_grid(sys.stdin.readline()))

    return grids, patterns


def read_grid(sys.stdin.readline()):
    line = sys.stdin.readline().readline()
    splits = line.split(' ')
    rows = int(splits[0])
    columns = int(splits[1])

    grid = list()
    for i in range(rows):
        grid.append(list())
        line = sys.stdin.readline().readline()
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


def write_output(file_name, results):
    with open(file_name, 'w') as file_out:
        for i in range(len(results)):
            if results[i]:
                file_out.write("YES\n")
            else:
                file_out.write("NO\n")


def main():
    grids, patterns = read_input("input03.txt")

    results = list()
    for i in range(len(patterns)):
        results.append(solve(grids[i], patterns[i]))

    write_output("output.txt", results)


if __name__ == "__main__":
    main()