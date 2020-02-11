import sys

if __name__ == '__main__':
    lines = sys.stdin.readline()
    sum = 0
    for i in range(int(lines)):
        sum += int(sys.stdin.readline())
    if sum > 15:
        print(sum)
    else:
        print("ERROR")