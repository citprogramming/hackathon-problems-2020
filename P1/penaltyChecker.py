

def calculate_penalty(n, grid):
    dimensions = n * n
    penalty = 0

    # check rows
    for y in range(dimensions):
        original = set()
        for x in range(dimensions):
            if original.__contains__(grid[x][y]):
                penalty += 1
            else:
                original.add(grid[x][y])

    # check columns
    for x in range(dimensions):
        original = set()
        for y in range(dimensions):
            if original.__contains__(grid[x][y]):
                penalty += 1
            else:
                original.add(grid[x][y])

    # check boxes
    top, left = 0, 0
    while top < dimensions:
        while left < dimensions:
            original = set()
            for x in range(n):
                for y in range(n):
                    if original.__contains__(grid[top + x][left + y]):
                        penalty += 1
                    else:
                        original.add(grid[top + x][left + y])
            left += n
        top += n

    return penalty


def main():
    n = int(input())
    dimensions = n * n
    grid = [[0 for i in range(dimensions)] for j in range(dimensions)]

    for i in range(dimensions):
        line = input().split()
        for j in range(dimensions):
            grid[i][j] = int(line[j])

    print("Penalty: " + str(calculate_penalty(n, grid)))


if __name__ == '__main__':
    main()
