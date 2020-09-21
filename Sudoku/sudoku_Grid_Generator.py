from random import shuffle
from random import randint
import time

grid=[
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0]
]

N1=[0,1,2,9,10,11,18,19,20]
N2=[3,4,5,12,13,14,21,22,23]
N3=[6,7,8,15,16,17,24,25,26]
N4=[27,28,29,36,37,38,45,46,47]
N5=[30,31,32,39,40,41,48,49,50]
N6=[33,34,35,42,43,44,51,52,53]
N7=[54,55,56,63,64,65,72,73,74]
N8=[57,58,59,66,67,68,75,76,77]
N9=[60,61,62,69,70,71,78,79,80]

numbers=[1,2,3,4,5,6,7,8,9]

#prints the board with the 81 numbers
def Print_Grid(g):
    for i in range(len(g)):
        if i % 3 == 0 and i != 0:
            print('------------------------------')
        for j in range(len(g[0])):
            if j % 3 ==0 and j!=0:
                print('|',end=" ")
            if j==8:
                print(g[i][j])
            else:
                print(str(g[i][j])+' ',end=' ')

#processing time
def printTime():
    CPUtime=time.process_time()
    print(CPUtime,'seconds')

def Grid_Checker(grid):
    for row in range(0,9):
        for col in range(0,9):
            if grid[row][col]==0:
                return(False)
    return(True)

def Grid_Generator(grid):
    for i in range(81):
        row=i//9
        col=i%9
        squares[1]=grid[0][0:3]+grid[1][0:3]+grid[2][0:3]
        squares[2]=grid[0][3:6]+grid[1][3:6]+grid[2][3:6]
        squares[3]=grid[0][6:9]+grid[1][6:9]+grid[2][6:9]
        squares[4]=grid[3][0:3]+grid[4][0:3]+grid[5][0:3]
        squares[5]=grid[3][3:6]+grid[4][3:6]+grid[5][3:6]
        squares[6]=grid[3][6:9]+grid[4][6:9]+grid[5][6:9]
        squares[7]=grid[6][0:3]+grid[7][0:3]+grid[8][0:3]
        squares[8]=grid[6][3:6]+grid[7][3:6]+grid[8][3:6]
        squares[9]=grid[6][6:9]+grid[7][6:9]+grid[8][6:9]
        if grid[row][col]==0:
            shuffle(numbers)
            for n in numbers:
                if not (n in grid[row]):
                        if not (n in [grid[0][col],grid[1][col],grid[2][col],grid[3][col],grid[4][col],grid[5][col],grid[6][col],grid[7][col],grid[8][col]]):
                            square=None
                            if i in N1:
                                square=squares[1]
                            if i in N2:
                                square=squares[2]
                            if i in N3:
                                square=squares[3]
                            if i in N4:
                                square=squares[4]
                            if i in N5:
                                square=squares[5]
                            if i in N6:
                                square=squares[6]
                            if i in N7:
                                square=squares[7]
                            if i in N8:
                                square=squares[8]
                            if i in N9:
                                square=squares[9]
                            if not (n in square):
                                grid[row][col]=n
                                if Grid_Checker(grid):
                                    return(True)
                                else:
                                    if Grid_Generator(grid):
                                        return(True)
            break
    grid[row][col]=0


squares=dict()
Grid_Generator(grid)
if Grid_Checker(grid) is False:
    Grid_Generator(grid)
Print_Grid(grid)
printTime()
