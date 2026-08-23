class Solution:

    def encode(self, strs: List[str]) -> str:
        arrayofstrings = []

        for string in strs:
            arrayofstrings.append(str(len(string)))
            arrayofstrings.append("#")
            arrayofstrings.append(string)

        return "".join(arrayofstrings)

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            start = j + 1
            end = start + length

            strings.append(s[start:end])

            i = end

        return strings