**Set MAtrix zeroes**

<img width="433" alt="image" src="https://user-images.githubusercontent.com/25766765/216745899-2454705b-1d06-411f-8705-7b2ebfcdd72e.png">

<img width="373" alt="image" src="https://user-images.githubusercontent.com/25766765/216745904-1cd9bc32-d1fc-4e72-af17-3ac0661d2612.png">

Notes:
1. Set the first element in row or column to 0 when there is a zero.
2. go throught the matrix and when there is a 0 in the column make every element in that column 0.
3. Go through the rows, if there is a 0 make that row zero.
4. Edge case will be for the first row in matrix. Use a separate flag to indicate if the first row should be made 0.

Runtime
142 ms
Beats
45.57%
Memory
14.7 MB
Beats
96.31%
