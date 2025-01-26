import os 
import time
from typing import Dict, List, Set

# Log File Path
file_path = os.getcwd() + "\\PythonCodeHub\\Modules\\Logs\\DataLog.log"
file_mode = "r"

class Example():
    """This Class illustrates exception handling
    Note: When you use 'with' statement with open function, you do not need to close the file at the end, because 'with' would automatically close it for you
    """
    def __init__(self, log_file_path: str='') -> None:
        """This is class constructor
        Args:
            log_file_path (str, optional): This argument holds log file path information. Defaults to ''.
        """
        self.log_file_path = log_file_path
    
    def read_log_file(self) -> None:
        """This functions illustrates automatic file closing example i.e., [with open] while reading log file
        """
        with open(self.log_file_path) as f:
            print("Is file closed during with logic ? --> ", f.closed)
            for row in f.readlines():
                try:
                    if "*" in row:
                        raise Exception("Manual Exception raised due to special character i.e., * ")
                except Exception as error:
                    print("Error --> %s" % (error))
                    pass
                    #'pass' statement simply does nothing. 
                    #We can use 'pass' statement when we want to create a method that we didn't wrote implementation logic, yet.
                    #Where 'continue' statement skip all the remaining statements in the loop and goes back to the starting of the loop
        print("Is file closed after with logic ? --> ", f.closed)

if __name__ == "__main__":
    print("**"*25)
    print("Context Manager Example : with + open")
    print("**"*25)
    ctx_mngr = Example(log_file_path=file_path)
    ctx_mngr.read_log_file()

# **************************************************
# Context Manager Example : with + open
# **************************************************
# Is file closed during with logic ? -->  False
# Error --> Manual Exception raised due to special character i.e., *
# Error --> Manual Exception raised due to special character i.e., *
# Is file closed after with logic ? -->  True
