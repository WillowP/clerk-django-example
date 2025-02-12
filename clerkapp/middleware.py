from django.conf import settings
from clerk_backend_api.jwks_helpers import verify_token, VerifyTokenOptions, TokenVerificationError

class ClerkAuthMiddleware:
    """
    Middleware that adds a `clerk_user` attribute to request objects
    before the view is called.

    The `clerk_user` attribute is simply the value returned by `verify_token` if valid,
    or `None` if the token verification fails.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        # Strip the "Bearer " prefix from the header
        token = request.headers['Authorization'][7:]
        try:
            request.clerk_user = verify_token(token, VerifyTokenOptions(
                secret_key=settings.CLERK_SECRET_KEY,
                authorized_parties=settings.CLERK_ALLOWED_PARTIES
            ))

        except TokenVerificationError:
            request.clerk_user = None

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
