#1. Implement a method to find the middle element of the linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.value

# Example Usage
head = ListNode(3, ListNode(6, ListNode(9, ListNode(12, ListNode(15)))))
print(find_middle(head)) 

#2.  Create a method to detect if the linked list has a cycle.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def has_cycle(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# Example Usage
head = ListNode(3)
head.next = ListNode(6)
head.next.next = head  
print(has_cycle(head))  

# 3. Implement a method to remove duplicates from an unsorted linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def remove_duplicates(head):
    if not head:
        return head
    
    current = head
    values = set()
    prev = None
    while current:
        if current.value in values:
            prev.next = current.next
        else:
            values.add(current.value)
            prev = current
        current = current.next
    
    return head

# Example Usage
head = ListNode(3, ListNode(6, ListNode(6, ListNode(12, ListNode(15, ListNode(15))))))
new_head = remove_duplicates(head)
current = new_head
while current:
    print(current.value, end=" ")  # Output: 3 6 12 15
    current = current.next

# 4. Add a method to merge two sorted linked lists into a single sorted linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_two_sorted_lists(l1, l2):
    dummy = ListNode(0)
    current = dummy

    p1, p2 = l1, l2
    while p1 and p2:
        if p1.value < p2.value:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next

    if p1:
        current.next = p1
    elif p2:
        current.next = p2

    return dummy.next

# Example Usage
l1 = ListNode(1, ListNode(3, ListNode(5)))
l2 = ListNode(2, ListNode(4, ListNode(6)))
merged_head = merge_two_sorted_lists(l1, l2)
current = merged_head
while current:
    print(current.value, end=" ")  
    current = current.next