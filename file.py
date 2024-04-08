import os

def read_file_string(filename):
    return read_file_lines(filename)[0]
    
def read_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def list_role_files(role_name, default_subdirectory_name='default'):

    roles_directory = "data/roles"
    
    role_name = role_name.strip()
    if not role_name:
        print("No role name provided. Using default role.")
        role_name = default_subdirectory_name
    
    subdirectory_path = os.path.join(roles_directory, role_name)
    
    if not os.path.exists(subdirectory_path) or not os.path.isdir(subdirectory_path):
        print(f"Cannot find role-description for '{subdirectory_path}'. Using default role.")
        subdirectory_path = os.path.join(roles_directory, default_subdirectory_name)

    if os.path.exists(subdirectory_path) and os.path.isdir(subdirectory_path):
        entries = os.listdir(subdirectory_path)
        files = [os.path.abspath(os.path.join(subdirectory_path, entry))
            for entry in entries
                if os.path.isfile(os.path.join(subdirectory_path, entry)) and entry.endswith('.txt')]
        files = sorted(files)
        return files
    else:
        print(f"Error: '{default_subdirectory_name}' does not exist in '{roles_directory}'.")
        return []

