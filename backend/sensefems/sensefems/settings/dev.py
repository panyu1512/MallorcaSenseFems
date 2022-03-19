from .base import *
import mimetypes

DEBUG=True
mimetypes.add_type("text/css", ".css", True)
CORS_ALLOWED_ORIGINS = ['http://localhost']