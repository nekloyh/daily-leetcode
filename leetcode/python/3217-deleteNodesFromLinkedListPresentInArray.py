from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        vals = []
        curr = self
        while curr:
            vals.append(str(curr.val))
            curr = curr.next
        return " ".join(vals)

class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        rm_set = set(nums)
        while head and head.val in rm_set:
            head = head.next
            
        tmp = head
        while tmp and tmp.next:
            while tmp.next and tmp.next.val in rm_set:
                tmp.next = tmp.next.next 
            tmp = tmp.next
            
        return head


def build_ListNode(headList: List[int]) -> Optional[ListNode]:
    head = ListNode(headList[0])
    tmp = head
    for _head in headList[1:]:
        tmp.next = ListNode(_head)
        tmp = tmp.next
    return head


def main():
    sol = Solution()
    nums = [1, 2, 3]
    head = [1, 2, 3, 4, 5]
    listNode = build_ListNode(head)
    res = sol.modifiedList(nums, listNode)
    print(res)


if __name__ == "__main__":
    main()
    