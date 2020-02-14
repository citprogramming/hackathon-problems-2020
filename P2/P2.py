import sys

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    lines = int(file.readline())
    first_problem = list(map(int ,file.readline().split()))
    second_problem = list(map(int, file.readline().split()))

    bob = 0
    alice = 0
    for i in range(3):
        if first_problem[i] < second_problem[i]:
            bob += 1
        elif first_problem[i] == second_problem[i]:
            continue
        else:
            alice += 1
    
    print(alice, " ", bob,"\n")

