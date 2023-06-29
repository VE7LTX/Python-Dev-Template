# File: file_control.py
# Description: Default functions for general file control using the os and shutil libraries.

import os
import shutil

# TODO: Implement function for creating a new directory
def create_directory(directory):
    """
    Creates a new directory.
    """
    os.makedirs(directory)

# TODO: Implement function for copying files
def copy_file(source, destination):
    """
    Copies a file from the source path to the destination path.
    """
    shutil.copy(source, destination)

# TODO: Implement function for deleting a directory and its contents
def delete_directory(directory):
    """
    Deletes a directory and its contents.
    """
    shutil.rmtree(directory)

# TODO: Implement function for renaming a file
def rename_file(file_path, new_name):
    """
    Renames a file.
    """
    directory, old_name = os.path.split(file_path)
    new_file_path = os.path.join(directory, new_name)
    os.rename(file_path, new_file_path)

# TODO: Implement function for listing all files in a directory
def list_files(directory):
    """
    Lists all files in a directory.
    """
    files = os.listdir(directory)
    return files
