# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def remove_kth_from_end(head, k):
    # remove the kth node from the end of the LL and return the head
    # ------------------------------------------------------- #
    #                  Solution 1: Two pass                   #
    # ------------------------------------------------------- #

    # loops while next is not none
    # store a count of total items in the LL
    # kth location(index) = count - k + 1  (10-4+1)
    # loop until count == kth location
    # track prev and cur
    # prev = cur.next
    # cur.next = None
    # return head

    actual_head = head
    cur = head
    count = 1

    if k == 0:
        return actual_head

    # Count the number of items in the LL
    while cur.next:
        count += 1
        cur = cur.next

    if k > count:
        return actual_head

    kth_location = (count - k) + 1

    count = 1
    cur = head
    prev = None

    while count <= kth_location:
        # Removing head case
        if kth_location == 1:
            new_head = cur.next
            cur.next = None
            return new_head

        # Removing kth location
        if kth_location > 1:
            if count == kth_location:
                # set prev.next to cur.next
                # set cur.next to None
                # return head
                prev.next = cur.next
                cur.next = None
                return actual_head

        count += 1
        prev = cur
        cur = cur.next