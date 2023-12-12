class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def main():
    while True:
        print("Choose an option:")
        print("1. Stack")
        print("2. Queue")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            stack = Stack()
            while True:
                print("\nStack Operations:")
                print("1. Push")
                print("2. Pop")
                print("3. Peek")
                print("4. Size")
                print("5. Back to Main Menu")
                stack_choice = input("Enter your choice: ")

                if stack_choice == "1":
                    item = input("Enter item to push: ")
                    stack.push(item)
                elif stack_choice == "2":
                    popped_item = stack.pop()
                    print(f"Popped item: {popped_item}")
                elif stack_choice == "3":
                    peeked_item = stack.peek()
                    print(f"Top item: {peeked_item}")
                elif stack_choice == "4":
                    stack_size = stack.size()
                    print(f"Stack size: {stack_size}")
                elif stack_choice == "5":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "2":
            queue = Queue()
            while True:
                print("\nQueue Operations:")
                print("1. Enqueue")
                print("2. Dequeue")
                print("3. Size")
                print("4. Back to Main Menu")
                queue_choice = input("Enter your choice: ")

                if queue_choice == "1":
                    item = input("Enter item to enqueue: ")
                    queue.enqueue(item)
                elif queue_choice == "2":
                    dequeued_item = queue.dequeue()
                    print(f"Dequeued item: {dequeued_item}")
                elif queue_choice == "3":
                    queue_size = queue.size()
                    print(f"Queue size: {queue_size}")
                elif queue_choice == "4":
                    break
                else:
                    print("Invalid choice. Try again.")

        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()            
