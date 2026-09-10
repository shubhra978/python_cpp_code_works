def triangular_sum(nums):
    while len(nums) > 1:
        new_nums = []
        for i in range(len(nums) - 1):
            new_nums.append((nums[i] + nums[i+1]) % 10)
        nums = new_nums
    return nums[0]
