# Ellipsis as --> Placeholder
# ---------------------------
def compute_cost():
    ...

# Ellipsis as --> Argument
# ------------------------
def get_fruit_details(name="Apple", quantity=...):
    if quantity == ...:
        quantity = 0
    print(f"Fruit name: {name} and its quantity: {quantity}")

get_fruit_details("Banana", 1) # Fruit name: Banana and its quantity: 1
get_fruit_details("Orange",...) # Fruit name: Orange and its quantity: 0
get_fruit_details("Mango", None) # Fruit name: Mango and its quantity: None

# Ellipsis with --> TypeHint: List with unknown size
# --------------------------------------------------
from typing import List
fruits: List[str, ...] = ["Apple", "Banana", "Orange", "Mango", ...] # Fruits List: ['Apple', 'Banana', 'Orange', 'Mango', Ellipsis]
print(f"Fruits List: {fruits}")
fruits: List[str, 2] = ["Apple", "Banana", "Orange", "Mango"] # TypeError: Too many arguments for typing.List; actual 2, expected 1
print(f"Fruits List: {fruits}")
fruits: List[str, ...] = ["Apple", "Banana", "Orange", "Mango"] # Fruits List: ['Apple', 'Banana', 'Orange', 'Mango']
print(f"Fruits List: {fruits}")

# Ellipsis with --> Abstraction
# -----------------------------
from typing import Callable
# Callable[..., int] in Python is a type hint that indicates a callable object (like a function) 
# that can accept any number and type of arguments (denoted by the ellipsis ...) and will return an float
def compute_data(func: Callable[..., float], *args) -> float: # This abstract function can be modified to include logging, error handling, or to apply multiple funs
    return func(*args)

def multiply_numbers(a: float, b: float) -> float:
    return a * b

result = compute_data(multiply_numbers, 1.2, 2.2)
print(result) # 2.64


