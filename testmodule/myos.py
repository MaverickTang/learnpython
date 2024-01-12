import os

def get_cr3_files(directory_path):
    cr3_files = []  # Initialize an empty list to store .CR3 filenames

    # Loop through each filename in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".jpg"):  # Check if the file has a .CR3 extension
            cr3_files.append(filename)  # Append the filename to the list
    
    return cr3_files  # Return the list of .CR3 filenames

# Example usage
directory_path = "/Users/mt/Desktop/Desktop/photos/6.29上海/杭州"  # Replace with your directory path
cr3_files = get_cr3_files(directory_path)
print(cr3_files)
