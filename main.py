import os


files_extensions = ('.jpg', '.png', '.PNG')
def get_file_last_modified_date(file_name, file_path):
    try:
        decoded_file_path = os.fsdecode(file_path)
        modification_time = os.path.getmtime(f'{decoded_file_path}/{file_name}')
    except OSError:
        modification_time = 0
    return modification_time

def get_all_files(files_path):
    directory = os.fsencode(files_path)
    for files in os.listdir(directory):
        filename = os.fsdecode(files)
        if filename.endswith(files_extensions):
            
            print(get_file_last_modified_date(filename, directory))



if __name__ == "__main__":
    files_path = '/home/albin/Pictures'
    get_all_files(files_path)
