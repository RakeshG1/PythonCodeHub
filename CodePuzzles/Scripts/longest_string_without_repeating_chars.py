class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        print(f"string --> {s}")
        # Intermediate substring characters as list
        inter_temp_space = []
        # Final substring characters as list
        final_char_collection = []
        # Final substring characters as string
        final_string = ""
        # Iterating through each character
        for index, char in enumerate(s):
            print(f"char --> {char}")
            # If current char not already exists in current temp substring list
            if char not in inter_temp_space:
                inter_temp_space.append(char)
                print(f"    >> if : inter_temp_space --> {inter_temp_space}, final_char_collection --> {final_char_collection}")
                # If current temp substring list is greater than last final substring list  
                if (len(inter_temp_space) > len(final_char_collection)):
                    final_char_collection = inter_temp_space[:]
                    final_string = "".join(inter_temp_space)
                print(f"    >> if : final_string --> {final_string}")
            else: # If current char already exists in current temp substring list
                print(f"    >> else : inter_temp_space --> {inter_temp_space}, final_char_collection --> {final_char_collection}")
                # If current temp substring list is greater than last final substring list  
                if (len(inter_temp_space) > len(final_char_collection)):
                    final_char_collection = inter_temp_space[:] # This avoid automatic reflection of inter_temp_space computation on final_char_collection
                    final_string = "".join(inter_temp_space)
                    inter_temp_space = []
                    inter_temp_space.append(char)
                    print(f"    >> final_string --> {final_string}")
                else: # If current temp substring list is less than last final substring list  
                    duplicate_index = inter_temp_space.index(char)
                    print(f"    >> else: before duplicate index finding : inter_temp_space --> {inter_temp_space}, duplicate_index --> {duplicate_index}")
                    if duplicate_index == 0: # remove first element if it matches 1st element in list, as we can't remove intermediate substring
                        print(f"inter_temp_space[1:] --> {inter_temp_space[1:]}")
                        inter_temp_space = inter_temp_space[1:]
                    elif duplicate_index > 0 and duplicate_index < len(inter_temp_space)-1: # if it matches 2nd element / in elements before last element in list, then keep after duplicated index
                        print(f"inter_temp_space[len(inter_temp_space)-1] --> {inter_temp_space[len(inter_temp_space)-1]}")
                        # inter_temp_space = [inter_temp_space[len(inter_temp_space)-1]]
                        inter_temp_space = inter_temp_space[duplicate_index+1:]
                    elif duplicate_index == len(inter_temp_space) - 1: # if it macthes last element, then make fresh
                        inter_temp_space = []
                    inter_temp_space.append(char)
                    print(f"    >> else: after duplicate index finding and append : inter_temp_space --> {inter_temp_space}")
        print(f"final_string --> {final_string}")
        return len(final_string)


if __name__ == "__main__":
    s = Solution()
    # s.lengthOfLongestSubstring("abcabcacadfg")
    # s.lengthOfLongestSubstring("abcabcbab")
    # s.lengthOfLongestSubstring("abcabcbb")
    # s.lengthOfLongestSubstring("bbbbb")
    # s.lengthOfLongestSubstring("pwwkew")
    s.lengthOfLongestSubstring("wobgrovw")