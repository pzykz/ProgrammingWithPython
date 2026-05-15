# class MyException(Exception):
#     def __init__(self, *args, **kwargs):
#         super().__init__(self, *args, **kwargs)

class MyException(Exception):
    def __init__(self, exception_parameter, exception_message):
        super().__init__(self, exception_parameter, exception_message)

class MyIndexError(IndexError):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
