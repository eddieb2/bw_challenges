# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # --------------------------------------------------------
        # SOLUTION 1 -- O(n) -- ugly but very fast
        num1 = []
        num2 = []
        
        itr1 = l1
        while itr1:
            num1.append(str(itr1.val))
            itr1 = itr1.next
        
        itr2 = l2
        while itr2:
            num2.append(str(itr2.val))
            itr2 = itr2.next
        
        # reverse each list 
        # ['3','4','2'] -> ['2','4','3'] && ['4','6','5'] -> ['5','6','4']
        # allows us to have the correct sequence of nums to add correctly
        num1.reverse()
        num2.reverse()
    
        # join each list => ['243'] && ['564']
        full_num1 = ''.join(num1)
        full_num2 = ''.join(num2)

        # convert to each to integers and add
        total = int(full_num1) + int(full_num2)
        
        # convert back into a list with each integer in it's own index
        list_LL = [int(num) for num in str(total)]
        
        # reverse order as required for the linked list output
        list_LL.reverse()
        
        # create a head
        l3 = ListNode(0)
        cur = l3
        
        # add all items from the list into the new linked list
        for i in range(len(list_LL)):
            cur.next = ListNode(list_LL[i])
            next_itr = cur.next
            cur = next_itr
            
        # remove the head
        l3 = l3.next
        
        #return new linked list
        return l3
        
        # -------------------------------------------------------