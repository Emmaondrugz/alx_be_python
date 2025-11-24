def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            print('')
            new_item = input('What item would you like to add: ')
            shopping_list.append(new_item)
            print('')
            pass
        elif choice == '2':
            print('')
            for idx, x in enumerate(shopping_list):
                print(f'{idx + 1}. {x}')
            item = input('What item would you like to remove: ')

            if item not in shopping_list:
                print('Items could not be found in the shopping list')
            else:
                shopping_list.remove(item)
            print('')
            pass
        elif choice == '3':
            # Display the shopping list
            print('')
            print('Shopping list: ')
            for idx, x in enumerate(shopping_list):
                print(f'{idx + 1}. {x}')
            print('')
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()