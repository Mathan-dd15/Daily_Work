# find 1st two max number

nums = [3,99,10,5,3,67]

sorted_num = nums.sort(reverse=True)
print(nums[:2])
#----------
max1 = max2 = float('-inf')

for num in nums:
    if num >max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print(max1,max2)

# sort the numbers

n = len(nums)

for i in range(n):
    for j in range(0, n-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]

print(nums)
