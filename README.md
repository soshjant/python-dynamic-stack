# python_dynamic_stack

A simple, from-scratch implementation of the **Stack** data structure in Python, with **dynamic resizing** — the stack automatically grows when it runs out of space, so you never have to worry about it being "full".

## What is a Stack?

A stack is a linear data structure that follows the **LIFO** principle (*Last In, First Out*): the last item you add is the first one you remove. Think of a stack of plates — you can only add or remove from the top.

## Features

- ✅ `push` — add an item to the top of the stack
- ✅ `pop` — remove and return the top item
- ✅ `peak` — view the top item without removing it
- ✅ `is_empty` — check if the stack has no items
- ✅ `show_size_top` — see how many slots are filled vs. empty
- ✅ `__len__` — use Python's built-in `len()` to get the number of items
- ✅ **Dynamic resizing** — the internal array doubles in size automatically when full, instead of raising an error

## Installation

No dependencies needed — just Python 3. Clone the repo or copy the `stack.py` file into your project.

```bash
git clone https://github.com/soshjant/python_dynamic_stack.git
```

## Usage

```python
from stack import stack

# Create a stack (starts with a small size, grows automatically)
s = stack(2)

# Add items
s.push(10)
s.push(20)
s.push(30)   # stack was full (size=2), it automatically resizes to 4

print(s.list)   # [10, 20, 30, None]
print(s.size)   # 4

# Check the top item without removing it
print(s.peak())   # 30

# Remove the top item
print(s.pop())    # 30

# Check how many slots are filled / empty
print(s.show_size_top())   # (2, 2)

# Check the number of items using len()
print(len(s))   # 2

# Check if the stack is empty
print(s.is_empty())   # False
```

## How dynamic resizing works

When you `push` an item and the stack is full, instead of stopping with an error, the stack:

1. Creates a new, larger internal list (double the current size).
2. Copies all existing items into the new list.
3. Replaces the old list with the new one.

This means you can start with a small stack (or no size at all) and keep pushing items — the stack will keep growing to fit your needs, just like Python's built-in `list`.

```python
s = stack(1)   # starts tiny
for i in range(10):
    s.push(i)   # keeps growing automatically: 1 → 2 → 4 → 8 → 16
print(s.size)   # 16
```

## Class Reference

| Method | Description |
|---|---|
| `stack(size)` | Creates a new stack with an initial size (default varies by version) |
| `push(x)` | Adds `x` to the top of the stack; resizes automatically if full |
| `pop()` | Removes and returns the top item; prints a message if empty |
| `peak()` | Returns the top item without removing it; prints a message if empty |
| `is_empty()` | Returns `True` if the stack has no items |
| `show_size_top()` | Returns a tuple: `(filled_slots, empty_slots)` |
| `len(stack)` | Returns the number of items currently in the stack |

## Notes

- This project was built as a learning exercise to understand how data structures like `list` manage memory and resize dynamically under the hood.
- Popped items are not physically cleared from the internal list; only the `top` pointer moves. This is normal and doesn't cause any bugs.

## License

Feel free to use, modify, and learn from this code.
