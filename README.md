# DSA LeetCode Practice Solutions

## Problem: Add Two Numbers (LeetCode #2)
**Difficulty:** Medium  
**Link:** [LeetCode Problem Link](https://leetcode.com)

### Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

### My Approach
1. Convert both linked lists into standard Python integers by iterating through them using a multiplier (1, 10, 100, etc.).
2. Sum the two integer values together.
3. Rebuild a brand-new linked list from the resulting sum using a dummy node strategy.
4. Handle the edge case where the total sum is exactly `0`.
