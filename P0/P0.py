import sys

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    lines = file.readline()
    sum = 0
    for i in range(int(lines)):
        sum += int(file.readline())
    if sum > 15:
        print(sum)
    else:
        print("ERROR")