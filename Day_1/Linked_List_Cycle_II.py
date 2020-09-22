# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        #---------------------------------------------#
        #                 SOLUTION 1                  #
        #---------------------------------------------#
#         walker = head
#         runner = head
        
#         while runner and runner.next:
#             # walker is always 2 paces behind runner
#             walker = walker.next
#             runner = runner.next.next
            
#             if walker == runner:
#                 seeker = head
                
#                 while seeker != walker:
#                     seeker = seeker.next
#                     walker = walker.next
                    
#                 return walker
            
        #---------------------------------------------#
        #                 SOLUTION 2                  #
        #---------------------------------------------#
        
        visited = set()
        itr = head
        
        while itr is not None:
            if itr in visited:
                return itr
            else:
                visited.add(itr)
                itr = itr.next
                
        return None