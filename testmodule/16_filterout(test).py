import os
import shutil

def list_subfolders(start_folder):
    folder_list = []  # Initialize an empty list to store folder paths
    for root, dirs, files in os.walk(start_folder):  # Iterate through the directory tree
        for name in dirs:  # Loop through each subdirectory
            full_path = os.path.join(root, name)  # Get the full path of the subdirectory
            folder_list.append(full_path)  # Append the full path to the list
    return folder_list  # Return the list of folder paths

def list_files_in_folder(folder_path):
    file_list = []  # Initialize an empty list to store file names
    
    if os.path.exists(folder_path):  # Check if the folder exists
        for filename in os.listdir(folder_path):  # Loop through each file and subfolder
            if os.path.isfile(os.path.join(folder_path, filename)):  # Check if it's a file
                file_list.append(filename)  # Append the filename to the list
    
    return file_list  # Return the list of file names

def extract_and_unique_prefix(str_array):
    prefix_set = set()  # Use a set to store unique prefixes
    result = []  # List to store the final unique prefixes
    for item in str_array:  # Loop through each string in the input array
        prefix = item.split('.')[0]  # Extract the substring before '.'
        if prefix not in prefix_set:  # Check if prefix is unique
            prefix_set.add(prefix)  # Add it to the set
            result.append(prefix)  # Append it to the result list
    return result  # Return the unique prefixes

# def move_files(file_names, source_folder, target_folder):
#     # Create target folder if it does not exist
#     if not os.path.exists(target_folder):
#         os.makedirs(target_folder)

#     # Create a set to store the names of existing files without suffixes
#     existing_files_no_suffix = set()

#     # Populate the set with file names (without suffixes) from the source folder
#     for existing_file in os.listdir(source_folder):
#         name_without_suffix = os.path.splitext(existing_file)[0]  # Get file name without suffix
#         existing_files_no_suffix.add(name_without_suffix)

#     # Loop through each file name in the given array
#     for file_name in file_names:
#         # Check if the file name (without suffix) exists in the source folder
#         if file_name in existing_files_no_suffix:
#             # Find the full file name with suffix
#             for existing_file in os.listdir(source_folder):
#                 if os.path.splitext(existing_file)[0] == file_name:
#                     source_file_path = os.path.join(source_folder, existing_file)
#                     target_file_path = os.path.join(target_folder, existing_file)
#                     shutil.copy(source_file_path, target_file_path)  # Move the file
#                     print(f"Moved {existing_file} to {target_folder}")
#                     break  # Exit the loop once the file is found and moved
#         else:
#             print(f"{file_name} not found in {source_folder}")

def move_files_with_names_and_suffix(file_names, source_folder, target_folder):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
        
    # Iterate over all files in the source folder
    for file in os.listdir(source_folder):
        # Split the file name into name and suffix
        name, suffix = os.path.splitext(file)
        # Check if the name is in the list and the suffix is '.CR3'如果是jpg则应该是JPEG
        if name in file_names and suffix.upper() == '.JPG':
            source_file_path = os.path.join(source_folder, file)
            target_file_path = os.path.join(target_folder, file)
            # Move the file
            shutil.copy(source_file_path, target_file_path)
            print(f"Moved {file} to {target_folder}")



if __name__ == "__main__":
    # 大文件夹
    # start_folder = "/Users/mt/Desktop/travel/摄影/23.10理工"  # Replace with the path of your folder
    # folder_path=list_subfolders(start_folder)
    # for folder in folder_path:
    #     print(folder)
    #     original_file_name=list_files_in_folder(folder)
    #     print(original_file_name)
    #     filtered_file=extract_and_unique_prefix(original_file_name)
    #     print(filtered_file)
    #     move_files_with_names_and_suffix(filtered_file, '/Volumes/CanonR6/DCIM/100CANON', '/Volumes/TangSSD/摄影/save')

    # 小文件夹
    folder="/Users/mt/Desktop/travel/摄影/23.10理工"
    print(folder)
    original_file_name=list_files_in_folder(folder)
    print(original_file_name)
    filtered_file=extract_and_unique_prefix(original_file_name)
    print(filtered_file)
    move_files_with_names_and_suffix(filtered_file, '/Volumes/CanonR6/DCIM/100CANON', '/Volumes/TangSSD/摄影/save')