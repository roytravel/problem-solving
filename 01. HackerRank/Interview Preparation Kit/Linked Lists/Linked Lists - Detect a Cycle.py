def has_cycle(head):
    visit = []
    current = head

    while current:
        node = current.data
        if node not in visit:
            visit.append(node)
        else:
            return True
        current = current.next
    return False