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

    for i in range(s):
        start_row = commands[i][0]
        end_row = commands[i][0] + commands[i][2]
        start_column = commands[i][1]
        end_column = commands[i][1] + commands[i][2]
        row_track = start_row -1
        selected_troops = []
        
        # Extracting the troops from the command
        for _ in range((end_row-start_row)+1):
            selected = []
            col_track = start_column - 1
            for _ in range((end_column-start_column)+1):
                if len(selected) == ((end_column-start_column)+1):
                    break
                else:
                    selected.append(troops[row_track][col_track])
                col_track += 1 
            selected_troops.append(selected)
            row_track += 1

        #Rotating the data by 90 degrees
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
    lines = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    s = int(sys.stdin.readline())
    commands = []

    for _ in range(s):
        commands.append(list(map(int, sys.stdin.readline().rstrip().split())))

    important_knights_num = int(sys.stdin.readline())
    knights = []
    for _ in range(important_knights_num):
        knights.append(int(sys.stdin.readline()))
    result = kingRichardKnights(n, s, commands, knights)
    for i in result:
        print(' '.join(list(map(str, i))))
