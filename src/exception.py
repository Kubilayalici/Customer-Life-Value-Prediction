import sys
import logging

def error_message_detail(error, exc_tb):
    """
    Formats the error message details.
    :param error: The error object.
    :param exc_tb: The traceback object.
    :return: A formatted string containing the error type, value, and traceback.
    """
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = (
        f"Error occurred in script: [{file_name}] at line number: [{line_number}] with error message: [{str(error)}]"
    )
    return error_message

class CustomException(Exception):
    """
    Custom exception class to handle exceptions in the application.
    Inherits from the built-in Exception class.
    """
    def __init__(self, error_message):
        """
        Initializes the CustomException with a formatted error message.
        :param error_message: The error message to be displayed.
        """
        _, _, exc_tb = sys.exc_info()
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, exc_tb)

    def __str__(self):
        return self.error_message