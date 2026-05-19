class Solution:
    # Move Zeroes using Two Pointers
    def move_zeroes_two_pointers(self, nums):
        left = 0  # Pointer for placing non-zero elements

        # Iterate with right pointer
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap elements if right pointer finds a non-zero
                nums[left], nums[right] = nums[right], nums[left]
                left += 1  # Move left pointer forward