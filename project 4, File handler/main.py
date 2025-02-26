import os
import shutil


class FileHandler:
    def __init__(self):
        self.folder_name = ''
        self.file_name = ''
        self.content = ''
        self.new_file_permition = False
        self.content_r = []
        self.folder_path = os.getcwd()
        self.derectories = [i for i in os.listdir() if os.path.isdir(i)]
        self.files = [i for i in os.listdir() if not os.path.isdir(i)]
    # Make folder
    def get_forder_name(self):
        self.folder_name = input('Name the folder>')
        while os.path.exists(self.folder_name) and os.path.isdir(self.folder_name):
            print('Folder exists, do you wand to add file to existing folder. Yes or No >')
            print(os.listdir(self.folder_name))
            answer = input('>')
            if answer == 'Yes' or 'yes':
                os.chdir(self.folder_name)
                self.new_file_permition = True
                break
            else:
                self.file_name = input('New folder name> \n')
                continue
        os.mkdir(self.folder_name)

    # Make file functionality
    def make_file(self):
        if self.new_file_permition:
            self.file_name = input('Name the file(with file extention(eg:- .py .txt)> \n')
            if os.path.exists(self.file_name):
                answer = input('Do you want to rewrite or add>')
                if 'rewrite' in answer:
                    content = input('What do you want to write file>')
                    with open(self.file_name, 'w') as f:
                        f.write(content)
                elif 'add' in answer:
                    content = input('What do you wan\'t to add to file>\n')
                    with open(self.file_name, 'a') as f:
                        f.write(f'\n{content}')

                print(f'Content writen to {self.file_name}')
            else:
                content = input('What do you want to write file>\n')
                with open(self.file_name, 'w') as f:
                    f.write(content)
                    print(f'Content writen to \n{self.file_name}')
        else:
            pass

    # Read file functionality
    def read_file(self):
        files = os.listdir()
        print(files)
        uer_input = input('Which one do you wan\'t to read>\n')
        if uer_input in files:
            with open(uer_input, 'r') as f:
                self.content_r = f.readlines()
            for i in self.content_r:
                print(i, end='')
            print()

    #Change directory
    def change_directory(self):
        path = self.folder_path
        files_or_forder = os.listdir()
        directories = [i for i in files_or_forder if os.path.isdir(i)]
        print(path)
        print(directories)
        new_dir = input('Which directory do you want to enter \n or \'..\' to go back a directory> \n')
        if new_dir in directories or new_dir == '..':
            os.chdir(new_dir)
            f_n = os.listdir()
            print(f_n)
            self.folder_path = os.getcwd()
        else:
            print('Folder does not exist.')

    def delete_forlder_file(self):
         fils_folders = os.listdir()
         path = self.folder_path
         path = os.getcwd()
         print(f'Current directory:\n{path}')
         print(fils_folders)
         del_foler_file = input('What do you wan\'t to delete>\n')
         if del_foler_file not in fils_folders:
             print('File not found')
         else:
            del_per = input('Are you suer you want to delete the file or folder(yes, no): THIS CAN\'T BE UNDONE!!>\n')
            massage = ''
            if del_per == 'yes':
                if os.path.isdir(del_foler_file):
                    massage = f'\'{del_foler_file}\' and all its content was deleted'
                    shutil.rmtree(del_foler_file)
                else:
                    os.remove(del_foler_file)
                    massage = f'\'{del_foler_file}\' was deleted'
                print(massage)
            else:
                print('Folder not Deleted')

    def move(self):
        while True:
            print("\nAvailable files and folders:")
            print(os.listdir(self.folder_path))  # Show contents of the directory

            file_folder = input("Which file/folder do you want to move?>\n ")
            source = os.path.join(self.folder_path, file_folder)  # Correct path

            if not os.path.exists(source):  # Corrected check
                print("Error: The specified file or folder does not exist. Try again.")
                continue

            destination_folder = input("Where do you want to move it to?>\n ")
            destination = os.path.join(self.folder_path, destination_folder)

            try:
                shutil.move(source, destination)
                print(f"{file_folder} moved successfully to {destination}")
                break  # Exit loop on success
            except shutil.Error as e:
                print(f"Error: {e}. Try again.")
                continue


if __name__ == "__main__":
    file_hander = FileHandler()
    print('Welcome to file handler.')
    current_folder = os.getcwd().split("/")
    print(f'Current directory \n{current_folder[-1]}')
    while True:
        try:
            print('You can carry out folowing commands: \nMake folder-Mf \nWrite file-Wf \nRead file-Rf\nChange directory-Cd\nDelete-Dl\nMove-Cp')
            a = input('Enter command or eixt() to exit> \n').lower()
            if a == 'exit()':
                print("Bye, have a nice day")
                break
            else:
                if a in ['Make folder', 'make folder', 'Mf', 'mf']:
                    file_hander.get_forder_name()
                    if file_hander.new_file_permition:
                        file_hander.make_file()
                        continue
                    else:
                        pass
                elif a in ['write file', 'wf']:
                    file_hander.new_file_permition = True
                    print(os.listdir())
                    file_hander.make_file()
                    continue
                elif a in ['read file', 'rf']:
                    file_hander.read_file()
                    continue
                elif a in ['change directory', 'cd']:
                    file_hander.change_directory()
                elif a in ['delete', 'dl']:
                    file_hander.delete_forlder_file()
                elif a in ['move', 'cp']:
                    file_hander.move()
                else:
                    print("Command error")
        except OSError:
            print("Somting happend")
            print(str(OSError))
