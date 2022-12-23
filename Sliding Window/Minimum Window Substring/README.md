**Minimum Window Substring**

<img width="404" alt="image" src="https://user-images.githubusercontent.com/25766765/209254967-22774d41-d161-4585-9f39-ba7532ca24a7.png">

Notes:
1. Loop through the letters in the string, and alter the left and right pointer accordingly.
2. maintain two dicts, one for the current count, other for the actual count expected.
3. Instead of checking each char in the dict, have a variable to maintain how the coniditon is met.
4. When the condition is met, then move the left pointer and update the window accordingly

Runtime
431 ms
Beats
38.56%
Memory
14.8 MB
Beats
38.44%
