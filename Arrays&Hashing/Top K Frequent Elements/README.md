**Top k Frequent elements**

<img width="461" alt="image" src="https://user-images.githubusercontent.com/25766765/208530434-623801a6-7769-4c09-b617-4e8c91da1e31.png">

Efficient approach notes:
1. Use bucket sort - The indexes are the frequency, and the value are the values that has this frequency.
2. Loop through the sorted dictionary from backwards and return the items until the length is equal to the k.

Runtime
94 ms
Beats
99.49%
Memory
18.7 MB
Beats
71.27%
