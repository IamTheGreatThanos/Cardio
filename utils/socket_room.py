from channels.auth import AuthMiddlewareStack


class TokenAuthMiddleware:

    def __init__(self, inner):
        self.inner = inner

    def __call__(self, scope):
        query = dict((x.split('=') for x in scope['query_string'].decode().split("&")))
        if "wid" in query.keys():
            t = query['wid']
            # print(t)
            scope['id'] = t
        return self.inner(scope)

TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(AuthMiddlewareStack(inner))