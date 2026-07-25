chat = []

while True:
    print("\n===== CHAT APPLICATION =====")
    print("1. Send Message")
    print("2. View Chat History")
    print("3. Update Message")
    print("4. Delete Message")
    print("5. Search Message")
    print("6. Total Messages")
    print("7. Clear Chat History")
    print("8. Exit")
    
    choice = int(input("Enter your choice: "))

    # Send Message
    if choice == 1:
        msg = input("Enter your message: ")
        chat.append(msg)
        print("Message sent successfully.")

    # View Chat History
    elif choice == 2:
        if len(chat) == 0:
            print("No messages found.")
        else:
            print("\nChat History:")
            for i in range(len(chat)):
                print(f"{i + 1}. {chat[i]}")

    # Update Message
    elif choice == 3:
        if len(chat) == 0:
            print("No messages to update.")
        else:
            for i in range(len(chat)):
                print(f"{i + 1}. {chat[i]}")
            num = int(input("Enter message number to update: "))
            if 1 <= num <= len(chat):
                new_msg = input("Enter new message: ")
                chat[num - 1] = new_msg
                print("Message updated successfully.")
            else:
                print("Invalid message number.")

    # Delete Message
    elif choice == 4:
        if len(chat) == 0:
            print("No messages to delete.")
        else:
            for i in range(len(chat)):
                print(f"{i + 1}. {chat[i]}")
            num = int(input("Enter message number to delete: "))
            if 1 <= num <= len(chat):
                chat.pop(num - 1)
                print("Message deleted successfully.")
            else:
                print("Invalid message number.")

    # Search Message
    elif choice == 5:
        if len(chat) == 0:
            print("No messages found.")
        else:
            search = input("Enter message to search: ")
            found = False
            for i in range(len(chat)):
                if search.lower() in chat[i].lower():
                    print(f"Found at message {i + 1}: {chat[i]}")
                    found = True
            if not found:
                print("Message not found.")

    # Total Messages
    elif choice == 6:
        print(f"Total Messages: {len(chat)}")

    # Clear Chat History
    elif choice == 7:
        chat.clear()
        print("Chat history cleared.")

    # Exit
    elif choice == 8:
        print("Thank you for using Chat Application.")
        break

    else:
        print("Invalid choice. Please try again.")