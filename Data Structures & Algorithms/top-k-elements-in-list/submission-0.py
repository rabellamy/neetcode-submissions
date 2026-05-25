class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1 & 2: Count the frequency of each element
        # Counter creates a dictionary of {element: frequency}
        count_map = Counter(nums)
        
        # Step 3: Sort the unique elements by their frequency in descending order
        # We use the keys of the dictionary and sort them based on their dictionary values
        sorted_elements = sorted(count_map.keys(), key=lambda x: count_map[x], reverse=True)
        
        # Step 4: Return the top k elements
        return sorted_elements[:k]