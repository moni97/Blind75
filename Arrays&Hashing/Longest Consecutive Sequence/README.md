**Longest Consecutive Sequence**
<img width="448" alt="image" src="https://user-images.githubusercontent.com/25766765/208737044-b2beb3e1-c263-42a0-9a97-8913469c64f7.png">

Notes:
1. Use sets, as lookup/inset/delete all are O(1)
2. Start counting the length when the element is the starting of the sequence.
3. Loop until the current element plus the current legnth is in the nums(which is a set).


Runtime
2121 ms
Beats
38.32%
Memory
28.9 MB
Beats
86.52%
