**Sum of two integers**

<img width="439" alt="image" src="https://user-images.githubusercontent.com/25766765/216796870-23007180-b10d-4f66-9d8e-1695ffa9d87f.png">

Notes:
1. XOR of two numbers gives the sum, but without carry.
2. And of two numbers will give us the places where there should be a carry.
3. Shift the and of two numbers and again xor.
4. Do this in a while loop, until the second number is not zero. Put the carry shifted value and second number and xored value in the first number

Runtime
0 ms
Beats
100%
Memory
38.8 MB
Beats
94.15%
