import sys

if __name__ == '__main__':
    input_file = open(sys.argv[1], 'r')
    first_problem = list(map(int, input_file.readline().split()))
    second_problem = list(map(int, input_file.readline().split()))

    bob = 0
    alice = 0
    for i in range(3):
        if first_problem[i] < second_problem[i]:
            bob += 1
        elif first_problem[i] == second_problem[i]:
            continue
        else:
            alice += 1

    with open(sys.argv[2], 'w') as output_file:
        output_file.write(str(alice) + " " + str(bob) + "\n")

