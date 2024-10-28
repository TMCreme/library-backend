from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    """
    Calls framework's default exception handler to get the standard error response.
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status_code'] = response.status_code
    return response