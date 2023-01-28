**Maximum Product Subarray**

<img width="419" alt="image" src="https://user-images.githubusercontent.com/25766765/215239497-5e406ebc-01ee-4651-b147-c769945f1b7f.png">

Notes:
1. Negative numbers in this problem will make it tricky.
2. Have a currMin, currMax, multiply it with the curr number.
3. Having 0 in the array is the edge case.
4. Store the maximum at each loop in res.
5. The main idea behind having the currMin, currMax is that a negative number might be in the end and it can change the entire dynamic of th array.



Runtime
89 ms
Beats
71.47%
Memory
14.4 MB
Beats
74.94%
