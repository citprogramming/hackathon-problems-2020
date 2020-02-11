import sys

if __name__ == '__main__':
    file = open(sys.argv[1], "r")
    data = []
    lines = file.readline()
    test = int(file.readline())
    data.append(str(test))
    for i in range(test):
        for j in range(2):
            data.append(file.readline().rstrip())
    
    s = '-'.join(data)
    f = open("output.txt", "a")
    f.write(s)
    print(len(s))
#     s = s.split("-")
#    # print(s[0:len(s)-1])