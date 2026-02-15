import sys
import os

def err_detail():
    _,_,exc_tb=sys.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    line_number=exc_tb.tb_lineno
    error_message=str(sys.exc_info())
    return f"Error occurred in script: {file_name} at line number: {line_number} with error message: {error_message}"

class CustomException(Exception):
    def __init__(self, message, error_detail: sys):
        super().__init__(message)
        self.error_detail = err_detail()

    def __str__(self):
        return self.error_detail