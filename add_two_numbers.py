# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
     num1=0
     multiplier=1
     while l1:
        num1=num1+(l1.val *multiplier)
        multiplier=multiplier*10
        l1=l1.next

     num2=0
     multiplier=1  
     while l2:
        num2=num2+(l2.val *multiplier)
        multiplier=multiplier*10
        l2=l2.next 
     total_sum=  num1 +num2

     dummy=ListNode(0)
     carry=dummy
     
     if total_sum == 0:
        return ListNode(0)

     while total_sum:
        digits=total_sum % 10    
        carry.next=ListNode(digits)
        carry=carry.next
        total_sum//= 10

     return dummy.next


        
