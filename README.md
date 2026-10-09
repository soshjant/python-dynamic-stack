# python-dynamic-stack

A simple, from-scratch implementation of the **Stack** data structure in Python, with **dynamic resizing** (the stack grows automatically when it is full) and a built-in **operation log** that records what was done to the stack.

## What is a Stack?

A stack is a linear data structure that follows the **LIFO** principle (*Last In, First Out*): the last item you add is the first one you remove. Think of a stack of plates: you can only add or remove from the top.

## Features

- `push` - add an item to the top of the stack
- `pop` - remove and return the top item
- `peak` - view the top item without removing it
- `is_empty` - check if the stack has no items
- `show_size_top` - see how many slots are filled vs. empty
- `__len__` - use Python's built-in `len()` to get the number of items
- **Dynamic resizing** - the internal list doubles in size automatically when full, instead of rejecting new items
- **Logging** - every operation is recorded, and `show_log` returns the last 5 entries

## Installation

No dependencies needed, just Python 3. Clone the repo or copy `stack.py` into your project.

```bash
git clone https://github.com/soshjant/python-dynamic-stack.git
```

## Usage

```python
from stack import stack

s = stack(2)   # initial size 2 (default is 10)

s.push(10)
s.push(20)
s.push(30)     # stack is full -> it resizes automatically to 4

print(s.list, s.size)      # [10, 20, 30, None] 4
print(s.peak())            # 30
print(s.pop())             # 30
print(s.show_size_top())   # (2, 2)  -> 2 filled, 2 empty
print(len(s))              # 2
print(s.is_empty())        # False
```

## How dynamic resizing works

When you `push` an item and the stack is full, instead of stopping with an error, the stack:

1. Creates a new, larger internal list (double the current size).
2. Copies all existing items into the new list.
3. Replaces the old list with the new one.

```python
s = stack(1)   # starts tiny
for i in range(10):
    s.push(i)  # grows automatically: 1 -> 2 -> 4 -> 8 -> 16
print(s.size)  # 16
```

## Logging

Every operation adds an entry to `s.log`. Calling `show_log()` returns the **last 5 entries**.

```python
s = stack(2)
s.push(10)
s.push(20)
s.push(30)
print(s.peak())
print(s.pop())
print(s.show_log())
```

Output:

```
30
30
['resize: 2 -> 4', 'push: 30', 'peak: 30', 'pop: 30', 'show_log called']
```

Notes about the log:

- The full history is stored in `s.log` (a normal Python list). `show_log()` only returns the last 5 entries.
- `show_log()` also records itself, so its own entry appears in the result.
- Failed operations are logged too, for example `pop failed: stack is empty`.

## Class Reference

| Method | Description |
|---|---|
| `stack(size=10)` | Creates a new stack with an initial size (default: 10) |
| `push(x)` | Adds `x` to the top; resizes automatically if full |
| `pop()` | Removes and returns the top item; prints a message if empty |
| `peak()` | Returns the top item without removing it; prints a message if empty |
| `new_size(size2)` | Resizes the internal list to `size2` (used automatically by `push`) |
| `show_log()` | Returns the last 5 log entries |
| `show_size_top()` | Returns a tuple: `(filled_slots, empty_slots)` |
| `is_empty()` | Returns `True` if the stack has no items |
| `len(stack)` | Returns the number of items currently in the stack |

## Notes

- This project was built as a learning exercise to understand how data structures like `list` manage memory and resize dynamically under the hood.
- Popped items are not physically cleared from the internal list; only the `top` pointer moves. This is normal and doesn't cause any bugs.
- Read-only methods such as `len()`, `is_empty()` and `show_size_top()` are logged as well, so the last 5 log entries can fill up with them.

## License

Feel free to use, modify, and learn from this code.
