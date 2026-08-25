class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n - 1, 0, -1):
            answer[i-1] = nums[i] * answer[i]

        temp = 1 
        for i in range(0, n):
            answer[i] = temp * answer[i]
            temp = temp * nums[i]

        return answer
   
