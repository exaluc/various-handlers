import os
import json
import uuid

class FolderManager:
    def __init__(self):
        self.file_list = []
        self.permission_denied_list = []
        self.other_errors = []

    def list_files(self, path):
        self.file_list = []
        self.permission_denied_list = []
        self.other_errors = []
        self._list_files_recursive(path, None)  # Initialize with None, as the root has no parent
        return self.file_list, self.permission_denied_list, self.other_errors

    def _list_files_recursive(self, path, parent_uuid):
        files = []
        try:
            files = os.listdir(path)
        except PermissionError:
            self.permission_denied_list.append(path)
        except (FileNotFoundError, NotADirectoryError, OSError) as e:
            self.other_errors.append(str(e))
            return

        current_uuid = str(uuid.uuid4())  # Generate a new UUID for this directory/file
        for file_name in files:
            try:
                file_path = os.path.join(path, file_name)
            except TypeError as e:
                self.other_errors.append(str(e))
                continue
                
            file_info = {
                "name": file_name,
                "path": file_path,
                "is_directory": os.path.isdir(file_path),
                "is_symlink": os.path.islink(file_path),
                "target": os.readlink(file_path) if os.path.islink(file_path) else None,
                "created_time": None,
                "modified_time": None,
                "size": None,
                "parent": parent_uuid,  # Assign parent UUID
                "id": current_uuid,  # Assign current UUID
            }

            try:
                if os.path.exists(file_path):
                    file_info["created_time"] = os.path.getctime(file_path)
                    file_info["modified_time"] = os.path.getmtime(file_path)
                    file_info["size"] = os.path.getsize(file_path) if os.path.isfile(file_path) else None
            except (OverflowError, OSError) as e:
                self.other_errors.append(str(e))

            self.file_list.append(file_info)
            
            if os.path.isdir(file_path) and not os.path.islink(file_path):
                self._list_files_recursive(file_path, current_uuid)  # Pass the current UUID as parent for children

if __name__ == "__main__":
    folder_manager = FolderManager()
    path_to_list = "/tmp"  # Replace with the desired folder path
    file_list, permission_denied_list, other_errors = folder_manager.list_files(path_to_list)
    
    print("List of files:")
    print(json.dumps(file_list, indent=4))
    
    print("\nPaths with Permission Denied:")
    print(json.dumps(permission_denied_list, indent=4))

    print("\nOther Errors:")
    print(json.dumps(other_errors, indent=4))
