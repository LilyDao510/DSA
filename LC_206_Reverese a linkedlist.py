#Reverese a linkedlist

def reverseLinkedlist():
    prev, curr = None, head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

