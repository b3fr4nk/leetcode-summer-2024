def maxArea(height):
    # minimum of the two bars restricts size
    # two pointer problem
    left, right = 0, len(height) - 1
    max_area = 0

    # loop through all bars
    while left < right:
        length = right - left
        if height[left] < height[right]:
            x = height[left]
            left += 1
        else:
            x = height[right]
            right -= 1

        area = x * length
        if area > max_area:
            max_area = area
    return max_area
