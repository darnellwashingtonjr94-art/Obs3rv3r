class FailoverManager:
    def __init__(self, primary: str, fallback: str):
        self.primary = primary
        self.fallback = fallback

    async def execute_with_fallback(self, call_func, *args, **kwargs):
        try:
            return await call_func(self.primary, *args, **kwargs)
        except Exception:
            return await call_func(self.fallback, *args, **kwargs)
