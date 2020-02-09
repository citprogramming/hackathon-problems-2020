import sys

if __name__ == '__main__':
    file = open(sys.argv[1], "r")

    first_problem = list(map(int ,file.readLine().split()))
    second_problem = list(map(int, file.readLine().split()))

    bob, alice = 0
    for i in range(3):
        if first_problem[i] < second_problem[i]:
            bob += 1
        elif first_problem[i] == second_problem[i]:
            continue
        else:
            alice += 2
    
    print(alice, "\t", bob)

