import sys

if __name__ == '__main__':
    input_file = open(sys.argv[1], "r")
    lines = input_file.readline()
    total = 0
    for i in range(int(lines)):
        total += int(input_file.readline())

    with open(sys.argv[2], 'w') as output_file:
        if total > 15:
            output_file.write(str(total))
        else:
            output_file.write("ERROR")