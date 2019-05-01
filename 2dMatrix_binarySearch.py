g = 5
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

def searchMatrix( matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    t = 0
    for row in matrix: 
        last = len(row)-1-t
        while target > row[t] and last < target:
            print row[t],"t"
            if row[t] == target:
                print row[t], "x"
                return True
            else:
                t += 1    
    print "false"
    return False
searchMatrix(m,g)

def searchMatrix2( matrix, target):
    j = -1
    for row in matrix:
        while j + len(row) and row[j] > target:
            j -= 1
        if row[j] == target:
            print "true"
            return True
    print "false"
    return False
searchMatrix2(m,g)


         




