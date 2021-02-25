#!/usr/bin/env python3

# test application.py

# Imports
from application import *


# Functions
def test_get_os(mocker):  # must import 'mocker' as parameter
    mocker.patch("application.is_windows", return_value = True) # mock function
    assert get_operating_system() == "Windows"


def main():
    result = get_operating_system()
    print(result)


if __name__ == "__main__":
    main()




# application.py 
# from https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606

#from time import sleep  

#def is_windows():    
#    # This sleep could be some complex operation instead
#    sleep(5)    
#    return True  
#
#def get_operating_system():    
#    return 'Windows' if is_windows() else 'Linux'
