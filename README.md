# DSA-Python
# Kadane's Algorithm (Maximum Subarray Sum)

## Description
Kadane's Algorithm is an efficient method to find the **maximum sum of a contiguous subarray** within a one-dimensional array.

## Problem Statement
Given an integer array `nums`, return the maximum possible sum of any contiguous subarray.

## Algorithm
1. Initialize `current_sum` and `max_sum` with the first element.
2. Traverse the array from the second element.
3. At each step:
   - Update `current_sum` as the maximum of:
     - the current element, or
     - `current_sum + current element`
   - Update `max_sum` if `current_sum` is greater.
4. Return `max_sum`.

## Example

**Input**
```python
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

**Output**
```python
6
```

**Explanation**
The maximum sum subarray is:
```python
[4, -1, 2, 1]
```
Sum = **6**

## Time Complexity
- **O(n)**

## Space Complexity
- **O(1)**

## Features
- Efficient linear-time solution
- Constant extra space
- Works with arrays containing negative numbers

## Author
Your Name
