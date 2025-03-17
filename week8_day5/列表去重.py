def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1

nums = [1, 1, 2, 2, 3, 4, 4, 5]
new_length = remove_duplicates(nums)

print(f"处理后的数组: {nums[:new_length]}")
