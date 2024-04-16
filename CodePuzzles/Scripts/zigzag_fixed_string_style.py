class Solution:
    def __init__(self):
        pass
    def convert(self, s: str, numRows: int) -> str:
        final_list = [""] * numRows # prepare empty list with fixed no of empty value place holders based on no. of rows count
        print(final_list)
        downwards_direction = False # Used to alter row index, as zig zag direction seems to move up->down->up->down so on...
        row_index = 0
        for index, val in enumerate(s): # iterate through list
            if numRows > 1:
                final_list[row_index] += val # assign value during iteration
                print(row_index, val, final_list)
                if row_index == 0: # if on top of the column, then direction -> downwards, index increases
                    downwards_direction = True
                elif row_index == numRows - 1: # if on bottom of the column, then direction -> upwards, index decreases
                    downwards_direction = False
                row_index += -1 if not downwards_direction else 1
            else:
                final_list.append(val)
                # print(index, val, final_list)
        final_str = "".join(final_list)
        print(final_str)
        return final_str

if __name__ == "__main__":
    # str_val = "PAYPALISHIRING"
    # str_val = "CARISREADY"
    str_val = "A"
    # rows_no = 3
    rows_no = 1
    # rows_no = 2
    s = Solution()
    s.convert(s=str_val, numRows=rows_no)