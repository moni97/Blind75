Word break 

<img width="352" alt="image" src="https://user-images.githubusercontent.com/25766765/214508851-0f7623f8-fd55-4fb9-9242-7443f1c6156c.png">

<img width="350" alt="image" src="https://user-images.githubusercontent.com/25766765/214508899-2cdf2725-f185-49cf-b7bb-9a66f64e44e4.png">

Notes:
1. Comparing each word, with the starting position in the string is the right approach.
2. Try to think that in the DP approach.
3. Bottom up approach, where each char is compared to each word in the dict, if the word exists make the dp array true. 
4. Next loop will be the previous value in the index, the word that was last matched is not skipped.

Runtime
59 ms
Beats
36.61%
Memory
13.8 MB
Beats
93.42%
