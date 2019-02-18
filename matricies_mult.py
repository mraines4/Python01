ma1 = [
    [1,2,3],
    [3,4,5],
    [5,7,8],
    [2,6,7],
    [2,2,2]
]
ma2 = [
    [87,3,-7,4],
    [3,8,8,0],
    [9,0,-.3,1]
]

def multiply_matrix(matrix1,matrix2):
    new_matrix = []
    for i in range(len(matrix1)):   #for each row in matrix 1
        inside_array = []
        #get each value
        rowlen = len(matrix1[0])    #number columns in 1st matrix
        row2len = len(matrix2[0])      #number columns in  2nd matrix

        x=0
        for j in range(row2len):        #for each columns in matrix 2
            for k in range(rowlen):
                # print("%d * %d" % (matrix1[i][k],matrix2[k][j]))
                x += (matrix1[i][k] * matrix2[k][j])
            inside_array.append(x)
            x=0

            # print(inside_array)
        new_matrix.append(inside_array)
    return new_matrix
	
print(multiply_matrix(ma1,ma2))