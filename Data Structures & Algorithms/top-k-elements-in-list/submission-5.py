class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        # freq = list of list.
        # start from 0 to n + 1, where n = size of list + 1
        freq = [[] for i in range(len(nums) + 1)]

        # Get hash map where key = num, value = frequency
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        print(count)

        for n, c in count.items():
            freq[c].append(n)
        print(freq)

        ans = []
        for i in range(len(freq)-1, 0, -1):
            if not(freq[i] == []):
                for j in freq[i]:
                    ans.append(j)
            if len(ans) >= k:
                break
        print(ans)

        return ans