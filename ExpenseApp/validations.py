import os

def check_file_existance(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False
    
