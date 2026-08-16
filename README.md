# Data Structures & Algorithms — LeetCode Solutions

This repository tracks my journey solving algorithmic problems, refining my coding logic, and mastering fundamental data structures.

---

## 📌 LeetCode #2: Add Two Numbers 
* **Topic:** Linked Lists, Math  
* **Language:** Python 3  
* **Problem Link:** https://leetcode.com 

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
* *Example:* Node values `2 -> 4 -> 3` translate cleanly into \((2 \times 1) + (4 \times 10) + (3 \times 100) = 342\).

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
* **Problem Link:** https://leetcode.com 

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
* **Problem Link:** https://leetcode.com 

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

---

## 🚀 Solved Problems Index

| # | Problem Title | Difficulty | Language | Solution File |
|---|---------------|------------|----------|---------------|
| 2 | [Add Two Numbers](https://leetcode.com) | 🟡 Medium | Python 3 | [Solution](./2_add_two_numbers.py) |
| 9 | [Palindrome Number](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./palindrome_number.py) |
| 13 | [Roman to Integer](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./roman_to_integer.py) |
| 14 | [Longest Common Prefix](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./14_longest_common_prefix.py) |
| 21 | [Merge Two Sorted Lists](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./21_merge_two_sorted_lists.py) |
| 26 | [Remove Duplicates from Sorted Array](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./solution.py) |
| 27 | [Remove Element](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./solution.py) |
| 35 | [Search Insert Position](https://leetcode.com) | 🟢 Easy | Python 3 | [Solution](./search_insert_position.py) |

---

## 📝 Additional Problem Breakdowns

### 📌 LeetCode #14: Longest Common Prefix
**Approach:** Vertical Scanning
- **Concept:** Compare characters of all strings index by index, using the first string as a baseline anchor.
- **Optimization:** Immediately returns the prefix slice the moment a character mismatch occurs or an out-of-bounds index condition is hit.

#### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(S)$ where $S$ is the total sum of all characters across all strings in the input array.
- **Space Complexity:** $\mathcal{O}(1)$ because the vertical scan checks characters in place without allocating extra memory structures.

---

### 📌 LeetCode #21: Merge Two Sorted Lists
**Approach:** Two-Pointer Iteration with Dummy Head Node
- **Concept:** Compare the head nodes of both lists, attach the smaller node to the building `tail`, and step that list pointer forward.
- **Optimization:** Avoids handling complex starting edge cases by initializing a baseline `ListNode()`, and snaps remaining straggler nodes onto the tail in a single $\mathcal{O}(1)$ step using a ternary operation when one list runs dry.

#### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(N + M)$ where $N$ and $M$ represent the total number of nodes in each independent linked list.
- **Space Complexity:** $\mathcal{O}(1)$ as the sorting operations reconnect existing node object references directly in-place.

---

### 📌 LeetCode #26: Remove Duplicates from Sorted Array
**Approach:** Two-Pointer In-Place Modification
- **Concept:** Since the input array is already sorted, all duplicate elements sit right next to each other. 

#### Intuition & Steps:
1. We track a `pointer` index that marks where the next unique element should be written.
2. We loop through the array with a scanning index `i`.
3. Whenever `nums[i]` is different from `nums[pointer]`, we know we've hit a brand new unique number.
4. We copy that unique number forward to `nums[pointer + 1]` and increment our unique `pointer`.

---

### 📌 LeetCode #35: Search Insert Position
**Approach:** Binary Search
- **Concept:** Continually divide the sorted search space in half to locate the index or isolate the exact point where insertion should occur.

#### Complexity Analysis
- **Time Complexity:** $\mathcal{O}(\log n)$ as the remaining items are cut in half at every comparison step.
- **Space Complexity:** $\mathcal{O}(1)$ using simple primitive tracking bounds variables.
