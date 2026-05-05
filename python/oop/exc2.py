# Reviewer: Alexander.

class Node:
    def __init__(self, data) -> None:
        self.next = None
        self.data = data


class Queue:
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, data) -> None:
        """
        Insert element to the queue.
        :param data: data element to be inserted.
        :return: None
        """
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self) -> all:
        """
        Print and remove the front of the queue.
        :return: all types.
        """
        if self.head is not None:
            self.length -= 1
            temp = self.head.data
            print(temp)
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return temp
        else:
            print("Queue is empty")

    def peek_queue(self) -> all:
        """
        return first element in line.
        :return: all types
        """
        if self.head is None:
            print("Queue is empty.")
            return None
        return self.head.data

    def print_queue(self) -> None:
        """
        Prints the Queue in order.
        :return: None
        """
        temp = self.head
        while temp is not None:
            print("" if temp is self.head or temp.next is None else " ->",
                  temp.data, end="")
            temp = temp.next
        print("")

    def count(self) -> int:
        """
        Returns the length of the current queue.
        :return: int
        """
        return self.length

    def is_empty(self) -> bool:
        """
        Check if Queue is empty.
        :return: bool
        """
        return self.head is None


def main():
    q = Queue()
    names = "Daniel Netta C ran anan ".split(" ")
    # Enqueue test.
    for name in names:
        q.enqueue(name)
    assert q.count() == len(names)
    assert q.peek_queue() == names[0]
    # Dequeue test.
    q.print_queue()
    for i in range(q.count()):
        assert q.dequeue() == names[i]
    # Is empty test.
    assert q.is_empty()
    assert 0 == q.count()

    print("All tests passed.")
    print("Done.")


if __name__ == '__main__':
    main()
