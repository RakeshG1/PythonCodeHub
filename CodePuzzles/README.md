## Search Elements in a List

### Brute Force Approach

- Logic: It uses nested loops to iterate through all possible pairs of elements in the list.
    - The outer loop iterates through each element (i).
    - The inner loop iterates through the remaining elements (j), starting from i+1 to avoid duplicate pairs.
- Time Complexity: O(n^2). The nested loops lead to n * (n-1) / 2 comparisons in the worst case, which grows quadratically with the input size (n).
- Advantage: Simple to understand and implement.
- Disadvantage: Inefficient for large datasets due to the high number of comparisons.

```python
  for i in range(n):
    for j in range(i + 1, n):
        if data[i] == data[j]:
```

- O(n^2) time complexity is not ideal for very large datasets, it can be acceptable for smaller lists. There might be more efficient algorithms for specific problems depending on the desired outcome.

- Two iterations => n * (n-1) => n^2 - n => O(n^2)
    - n -> 1st iteration
    - n-1 -> 2nd iteration
    - -n neglected in Time complexity
    - Time complexity notated with O

### Hash Table Approach

- Logic: It utilizes a hash table (implemented as a set in Python) to store elements encountered so far. Sets offer fast average lookup time (O(1)).
    - It iterates through each element (num) in the list.
    - It calculates the complement (the value needed to reach the target_sum when added to num).
    - It checks if the complement already exists in the seen set.
        - If it does, it means a pair that adds up to the target_sum is found.
        - If it doesn't, it adds the current element (num) to the seen set.
- Time Complexity: O(n) on average. The dominant operation is iterating through the list (n times) and performing constant-time lookups in the set.
- Advantage: Significantly faster than brute force for larger datasets due to the efficient lookups in the hash table.
- Disadvantage: Uses additional space to store the hash table (set).

```python
  seen = set()  # Create a set to store seen elements
  for num in data:
    complement = target_sum - num
    if complement in seen:
        found
    else
        add to seen
```

- One iteration => O(n)