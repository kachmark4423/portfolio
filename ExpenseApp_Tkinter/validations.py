import os

def check_file_existance(file_path):
    '''
        This function checks whether or not the given file path exists

        Parameters:
        -----------
        file_path: str
            the path of the file that is being checked for existence


        Return:
        -----------
        True/False: Bool
            boolean value from the check
    '''
    if os.path.exists(file_path):
        return True
    else:
        return False
    
