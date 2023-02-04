def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowZero = False
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    if i > 0:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    else:
                        rowZero = True
        for i in range(1, r):
            for j in range(1, c):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for i in range(r):
                matrix[i][0] = 0
        if rowZero:
            for i in range(c):
                matrix[0][i] = 0
