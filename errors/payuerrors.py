class BadRequestError(Exception):
    def __init__(self, message=None, *args, **kwargs):
        super(BadRequestError, self).__init__(message)
