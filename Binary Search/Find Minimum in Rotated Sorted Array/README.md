**Find minimum in rotated sorted array**

<img width="451" alt="image" src="https://user-images.githubusercontent.com/25766765/209406219-76a675d9-7552-4b82-8239-d056bd1da3b7.png">

Notes:
1. check if the mid is in left r right sorted array.
2. if in right sorted array search to the left of mid, as the numbers to the right are bigger than the mid
3. if in the left sorted array search to the right
4. store the mid as the minium number
5. if the left and right pointer are in a sorted array then return leftmost value.


Runtime
38 ms
Beats
96.85%
Memory
14.2 MB
Beats
23.21%
