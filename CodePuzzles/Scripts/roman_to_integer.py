class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000} # Lookup table
        print(s)
        print(roman_dict)
        prev_val = 0 # to check prev value
        final_val = 0 # to hold final computed integer
        for char in reversed(s): # goes from right -> left, as roman number computes in this direction
            curr_val = roman_dict[char] # get val
            print(f"    >> char --> {char}, prev_val --> {prev_val}, curr_val --> {curr_val}")
            if curr_val < prev_val: # if left value is less than right value then do substract
                final_val -= curr_val
                print(f"    >> if final_val --> {final_val}")
            else:
                final_val += curr_val # vice-versa
                print(f"    >> else final_val --> {final_val}")
            prev_val = curr_val # update current value to prev value
        print(f"final_val --> {final_val}")
        return final_val 

if __name__ == "__main__":
    # str_val = "MCMXCIV"
    str_val = "CIV"
    # str_val = "III"
    s = Solution()
    s.romanToInt(s=str_val)