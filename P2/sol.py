import sys
import math

def kingRichardKnights(n, s, commands, knights):
    troops = []
    track = 0
    for _ in range(n):
        tmp = []
        for _ in range(n):
            tmp.append(int(track))
            track += 1
        troops.append(tmp)
    print(troops)
    print(type(troops[0][1]))
    for i in range(s):
        print(commands)
        start_row = commands[i][0]
        end_row = commands[i][0] + commands[i][2]
        start_column = commands[i][1]
        end_column = commands[i][1] + commands[i][2]
        row_track = start_row -1
        selected_troops = []
        for _ in range((end_row-start_row)+1):
            selected = []
            col_track = start_column - 1
            for _ in range((end_column-start_column)+1):
                # print(row_track)
                # print(troops[row_track][col_track])
                if len(selected) == ((end_column-start_column)+1):
                    break
                else:
                    print(row_track, col_track)
                    #print(troops[row_track][col_track])
                    selected.append(troops[row_track][col_track])
                col_track += 1 
            print(selected)
            selected_troops.append(selected)
            row_track += 1
        #Rotating the data by 90 degrees
        print(selected_troops)
        tmp = list(map(list, zip(*selected_troops)))
        for i in range(len(selected)):
            selected_troops[i] = tmp[i][::-1]
        #Replacing the selected troops in the parent troops
        row_track = start_row -1
        for i in range((end_row-start_row)+1):
            col_track = start_column - 1
            for j in range((end_column-start_column)+1):
                troops[row_track][col_track] = selected_troops[i][j]
                col_track += 1
            row_track += 1

    #Getting the location of important troops
    coordinates = []
    for knight in knights:
        for i in range(n):
            for j in range(n):
                if(troops[i][j] == knight):
                    coordinates.append([i+1, j+1])
    return coordinates

if __name__=='__main__':
    file = open(sys.argv[1], "r")
    n = int(file.readline())
    s = int(file.readline())
    commands = []

    for _ in range(s):
        commands.append(list(map(int, file.readline().rstrip().split())))

    important_knights_num = int(file.readline())
    knights = []
    for _ in range(important_knights_num):
        knights.append(int(file.readline()))
    result = kingRichardKnights(n, s, commands, knights)
    print(result)