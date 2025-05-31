from typing import Tuple


class Solution:

    def is_at_end(self, curr_pos: int, s: str) -> bool:
        return (curr_pos + 1) >= len(s)

    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        i = 0
        max = len(s) - 1
        final_numerals = []

        while i <= max:
            curr_char = s[i]

            if curr_char == "I":
                if not self.is_at_end(i, s):
                    next_char = s[i + 1]
                    if next_char == "V" or next_char == "X":
                        curr_char_val = roman_numerals.get(curr_char)
                        next_char_val = roman_numerals.get(next_char)
                        final_numerals.append(abs(curr_char_val - next_char_val))
                        i += 2
                        continue
                    else:
                        final_numerals.append(roman_numerals.get(s[i]))
                else:
                    final_numerals.append(roman_numerals.get(s[i]))
            elif curr_char == "X":
                if not self.is_at_end(i, s):
                    next_char = s[i + 1]
                    if next_char == "L" or next_char == "C":
                        curr_char_val = roman_numerals.get(curr_char)
                        next_char_val = roman_numerals.get(next_char)
                        final_numerals.append(abs(curr_char_val - next_char_val))
                        i += 2
                        continue
                    else:
                        final_numerals.append(roman_numerals.get(s[i]))
                else:
                    final_numerals.append(roman_numerals.get(s[i]))
            elif curr_char == "C":
                if not self.is_at_end(i, s):
                    next_char = s[i + 1]
                    if next_char == "D" or next_char == "M":
                        curr_char_val = roman_numerals.get(curr_char)
                        next_char_val = roman_numerals.get(next_char)
                        final_numerals.append(abs(curr_char_val - next_char_val))
                        i += 2
                        continue
                    else:
                        final_numerals.append(roman_numerals.get(s[i]))
                else:
                    final_numerals.append(roman_numerals.get(s[i]))
            else:
                final_numerals.append(roman_numerals.get(curr_char))
            i += 1
        print(sum(final_numerals))


if __name__ == "__main__":
    solution = Solution()
    solution.romanToInt("DCXXI")