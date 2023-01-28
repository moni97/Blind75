**Longest Increasing Subsequence**

<img width="446" alt="image" src="https://user-images.githubusercontent.com/25766765/215237795-8bc76168-8bad-409a-a436-d75d3f7dc802.png">

Notes:
1. Start from the end.
2. Have a dp array, last num length is 1.
3. Loop backwards, for every index there is one more loop to loop from the current index until the end of nums
4. Each index in the second loop if the num is less the curr then increase the length of the subsequence

Runtime
5622 ms
Beats
16.11%
Memory
14.2 MB
Beats
45.13%
