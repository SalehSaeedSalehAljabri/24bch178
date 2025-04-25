def queue_program():
    queue = []
    while True:
        print("\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            element = input("Enter element to enqueue: ")
            queue.append(element)
        elif choice == 2:
            if queue:
                print("Dequeued:", queue.pop(0))
            else:
                print("Queue is empty!")
        elif choice == 3:
            print("Queue:", queue)
        elif choice == 4:
            break
        else:
            print("Invalid choice!")
queue_program()
