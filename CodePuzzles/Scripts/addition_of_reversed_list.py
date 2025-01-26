class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        # Get the values of the current nodes (or 0 if the node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create a new node with the sum digit and move to the next node
        current.next = ListNode(digit)
        current = current.next
        print(f"val1 --> {val1}, val2 --> {val2}, total --> {total}, carry --> {carry}, digit --> {digit}")

        # Move to the next nodes in both linked lists (if they exist)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next

# Example usage:
# Create linked lists representing numbers: 243 and 564
l1 = ListNode(3, ListNode(4, ListNode(2)))
l2 = ListNode(4, ListNode(6, ListNode(5)))

# Add the two numbers
result = addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" -> ")
    result = result.next
