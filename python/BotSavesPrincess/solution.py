#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    
    for i, line in enumerate(grid):
            if 'm' in line:
                bot = (line.index('m') + 1, i)
            if 'p' in line:
                princess = (line.index('p') + 1, i)

    import operator
    difference = tuple(map(operator.sub, princess, bot))
    x_steps = ['RIGHT' if difference[0] > 0 else 'LEFT'] * abs(difference[0])
    y_steps = ['UP' if difference[1] < 0 else 'DOWN'] * abs(difference[1])
    for i in x_steps:
        print(i)
    for i in y_steps:
        print(i)

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)