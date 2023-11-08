import sys


def error_mssg_detail(error, error_detail: sys):
    # will give us error info
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    err_info = str(error)
    error_message = f"Error occured in script : {file_name}. \nAt line no. : {line_no}.\nError message : {err_info}"

    return error_message


class CustomExceptionHandling(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_mssg_detail(
            error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message
