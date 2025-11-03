import math
s = "A"
numRows = 1

cy = 2*numRows-2
rows = []
for j in range(0, numRows):
    rows.append("")
for i in range(len(s)):
    if cy == 0:
        pos = 0
    else:
        pos = i%cy
    row = pos if pos < numRows else cy -pos
    rows[row] += s[i]
print(''.join(rows))