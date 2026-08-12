# Data Structures & Algorithms — LeetCode Solutions

This repository tracks my journey solving algorithmic problems, refining my coding logic, and mastering fundamental data structures.

---

## 📌 LeetCode #2: Add Two Numbers 
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

## 📌 LeetCode #9: Palindrome Number 
* **Topic:** Math, Two Pointers  
* **Language:** Python 3  
* **Performance:** 0 ms (Beats 100% of Python submissions!)  
* **Problem Link:** https://leetcode.com/problems/palindrome-number/ 

### 📝 Problem Statement
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise. An integer is a palindrome when it reads the same backward as forward (e.g., `121` is a palindrome, while `123` is not).

#### Example:
```text
Input: x = 121
Output: true
```

### 💡 Core Solution Logic & Strategy
1. **Immediate Edge Case:** Negative numbers (like `-121`) are instantly rejected (`return False`) because the trailing minus sign prevents them from reading identically backward.
2. **Value Preservation:** Before running the extraction math, the original value of `x` is duplicated into a tracking variable (`a = x`). This is necessary because processing digits reduces the target down to `0`.
3. **Mathematical Reversal:** A `while` loop extracts individual trailing numbers via modulo operations (`x % 10`), aggregates them into a running reversed sequence, and cuts the primary input value down systematically (`x //= 10`).
4. **Final Evaluation:** Once the math loop terminates, the stored baseline signature (`a`) is checked directly against the newly assembled reversed sequence (`return a == reversed_num`).


---

## 📌 LeetCode #13: Roman to Integer  
* **Topic:** Hash Table, Math, String  
* **Language:** Python 3  
* **Problem Link:** (https://leetcode.com/problems/roman-to-integer/) 

### 📝 Problem Statement
Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`. Given a roman numeral, convert it to an integer.

#### Example:
```text
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V = 5, III = 3.
```

### 💡 Core Solution Logic & Strategy
1. **Value Mapping:** Create a dictionary mapping each Roman numeral character symbol to its integer equivalent (e.g., `'I': 1`, `'V': 5`).
2. **Lookahead Lookups:** Iterate through the string using indices. For each character, check if there is a next character available (`if i < len(s) - 1`).
3. **Subtraction Rule Handling:** If a character's mapped numerical value is smaller than the following character's value (such as `I` appearing right before `V`), subtract its value from the tracker. 
4. **Aggregation:** In all standard circumstances where values remain steady or decrease sequentially, simply increment the running `total_sum` calculation.


