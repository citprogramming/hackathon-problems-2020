import sys

if __name__ == '__main__':
    first_problem = list(map(int ,sys.stdin.readLine().split()))
    second_problem = list(map(int, sys.stdin.readLine().split()))

    bob, alice = 0
    for i in range(3):
        if first_problem[i] < second_problem[i]:
            bob += 1
        elif first_problem[i] == second_problem[i]:
            continue
        else:
            alice += 2
    
    print(alice, "\t", bob)

