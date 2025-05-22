from rest_framework.views import exception_handler
import sentry_sdk

def custom_exception_handler(exc, context): 
    response = exception_handler(exc, context)
    if response is not None and response.status_code != 500:
        # Capture the exception with Sentry
        sentry_sdk.capture_exception(exc)
    return response
        # Optionally, you can also log the exception or perform other actions here