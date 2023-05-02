def twoSum(nums, target):
    n = len(nums)
    l = 0
    r = n-1
    nums.sort()

    while l<r:
        if nums[l] + nums[r] > target:
            r = r-1
        elif nums[l] + nums[r] < target:
            l = l+1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3], target=14))


def twoSum(nums, target):
    l, r = 0, len(nums)-1
    nums.sort()
    while l<r:
        if nums[l] + nums[r] > target:
            r = r-1
        elif nums[l] + nums[r] < target:
            l = l+1
        elif nums[l] + nums[r] == target:
            return True
    return False

print(twoSum(nums=[4,1,9,7,5,3], target=14))


