# A Menu based program to perform the operations on stack in python.

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if is_empty(stack):
        raise Exception("Stack is empty")
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        raise Exception("Stack is empty")
    return stack[-1]

def display(stack):
    if is_empty(stack):
        print("Stack is empty")
    else:
        print("Stack is: ", end="")
        for item in stack:
            print(" |",item, end=" |")
        print()



if __name__=='__main__':
    stack = []
    try:
       while True:
           print("+++++++ Stack Operations +++++++")
           print("1. Push an element")
           print("2. Pop an element")
           print("3. Peek at the top element")
           print("4. Display the stack")
           print("5. Exit the program")
           choice = int(input("Enter your choice: "))
           if choice == 1:
               item = int(input("Enter the item to push: "))
               push(stack, item)
           elif choice == 2:
               print("Popped item is: ", pop(stack))
           elif choice == 3:
               print("Peeked item is: ", peek(stack))
           elif choice == 4:
               display(stack)
           elif choice == 5:
               break
           else:
               print("Wrong choice")
    except Exception:
        print("The stack is already empty")
        print("Exiting the program")
        exit()
