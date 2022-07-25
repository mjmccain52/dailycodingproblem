"""Given a singly linked list and an integer k, remove the kth last 
element from the list. k is guaranteed to be smaller than the length 
of the list.

The list is very long, so making more than one pass is prohibitively 
expensive.

Do this in constant space and in one pass.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values:list) -> None:
        self.head = Node(values[0])
        prev = self.head
        for i in range(1, len(values)):
            curr = Node(values[i])
            prev.next = curr
            prev = curr
    def __str__(self):
        curr = self.head
        out = ""
        while curr is not None:
            out += f"{curr.value} -> "
            curr = curr.next
        return out

def main():
    ll = LinkedList([9,9,1,6,3])
    print(ll)
    remove_element(ll, 4)
    print(ll)

def remove_element(linked_list: LinkedList, k: int) -> None:
    if k == 0:
        gone = linked_list.head
        linked_list.head = linked_list.head.next
        del gone
        return
    curr = linked_list.head
    for i in range(1, k):
        curr = curr.next
    gone = curr.next
    curr.next = curr.next.next
    del gone
    

if __name__ == "__main__":
    main()
