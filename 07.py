s = "leetcode"
wordDict = ["leet", "code"]

for i in range(len(wordDict)):
    s = s.replace(wordDict[i], "")
if s == "":
    print(True)
else:
    print(False)
