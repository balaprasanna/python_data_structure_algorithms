
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2, c=0):
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            return ListNode(l2.val)
        if l2 is None:
            return ListNode(l1.val)

        curr_sum = l1.val + l2.val + c
        if curr_sum > 9:
            c, curr_sum = curr_sum//10, curr_sum % 10

        l3 = ListNode(curr_sum)
        l3.next = self.addTwoNumbers(l1.next, l2.next, c)
        return l3


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = Solution().addTwoNumbers(l1, l2)
    while result:
        print(result.val)
        result = result.next
        # 7 0 8
