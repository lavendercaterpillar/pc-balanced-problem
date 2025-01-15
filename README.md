# Balanced Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in writing a function that determines if a sequence of numbers contains two pairs (a, b) and (c, d) such that a+b = c+d.

Our function should accept a list of integers.

For example, if

```py
numbers = [3, 10, 4, 5, 2, 14]
```

then 3 + 4 = 2 + 5. Therefore our function should return `{3, 2, 4, 5}` as a set.

Note that each element of the input list will be unique. Each input will have at most one solution.

## Examples

### Example 1

```py
numbers = [3, 10, 4, 5, 2, 14]
balanced(numbers)
```

Produces

```py
{3, 2, 4, 5}
```

### Example 2

```py
numbers = [60, 0, 10, -35, 90]
balanced(numbers)
```

Produces

```py
set()  # Recall that {} would be an empty dict
```

### Example 3

```py
numbers = []
balanced(numbers)
```

Produces

```py
set()
```
