class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = dict()

        for s in strs:
            # Find the key of this current `string`
            key = [0] * 26
            for c in s:
                key[ord(c) - ord('a')] += 1
            key = tuple(key)

            # Add unique key
            if key not in table:
                table[key] = []

            # Add this current `string` to the responding key
            table[key].append(s)
        return [val for val in table.values()]