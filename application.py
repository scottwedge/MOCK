# application.py 
# from https://medium.com/analytics-vidhya/mocking-in-python-with-pytest-mock-part-i-6203c8ad3606

from time import sleep  

def is_windows():    
    # This sleep could be some complex operation instead
    sleep(5)    
    return True  

def get_operating_system():    
    return 'Windows' if is_windows() else 'Linux'
