class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = dict()

        for num in nums:
            if num not in frequencyMap:
                frequencyMap[num] = 0
            frequencyMap[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in frequencyMap:
            freq = frequencyMap[num]
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                if len(result) == k:
                    return result

        return result