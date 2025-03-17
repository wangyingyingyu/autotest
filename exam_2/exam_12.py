# 整型数组的最大连续子数组累加和
def max_sum(nums):
    if not nums:
        return 0

    max_sum = current_sum = nums[0]

    for num in nums[1:]:

        current_sum = max(num, current_sum + num)

        max_sum = max(max_sum, current_sum)

    return max_sum

# 示例
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_sum(nums)
print("最大连续子数组累加和:", result)  # 输出: 6