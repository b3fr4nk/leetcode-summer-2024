def removeElement(nums, val):
    end = len(nums) - 1
    current = end

    while current >= 0:
        if nums[current] == val:
            nums[current], nums[end] = nums[end], nums[current]
            end -= 1
        current -= 1
    return end+1
