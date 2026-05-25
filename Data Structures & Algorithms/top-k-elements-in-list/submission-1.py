class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequencies of each element
        count_map = Counter(nums)
        
        # Step 2: Create a bucket array where the index represents the frequency.
        # The maximum possible frequency is the length of the input array `nums`.
        # We need size len(nums) + 1 to safely accommodate 0-indexing up to len(nums).
        buckets = [[] for _ in range(len(nums) + 1)]
        
        # Step 3: Populate the buckets. 
        # Elements with frequency `freq` are appended to buckets[freq]
        for num, freq in count_map.items():
            buckets[freq].append(num)
            
        # Step 4: Gather the top k frequent elements by iterating backwards.
        result = []
        # Iterate from the highest possible frequency down to 1
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                # Once we have gathered exactly k elements, we can return immediately
                if len(result) == k:
                    return result
                    
        return result