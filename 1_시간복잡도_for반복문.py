def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return True
            
    return False

print(twoSum(nums=[4,1,9,7,5,3,16], target=14))

##################################################

def TwoSum(nums,target):
    for i in range(len(nums)-1): # 012345
        for j in range(i+1,len(nums)): #123456
            if nums[i] + nums[j] == target:
                return True
    else:
        return False

nums = [4,1,9,7,5,3,16]
target = 14

TwoSum(nums,target)