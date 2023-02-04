**Counting Bits**

<img width="432" alt="image" src="https://user-images.githubusercontent.com/25766765/216789957-fda3bd56-8cd9-4614-851e-77d98bafbdd4.png">

Notes:
1. Find the pattern with the bit representation for every number.
2. The pattern repeats for every significant number, which will be 2, 4, 6, .... etc
3. Change the offset whenever a significant number is reached.
4. For every number in the loop add 1 + the the current i - the offset
5. return the dp array.

Runtime
79 ms
Beats
92.43%
Memory
20.8 MB
Beats
71.82%
