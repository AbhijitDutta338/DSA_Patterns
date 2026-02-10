class Solution:
    def max_area_two_pointers(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        # Move pointers toward each other
        while left < right:
            width = right - left  # Distance between lines
            min_height = min(height[left], height[right])  # Compute height
            area = min_height * width  # Compute water contained

            max_area = max(max_area, area)  # Update max water

            # Move the pointer pointing to the shorter height
            if height[left] < height[right]:
                left += 1  # Move left pointer forward
            else:
                right -= 1  # Move right pointer backward

        return max_area