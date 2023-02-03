def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_len = len(matrix) -1
        for i in range(len(matrix)-1, matrix_len//2, -1):
            matrix[i], matrix[matrix_len - i] = matrix[matrix_len-i], matrix[i]

        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
