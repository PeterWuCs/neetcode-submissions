class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for a in strs:
            result += str(len(a)) + '#' + a
        # print(result)
        return result

    def decode(self, s: str) -> List[str]:
        result = [ ]

        number_start_index = 0

        i = 0
        while i < len(s):
            if s[i] == '#':
                sub = s[ number_start_index: i ]
                print("number_start_index", number_start_index, "i", i)
                print(sub)
                length = int(sub)
                result.append(s[ i + 1: i + 1 + length])

                number_start_index = i + length + 1
                i = number_start_index + 1

                continue

            i += 1

        return result

