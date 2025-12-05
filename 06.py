s = "LVIII"
j = 0
lis = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
for i in range(len(s)):
    if lis[s[i]] > lis[s[i-1]] and i > 0:
        j += lis[s[i]] - lis[s[i-1]]
    elif i+1 <= len(s)-1 and lis[s[i]] < lis[s[i+1]]:
        pass
    else:
        j += lis[s[i]]
print(j)