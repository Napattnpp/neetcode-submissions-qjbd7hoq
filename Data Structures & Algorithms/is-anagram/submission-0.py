class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()

        ls = len(s)
        if ls != len(t):
            return False

        for i in range(ls):
            # Frequency map of s str
            if s[i] in dict_s:
                dict_s[s[i]] += 1
            else:
                dict_s[s[i]] = 1
        
            # Frequency map of t str
            if t[i] in dict_t:
                dict_t[t[i]] += 1
            else:
                dict_t[t[i]] = 1


        return dict_s == dict_t

        