import traceback
from typing import Optional

class Status:
    def __init__(self,name:str = None, error_class: Optional[type] = None, tb: Optional[traceback.print_exc()] = None):
        
        self.name = name
        self.error_class = error_class
        self.tb = tb
 
    def set_name(self,s):
        self.name = str(s)
