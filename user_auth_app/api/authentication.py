from rest_framework.authentication import BaseAuthentication


class CookieTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token_key = request.COOKIES.get('user_token')
        if not token_key:
            return None
        return (None, token_key)