import os
import time
import shutil

class FileHandler:
    def __init__(self):
        # Current working directory
        self.path = os.getcwd()
        # List directories in the current working directory
        self.directories = [i for i in os.listdir() if os.path.isdir(i)]
        # Dictionary mapping file content to a list of full file paths
        self.files_contents = dict()
        # List of duplicate groups (each group is a list of full file paths with identical content)
        self.duplicate_groups = []
        self.new_directory = None
        self.found_duplicates = True

    def dp_content_finder(self):
        print("Available folders:")
        print(self.directories)

        while True:
            folder = input("Which one do you want to scan for duplicates in? \n")
            if folder in self.directories:
                # Use absolute path for the chosen folder
                self.new_directory = os.path.join(self.path, folder)
                print("Scanning...")
                # Recursively scan for files in the chosen folder
                for root, dirs, files in os.walk(self.new_directory):
                    for file in files:
                        full_path = os.path.join(root, file)
                        try:
                            with open(full_path, 'r', errors='ignore') as f:
                                content = f.read()
                        except Exception as e:
                            print(f"Error reading {full_path}: {e}")
                            continue

                        if content in self.files_contents:
                            self.files_contents[content].append(full_path)
                        else:
                            self.files_contents[content] = [full_path]

                time.sleep(1)
                print("\nDuplicate files found (files with identical content):")
                found = False
                for content, paths in self.files_contents.items():
                    if len(paths) > 1:
                        found = True
                        # Show relative paths for convenience:
                        rel_paths = [os.path.relpath(p, self.new_directory) for p in paths]
                        print(f"Duplicate group: {rel_paths}")
                        self.duplicate_groups.append(paths)
                if not found:
                    print("No duplicate files found.")
                    self.found_duplicates = False
                break
            else:
                print(f"{folder} not found! Try again.\n")
                continue

    def choose_closest_file(self, group):
        """
Given a list of full file paths (group), choose the one with the shallowest relative path.
        """
        closest = None
        min_depth = float('inf')
        for file in group:
            rel_path = os.path.relpath(file, self.new_directory)
            depth = rel_path.count(os.sep)
            if depth < min_depth:
                min_depth = depth
                closest = file
        return closest

    def remover(self, keep_file):
        """
Removes all files in the duplicate group containing keep_file, except for keep_file.
Parameter:
keep_file (str): The full path of the file to keep.
        """
        target_group = None
        for group in self.duplicate_groups:
            if keep_file in group:
                target_group = group
                break
        if not target_group:
            print("Specified file not found in any duplicate group. Aborting removal.")
            return

        for file in target_group:
            if file != keep_file:
                try:
                    os.remove(file)
                    print(f"Removed {os.path.relpath(file, self.new_directory)}")
                except Exception as e:
                    print(f"Error removing {file}: {e}")
        print("Removal completed.")

    def move_duplicates(self, keep_file):
        """
Moves all files in the duplicate group containing keep_file (except keep_file)
into a "duplicates" folder inside self.new_directory.
Parameter:
keep_file (str): The full path of the file to keep.
        """
        target_group = None
        for group in self.duplicate_groups:
            if keep_file in group:
                target_group = group
                break
        if not target_group:
            print("Specified file not found in any duplicate group. Aborting move.")
            return

        duplicates_folder = os.path.join(self.new_directory, "duplicates")
        if not os.path.exists(duplicates_folder):
            os.makedirs(duplicates_folder)

        for file in target_group:
            if file != keep_file:
                try:
                    dest_path = os.path.join(duplicates_folder, os.path.basename(file))
                    shutil.move(file, dest_path)
                    print(f"Moved {os.path.relpath(file, self.new_directory)} to {dest_path}")
                except Exception as e:
                    print(f"Error moving {file}: {e}")
        print(f"All duplicates (except {os.path.relpath(keep_file, self.new_directory)}) have been moved to: {duplicates_folder}")

if __name__ == '__main__':
    handler = FileHandler()
    handler.dp_content_finder()
    if handler.found_duplicates and handler.duplicate_groups:
        # If multiple duplicate groups are found, choose one group automatically (the first one)
        chosen_group = handler.duplicate_groups[0]
        # Automatically choose the file with the shallowest path (closest folder)
        file_to_keep = handler.choose_closest_file(chosen_group)
        print(f"\nAutomatically selected file to keep: {os.path.relpath(file_to_keep, handler.new_directory)}")

        action = input('What do you want to do: keep duplicates (keep), move duplicates (move) or remove duplicates (any other input)? \n').lower()
        if action == 'keep':
            print("No files were deleted or moved.")
        elif action == 'move':
            handler.move_duplicates(file_to_keep)
        else:
            handler.remover(file_to_keep)
            a = input('Should we remove empty folders? ').lower()
            if a == 'yes':
                os.chdir(handler.new_directory)
                folers = [ i for i in os.listdir() if os.path.isdir(i)]
                for i in folers:
                    if len(os.listdir(i)) == 0:
                        shutil.rmtree(os.path.join(i))
            else:
                pass
    else:
        print("No duplicate groups to process.")
        