import logging
from sentry_sdk import capture_exception
from rest_framework.response import Response
from rest_framework import status
logger = logging.getLogger(__name__)

def handler_creat_view(view_instace,request, *args, **kwargs):

    try:
        logger.info(f"[REGISTER] Tentative de creation {request.data}")
        response= super(view_instace.__class__, view_instace).create(request, *args, **kwargs)
        logger.info(f"[REGISTER] Utilisateur créé {response.data}")
        return response
    except Exception as e:
        # Log the exception
        logger.error(f"[REGISTER ERROR] Erreur: {str(e)}",exc_info=True)
        # Capture the exception with Sentry
        capture_exception(e)
        return Response(
            {"error": "Une erreur est survenue lors de l'inscription."},
              status=status.HTTP_500_INTERNAL_SERVER_ERROR
              )