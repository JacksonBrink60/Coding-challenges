nums = [2,7,11,15]
target = 9

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if i == j:
            pass
        elif nums[i] + nums[j] == target:
            print(f"[{i}, {j}]")
            break
    if i == j:
            pass
    elif nums[i] + nums[j] == target:
        break