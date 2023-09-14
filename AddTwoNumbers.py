

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
     num1 = 0
     count = 0
     temp = l1

     while(temp != None):
          num1 = num1 + temp.val * (10 ** count)
          count += 1
          temp = temp.next

     temp = l2
     count = 0
     num2 = 0
        
     while(temp != None):
          num2 += temp.val * (10 ** count)
          count += 1
          temp = temp.next

     result = num1 + num2

     if(result == 0):
          return ListNode(0)
        
     head = ListNode(None)
     temp = head

     while(result > 0):
          temp.next = ListNode(None)
          temp.val = result % 10
          temp = temp.next
          result //= 10

            

     curr = head
     prev = None

     while(curr.next):
          prev = curr
          curr = curr.next
        
     prev.next = None


     return head
