class Status:
    def __init__(name: str, error_class: Optional[type]=None, error: Optional[BaseException] = None, tb: Optional[traceback] = None):
        self.name = name
        self.error_class = error_class
        self.tb = tb
 
    def set_name(name):
        self.name = str(name)

