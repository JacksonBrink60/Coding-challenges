"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

· eg. in the example below, the coordinates of the two red lines are (1,0) to (1, 8) and (8,0) and (8,7)

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]

Output: 49

Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]

Output: 1

Example 3:

Input: height = [6,4,8,9,0,2,7,9,1]

Output: 42


Hint 1

If you simulate the problem, it will be O(n^2) which is not efficient.

---

Hint 2

Try to use two-pointers. Set one pointer to the left and one to the right of the array. Always move the pointer that points to the lower line.

---

Hint 3

How can you calculate the amount of water at each step?"""
import array
itered = -1
itered2 = -1
highest = 0
arrg = array.array("i", [6,4,8,9,0,2,7,9,1])
for i in arrg.tolist():
    itered += 1
    itered2 = -1
    for n in arrg.tolist():
        itered2 += 1
        if itered2>itered:
            dis = itered2-itered
        elif itered>itered2:
            dis = itered-itered2
        else:
            dis = 0
        if i < n:
            if i*dis > highest:
                highest = i*dis
        elif n < i:
            if n*dis > highest:
                highest = n*dis
        else:
            if i*dis > highest:
                highest = i*dis
print(highest)