"""Given a singly linked list and an integer k, remove the kth last 
element from the list. k is guaranteed to be smaller than the length 
of the list.

The list is very long, so making more than one pass is prohibitively 
expensive.

Do this in constant space and in one pass.
"""
import pytest


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

@pytest.fixture()
def linked_list():
    yield LinkedList([9,9,1,6,3])

def test_1(linked_list): 
    remove_element(linked_list, 0)
    assert str(linked_list) == "9 -> 1 -> 6 -> 3 -> "
def test_2(linked_list): 
    remove_element(linked_list, 2)
    assert str(linked_list) == "9 -> 9 -> 6 -> 3 -> "
def test_3(linked_list): 
    remove_element(linked_list, 4)
    assert str(linked_list) == "9 -> 9 -> 1 -> 6 -> "