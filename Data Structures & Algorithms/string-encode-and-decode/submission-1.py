class Solution:
    def encode(self, strs: List[str]) -> str:
        print("Original:", strs)

        encode_str = ''
        for s in strs:
            encode_str += str(len(s)) + '#' + s
        print("Encode:", encode_str)

        return encode_str

    def decode(self, s: str) -> List[str]:
        decode_str = list()
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decode_str.append(s[j+1:j+1+length])
            i = j + 1 + length

        print("Decode:", decode_str)

        return decode_str