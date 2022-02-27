# Jake Million
# 2/27/22

# import random
import random

# create  list
nums = []

# putting values into list
for i in range(0, 99):
    n = random.randint(0, 20)
    nums.append(n)

# find second highest
h = nums[0]
for b in range(0, 99):
    if h < nums[b]:
        h = nums[b]
sh = nums[0]
for c in nums:
    if sh < h and sh > nums[c+1]:
        sh = nums[c]
print("The second highest number: ", sh)

# delete repeating values
for e in nums:
    repeat = nums[e]
    for d in nums:
        if repeat == nums[d]:
            nums.remove(nums[d])
print(nums)