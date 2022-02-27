# Jake Million
# 2/27/22

# creating an empty list
nums = []
s = 0
# for loop to store user's nums into list and adding them to s
for i in range(0, 20):
    n = int(input("Enter a number: "))
    nums.append(n)
    s += n
# printing the list
print(nums)

# find lowest
low = nums[0]
for a in range(0, 20):
    if low > nums[a]:
        low = nums[a]
print("The lowest number entered was ", low)
# finding highest value in nums
high = nums[0]
for b in range(0, 20):
    if high < nums[b]:
        high = nums[b]
print("The highest number entered was ", high)

# print sum
print("The sum of all numbers entered: ", s)
# print average
print("Average of all numbers entered: ", s/20)
