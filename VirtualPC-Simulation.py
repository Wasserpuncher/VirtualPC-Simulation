import os

class VirtualPC:
    def __init__(self):
        self.running = True
        self.current_folder = os.getcwd()

    def run(self):
        print("Virtual PC is running.")
        while self.running:
            self.display_options()
            choice = input("Enter choice: ")
            self.perform_action(choice)

    def display_options(self):
        print("\nVirtual PC Options:")
        print("1. Show current folder")
        print("2. List files and folders")
        print("3. Change folder")
        print("4. Run application")
        print("5. Exit")

    def perform_action(self, choice):
        if choice == '1':
            print(f"Current folder: {self.current_folder}")
        elif choice == '2':
            self.list_files_and_folders()
        elif choice == '3':
            new_folder = input("Enter new folder path: ")
            self.change_folder(new_folder)
        elif choice == '4':
            app_name = input("Enter application name: ")
            self.run_application(app_name)
        elif choice == '5':
            self.running = False
            print("Virtual PC is shutting down.")
        else:
            print("Invalid choice")

    def list_files_and_folders(self):
        items = os.listdir(self.current_folder)
        print("\nContents of current folder:")
        for item in items:
            print(item)

    def change_folder(self, new_folder):
        if os.path.exists(new_folder):
            self.current_folder = new_folder
            print(f"Current folder changed to {new_folder}")
        else:
            print("Folder not found")

    def run_application(self, app_name):
        if app_name == 'notepad':
            os.system('notepad')
        elif app_name == 'calculator':
            os.system('calc')
        else:
            print("Application not supported")

def main():
    pc = VirtualPC()
    pc.run()

if __name__ == "__main__":
    main()
