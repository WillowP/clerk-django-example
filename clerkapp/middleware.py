from django.conf import settings
from clerk_backend_api.jwks_helpers import verify_token, VerifyTokenOptions, TokenVerificationError

class ClerkAuthMiddleware:
    """
    Middleware that adds a `verified_clerk_token` attribute to request objects
    before the view is called, which is `None` if the token verification failed,
    or the decoded access token if it succeeded.
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
            request.verified_clerk_token = verify_token(token, VerifyTokenOptions(
                secret_key=settings.CLERK_SECRET_KEY,
                authorized_parties=settings.CLERK_AUTHORIZED_PARTIES,
            ))

        except TokenVerificationError:
            request.verified_clerk_token = None

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
