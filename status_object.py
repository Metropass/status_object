class Status:
    def __init__(name: str, error_class: Optional[type]=None, error: Optional[BaseException] = None, tb: Optional[traceback] = None, logger_info: Optional[logger_info] = None, error_text: Optional[error_text] = None):
        self.name = name
        self.error_class = error_class
        self.tb = tb
        self.logger_info = logger_info
        self.error_text = error_text
    
    def set_name(name):
        self.name = str(name)

