import sys

if __name__ == '__main__':
    input_file = open(sys.argv[1], "r")

    result = ""
    for _ in range(int(input_file.readline())):
        l, a, b = map(int, input_file.readline().split())
        s = input_file.readline()
        i = 1
        cost = [float('inf')] * (l + 1)
        cost[0] = 0
        k = 0
        while i <= l:
            j = max(i, k)
            while j <= l and (s[i-1:j] in s[:i-1]):
                j += 1

            if j-1 != i:
                cost[j-1] = min(cost[i-1] + b, cost[j-1])
                k = j
            cost[i] = min(cost[i-1] + a, cost[i])
            i += 1

        result += str(cost[-1]) + "\n"

    with open(sys.argv[2], 'w') as output_file:
        output_file.write(result)
