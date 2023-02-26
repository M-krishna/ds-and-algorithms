"""
Design an algorithm to encode and decode strings
Sample I/P: ["hey", "there", "krishna!"]
O/P: ["hey", "there", "krishna!"]
One way of encoding: "hey:;there:;krishna!"
NOTE: The class should not maintain any state variables. The encoded string will be passed over the network.
"""

class Solution:
    def encode(self, strs) -> str:
        result_str = ''
        for s in strs:
            n = str(len(s)) + '#' + s
            result_str += n
        return result_str

    def decode(self, encoded_str) -> list[str]:
        decoded_list = []
        i = 0
        while i < len(encoded_str):
            num = int(encoded_str[i])
            s = ""
            for j in range(i+2, ((i+2) + num)):
                s += encoded_str[j]
            decoded_list.append(s)
            i = j + 1
        return decoded_list


if __name__ == '__main__':
    s = Solution()
    encoded_string = s.encode(["#lint", "co#de", "love23#4", "y#ou#"])
    print(encoded_string)
    decoded_string_list = s.decode(encoded_string)
    print(decoded_string_list)