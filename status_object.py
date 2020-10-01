class Status:
    def __init__(name: str, error_class: Optional[type]=None, error: Optional[BaseException] = None, tb: Optional[traceback] = None, Optional[logger_info] = None, Optional[error_text] = None):
        self.name = name
        self.error_class = error_class
        self.tb = tb
        self.logger_info = logger_info
        self.error_text = error_text

    def __del__:
        self.name = None
        self.error_class = None
        self.tb = None
        self.logger_info = None
        self.error_text = None

    def clean():
        self.name = None
        self.error_class = None
        self.tb = None
        self.logger_info = None
        self.error_text = None

