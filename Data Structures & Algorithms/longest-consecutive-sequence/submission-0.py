class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            # start counting if num-1 doesn't exist, which means it's the start of a new sequence
            if num - 1 not in nums_set:
                current = num
                length = 1

                # start counting how many numbers are consecutive
                while current + 1 in nums_set:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest