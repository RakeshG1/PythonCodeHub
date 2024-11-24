# List Comprehensions
# -------------------
squares = [x**2 for x in range(10)]
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary Comprehensions
# -------------------------
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Set Comprehensions
# ------------------
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares) # {0, 1, 4}

# Multiple Variable Assignments
# -----------------------------
a, b, c = 10, 20, 30
print(a, b, c) # 10 20 30

# Ternary Conditionals: if else
# -----------------------------
type = "Even" if 4 % 2 == 0 else "Odd"
print(type) # Even

# Zip for pairing
# ---------------
fruits = ["Apple", "Banana"]
prices = [100, 200]
pairs = zip(fruits, prices)
print(list(pairs)) # [('Apple', 100), ('Banana', 200)]

# Enumerate for indexing
# ----------------------
for idx, fruit in enumerate(["Apple", "Banana"]):
    print(idx, fruit)
# 0 Apple
# 1 Banana    

# Unpacking Iterables
# -------------------
a, *b, c = [1, 2, 3, 4, 5, 6]
print(a, b, c) # 1 [2, 3, 4, 5] 6

# Default Dictionary & Counter
# ----------------------------
from collections import Counter, defaultdict
count = defaultdict(int)
count["apple"] += 1
print(count) # defaultdict(<class 'int'>, {'apple': 1})
print(count["banana"]) # 0
word = "Hello World"
counter = Counter(word)
print(counter) # Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})

# String Concatenation with join
# ------------------------------
words = ["Hello", "World", "Python"]
sentence = " ".join(words)
print(sentence) # Hello World Python

# Multi Arguments [*args, *kargs]
# -------------------------------
def args_all(*args, **kwargs):
    print(args, kwargs)
args_all(10, 20, 30, a=100, b=200) # (10, 20, 30) {'a': 100, 'b': 200}

# F-strings for formating
# -----------------------
fruit = "Apple"
price = 100
print(f"The price of {fruit} is {price}") # The price of Apple is 100

# Lambda Functions
# ----------------
result = lambda x: x*2
print(result(10)) # 20

# Chained Comparison 
# ------------------
x = 10
print(0 < x < 100) # True

# any and all for Logical Operations
# ----------------------------------
numbers = [2, 4, 6]
print(all(x % 2 == 0 for x in numbers)) # True
print(any(x > 5 for x in numbers)) # True