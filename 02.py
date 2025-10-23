j = int(input())
k = ""
for i in str(j)[::-1]:
    k = k + f"{i}"

if k == str(j):
    print(True)
else:
    print(False)