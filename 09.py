s = "()"
def main():
    val = {")": "(", "]": "[", "}": "{"}
    temp = []
    for i in s:
        if i in val.values():
            temp.append(i)
        elif i in val:
            if not temp or val[i] != temp.pop():
                return False
    return not temp

if __name__ == "__main__":
    print(main())
        