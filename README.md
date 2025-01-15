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

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if there's an empty list?

A: See the test cases for the expected behavior.

#### Q: Can the integers be negative?

A: Yes, negative integers are valid. Notice that an example includes a negative integer.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: Can an element be used more than once?

A: No, assume each element of the array can be used at most once in the solution.

#### Q: Should the output be ordered in any way?

A: No, since you are returning a set, the data is expected to be unordered and will be valid as long as the correct items are in the set.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper.

- If your candidate struggles to track possible combinations of numbers, encourage them to first consider the brute force solution and generate all possible combinations of 4 elements of the array (this will require four nested loops).

- If your candidate struggles to debug their solution, encourage them to print the value of the numbers that they are summing at each step of the iteration.

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What's the complexity of the sample solution?

- If you wrote a solution without using a hash table, try refactoring your implementation to use a dictionary.

- Expand your solution so that it can handle inputs containing multiple solutions. Your function should return a set of tuples sorted in ascending order, where each tuple is a solution. For example

  ```py
  numbers = [2, 4, 6, 10, 0, 1]
  balanced(numbers)
  ```

  Produces

  ```py
  {(0,2,4,6), (0,4,6,10)}
  ```
