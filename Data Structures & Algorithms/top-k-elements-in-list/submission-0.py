class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
            
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num in seen:
            freq[seen[num]].append(num)
        
        result = []
        i = len(freq)-1

        while len(result)<k:
            for num in freq[i]:
                if len(result)>=k:
                    return result
                else:
                    result.append(num)
            i-=1
        
        return result