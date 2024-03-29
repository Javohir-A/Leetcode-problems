class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area_val = 0
        left = 0
        right = len(height) - 1

        while left < right:
            min_height = min(height[left], height[right])
            current_area = min_height * (right - left)
            max_area_val = max(max_area_val, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area_val