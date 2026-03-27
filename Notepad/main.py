import os
import getpass

BOLD = '\033[1m'
END = '\033[0m'

#Define a function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Define the main menu function
def main_menu():
    clear_screen()
    print(f"{BOLD}--- PYTHON NOTEPAD ---{END}")
    menuselect = input("1. Create a new note\n2. View existing notes\n3. Edit a note\n4. Exit\nSelect an option: ")
    return menuselect

# Main program loop
while True:
    
    menuselect = main_menu()

    if menuselect == "1":
        clear_screen()
        print(f"\n{BOLD}Create Note Mode{END}")
        filename = input("Enter the filename for your note (with extension, e.g., note.txt): ")

        if "." not in filename:
            filename += ".txt"

        clear_screen()
        print(f"{BOLD}Type your note below. Type 'stop' to save and exit.{END}\n")
        
        words_list = []
        
        # 2. TYPING LOOP
        while True:
            userinput = input("> ")
            
            if userinput.lower() not in ["stop", "exit", "quit", "info"]:
                words_list.append(userinput)
                
            elif userinput.lower() in ["stop", "exit", "quit"]:
                
                script_folder = os.path.dirname(os.path.abspath(__file__))
                notes_folder = os.path.join(script_folder, "saved_notes")
                os.makedirs(notes_folder, exist_ok=True)
                
                save_path = os.path.join(notes_folder, filename)
                
                with open(save_path, "w") as file:
                    file.write("\n".join(words_list))
                
                # We put the exact save_path back into the success message!
                print(f"\nSuccess! Your note was safely stored at:\n{save_path}")
                
                getpass.getpass("\nPress Enter to return to the Main Menu...")
                break
    elif menuselect == "2":
        clear_screen()
        print(f"{BOLD}--- View Existing Notes ---{END}\n")

        script_folder = os.path.dirname(os.path.abspath(__file__))
        notes_folder = os.path.join(script_folder, "saved_notes")

        if not os.path.exists(notes_folder):
            print("No notes saved yet")
            getpass.getpass("\nPress Enter to return to the Main Menu...")
            continue

        files = [f for f in os.listdir(notes_folder) if not f.startswith('.')]

        if len(files) == 0:
            print("No notes saved yet")
            getpass.getpass("\nPress Enter to return to the Main Menu...")
            continue

        for index, filename in enumerate(files):
            print(f"{index + 1}. {filename}")

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a note to view (by number): ")

        if choice == "0":
            continue

        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(files):
                selected_file = files[file_index]
                file_path = os.path.join(notes_folder, selected_file)

                clear_screen()
                print(f"{BOLD}--- Reading: {selected_file} ---{END}\n")
                with open(file_path, "r") as file:
                    print(file.read())

                getpass.getpass("\nPress Enter to return to the Main Menu...")
            else:
                print("Invalid selection. That file does not exist.")
                getpass.getpass("\nPress Enter to try again...")

        except ValueError:
            print("Invalid input. Please enter a number.")
            getpass.getpass("\nPress Enter to try again...")

    elif menuselect == "3":
        clear_screen()
        print(f"{BOLD}--- Edit a Note ---{END}\n")

        script_folder = os.path.dirname(os.path.abspath(__file__))
        notes_folder = os.path.join(script_folder, "saved_notes")

        if not os.path.exists(notes_folder):
            print("No notes saved yet")
            getpass.getpass("\nPress Enter to return to the Main Menu...")
            continue

        files = [f for f in os.listdir(notes_folder) if not f.startswith('.')]

        if len(files) == 0:
            print("No notes saved yet")
            getpass.getpass("\nPress Enter to return to the Main Menu...")
            continue

        for index, filename in enumerate(files):
            print(f"{index + 1}. {filename}")

        print("\n0. Return to Main Menu")

        choice = input("\nSelect a note to edit (by number): ")

        if choice == "0":
            continue

        try:
            file_index = int(choice) - 1
            if 0 <= file_index < len(files):
                selected_file = files[file_index]
                file_path = os.path.join(notes_folder, selected_file)

                clear_screen()
                print(f"{BOLD}--- Editing: {selected_file} ---{END}\n")
                
                with open(file_path, "r") as file:
                    existing_content = file.read()

                print(f"{BOLD}Current content:{END}\n{existing_content}\n")
                print(f"{BOLD}Type your new content below. Type 'stop' to save and exit.{END}\n")

                words_list = []
                
                while True:
                    userinput = input("> ")
                    
                    if userinput.lower() not in ["stop", "exit", "quit", "info"]:
                        words_list.append(userinput)
                        
                    elif userinput.lower() in ["stop", "exit", "quit"]:
                        with open(file_path, "w") as file:
                            file.write("\n".join(words_list))
                        
                        print(f"\nSuccess! Your note was updated at:\n{file_path}")
                        getpass.getpass("\nPress Enter to return to the Main Menu...")
                        break
            else:
                print("Invalid selection. That file does not exist.")
                getpass.getpass("\nPress Enter to try again...")

        except ValueError:
            print("Invalid input. Please enter a number.")
            getpass.getpass("\nPress Enter to try again...")

    elif menuselect == "4":
        clear_screen()
        print("Exiting...")
        break

    else:
        # invalid option, re-show menu
        continue
