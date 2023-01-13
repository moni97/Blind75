**Kth Smallest element in BST**

<img width="356" alt="image" src="https://user-images.githubusercontent.com/25766765/212238489-2dfd334f-2143-4674-9f3a-114fb79a1137.png">

<img width="362" alt="image" src="https://user-images.githubusercontent.com/25766765/212238505-74f6e68d-861e-4817-9b92-96ca37d023a6.png">

Notes:
1. For this case we need to traverse to the left most node, then look at the root node, then look at the right node of that root node. 
2. Traverse till the leftmose node and keep pushing in the stack.
3. Pop a node from the stack and store in current node, each time a node is popped increase the counter.
4. if count is equal to k then return that value
5. Else make the right node as the current node.

Runtime
58 ms
Beats
70.72%
Memory
18 MB
Beats
43.71%
