class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
            use a hash map of frequencies
            then create a list of buckets then iterate past 0s.
        '''

        freq = {}
        for num in nums:
            # nums = [1,2,2,3,3,3]
            # mapping: num -> frequency
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        '''
        {
        1 : 1
        2 : 1
        3 : 3
        }
        '''

        arr = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            arr[count].append(num)

        # so then at this point, iterate backwards from arr until u exhaust k

        ans = []
        for i in range(len(arr) - 1, -1, -1):
            if not arr[i]:
                continue

            for num in arr[i]:
                ans.append(num)
                k -= 1

                if k == 0:
                    return ans
