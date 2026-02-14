from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, listVal: List):
        self.head = ListNode(listVal[-1], None)
        for i in range(len(listVal) - 2, -1, -1):
            self.head =  ListNode(listVal[i], self.head)

class Solution:
    def getDecimalValue(self, head: List) -> int:
        linkedlist = LinkedList(head)
        node = linkedlist.head
        res = 0
        while node:
            res = res * 2 + node.val
            node = node.next
        return res
    
def main():
    sol = Solution()
    head = [1, 0, 1]
    print(sol.getDecimalValue(head))
    
if __name__ == "__main__":
    main()