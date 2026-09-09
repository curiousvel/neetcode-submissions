class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: Empty input list
        if not lists:
            return None
        
        min_heap = []
        
        # Initialize the heap with the head node of each non-empty linked list.
        # Format: (node_value, list_index, node_object)
        # Using `index` prevents Python comparison errors when two nodes have identical values.
        for index, l in enumerate(lists):
            if l:
               heapq.heappush(min_heap, (l.val, index, l))
        
        # Dummy head node to simplify list construction
        dummy_head = ListNode(0)
        tail = dummy_head

        # Continuously extract the smallest node across all k lists
        while min_heap:
            value, idx, smallest_node = heapq.heappop(min_heap)
            
            # Append the extracted node to the merged linked list
            tail.next = smallest_node
            tail = tail.next
            
            # If the extracted node has a next node, push it to the heap to keep k elements active
            if smallest_node.next:
                heapq.heappush(min_heap, (tail.next.val, idx, smallest_node.next))

        return dummy_head.next