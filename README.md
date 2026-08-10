# Data Structures & Algorithms — LeetCode Solutions

This repository tracks my journey solving algorithmic problems, refining my coding logic, and mastering fundamental data structures.

---

## 📌 LeetCode #2: Add Two Numbers
* **Difficulty:** Medium  
* **Topic:** Linked Lists, Math  
* **Language:** Python 3  
* **Problem Link:**  https://leetcode.com/problems/add-two-numbers/description/ 

### 📝 Problem Statement
You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#### Example:
```text
Input: l1 =, l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
```

---

### 💡 Core Solution Logic & Strategy

Instead of adding node-by-node immediately, this solution uses an intuitive approach that extracts the actual numeric values out of the linked lists, sums them up, and then reconstructs the resulting digits into a clean output chain.

#### 1. Linked List to Integer Conversion
* Traverse `l1` and `l2` independently using a loop.
* Track a base-10 `multiplier` variable starting at `1` that scales up (`* 10`) with each node step.
* Accumulate the values systematically to rebuild the full integer (`num1 = num1 + (node.val * multiplier)`). 
* *Example:* Node values `2 -> 4 -> 3` translate cleanly into $(2 \times 1) + (4 \times 10) + (3 \times 100) = 342$.

#### 2. Summation & Edge Cases
* Combine both calculated integers: `total_sum = num1 + num2`.
* Check for critical edge conditions: If `total_sum` equals exactly `0` (e.g., adding `0 + 0`), immediately return a single `ListNode(0)` to prevent the main translation loop from executing empty data.

#### 3. Rebuilding the Output Chain (The Dummy Node Strategy)
* Instantiate a baseline placeholder node `dummy = ListNode(0)` to anchor the structural chain.
* Loop continuously through the `total_sum` value while it remains greater than zero.
* Extract individual rightmost digits using the modulo operator (`total_sum % 10`) and anchor them into fresh nodes.
* Shift the running numeric sequence downwards via floor division (`total_sum //= 10`) to correctly strip the used values and gracefully close the loop.
* Return `dummy.next` to safely omit the placeholder anchor and return the clean, reversed answer node sequence.

---


