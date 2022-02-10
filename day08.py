# ------------------------------------------------------------------------------
# ********************************* { DAY 04 } *********************************
# ------------------------------------------------------------------------------


# QUESTION: Bot saves the princess-2

def findPrincess(n, grid):
    for row in range(n):
        for column in range(n):
            if (grid[row][column] == 'p'):
                return (row, column)
            
def nextMove(n,r,c,grid):
    pCoords = findPrincess(n, grid)
    pRow = pCoords[0];
    pCol = pCoords[1];
    
    # Move vertical until we are on her row
    if (pRow != r):
        return "UP" if pRow < r else "DOWN"
        
    # Move horizontal until we are on her column
    if (pCol != c):
        return "RIGHT" if pCol > c else "LEFT"


def matchingStrings(str_ , query_):
    count = 0
    res = []
    for i in query_:
        ls = [s for s in str_ if s == i ]
        res.append(len(ls))
        


    return res
    # from collections import Counter # module to count the values
    # #write your code here
    # store = Counter(str_)  ----> thid will return a dictionary
    # ans = []
    # for q in query_:
    #    ans.append(store[q])
    # return store

print(matchingStrings(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))