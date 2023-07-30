import os
import argparse
import logging
from collections import namedtuple

# Configure logging
logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define namedtuple for storing file information
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def gather_content_info(directory_path):
    content_info = []

    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        name, extension = os.path.splitext(entry)
        is_directory = os.path.isdir(full_path)

        parent_directory = os.path.basename(directory_path)

        info = FileInfo(name=name, extension=extension if not is_directory else None,
                        is_directory=is_directory, parent_directory=parent_directory)
        content_info.append(info)

        logging.info(f"{info}")

    return content_info

def main():
    parser = argparse.ArgumentParser(description='Gather content information about files and directories.')
    parser.add_argument('directory', type=str, help='Path to the directory on the PC')
    args = parser.parse_args()

    directory_path = args.directory

    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    content_info = gather_content_info(directory_path)

    # Save data to a text file using logging
    logging.info(f"Finished gathering content information for {directory_path}")

    # Display content information to the console
    for info in content_info:
        if info.is_directory:
            file_type = "Directory"
            extension = "N/A"
        else:
            file_type = "File"
            extension = info.extension

        print(f"{file_type}: {info.name}, Extension: {extension}, Parent Directory: {info.parent_directory}")

if __name__ == '__main__':
    main()
