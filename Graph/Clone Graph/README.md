**Clone Graph**

<img width="350" alt="image" src="https://user-images.githubusercontent.com/25766765/212962526-46effed3-cb77-4ad0-8e5f-6e07b2b228bc.png">

<img width="340" alt="image" src="https://user-images.githubusercontent.com/25766765/212962602-84dce1fe-27ba-44ef-b304-c4723cf304f8.png">

<img width="355" alt="image" src="https://user-images.githubusercontent.com/25766765/212962663-d85bf369-e7d7-49f4-ba25-620c8157be1e.png">

Notes:
1. DFS in every node.
2. Starting from the initial node, call dfs in the neighbors of the node.
3. When the DFS is complete for a node, return a new node created.
4. Have a map that maps for old node to new node.
5. If there is a node return the node and dont do dfs.

Runtime
26 ms
Beats
99.87%
Memory
14.4 MB
Beats
24.15%
