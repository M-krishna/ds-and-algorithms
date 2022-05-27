# Basic Queue(FIFO) implementation using List(array)


from __future__ import annotations


class Queue:
    def __init__(self):
        self.items = []  # infinite

    def enqueue(self, val: str):
        print(f"Enqueue: {val}")
        self.items.append(val)

    def dequeue(self):
        if self.is_empty:
            print("Queue is empty")
            return
        first_element = self.items[0]
        modified_queue = self.items[1:]
        self.items = modified_queue
        print("Dequeued item:", first_element)

    @property
    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peak(self):
        if self.is_empty:
            print("Queue is empty")
            return
        print("Peak:", self.items[0])

    def print_values(self):
        print("Items in Queue:")
        for item in self.items:
            print(item, end=" ")
        print()  # new line


if __name__ == "__main__":
    queue = Queue()

    # Add items to the Queue
    for i in range(1, 6):
        queue.enqueue(str(i))

    # print queue
    queue.print_values()

    # peak
    queue.peak()  # should print 1

    # dequeue
    queue.dequeue()  # should print 1

    # print queue
    queue.print_values()  # 1 should not be present in queue

    # peak
    queue.peak()  # should print 2

    # deque
    queue.dequeue()  # 2
    queue.dequeue()  # 3
    queue.dequeue()  # 4
    queue.dequeue()  # 5
    queue.dequeue()  # Empty

    # enqueue
    queue.enqueue("6")

    # print queue
    queue.print_values()  # should print 6

    # dequeue
    queue.dequeue()  # should print 6

    # peak
    queue.peak()  # queue is empty
