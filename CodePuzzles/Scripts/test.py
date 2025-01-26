def convert(s: str, numRows: int) -> str:
  """
  Converts a string to a zigzag pattern.

  Args:
      s: The input string.
      numRows: The number of rows in the zigzag pattern.

  Returns:
      The converted string in the zigzag pattern.
  """
  if numRows == 1:
    return s

  rows = ["" for _ in range(numRows)] # [''] * numRows  # Initialize empty rows
  print(f"rows --> {rows}")
  cur_row, going_down = 0, False

  for char in s:
    rows[cur_row] += char
    print(f"rows --> {rows}")
    if cur_row == 0 or cur_row == numRows - 1: # First value or Last value 
      going_down = not going_down
    cur_row += 1 if going_down else -1
    print(f"    >> cur_row --> {cur_row}")

  return ''.join(rows)

# Example usage
s = "PAYPALISHIRING"
numRows = 4
result = convert(s, numRows)
print(result)