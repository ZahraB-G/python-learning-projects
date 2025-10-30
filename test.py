nums = [3,3]
target = 6
result = []
for i in range(len(nums)):
    goal = target - nums[i]
    if goal in nums[i+1:]:
        result.append(nums.index(goal,i+1))
        result.append(i)

result.sort()     
print(result)
