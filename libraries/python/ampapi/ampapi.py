from typing import Any

from .auth import AuthProvider

class AMPAPI():
    """Class for interacting with the AMP API"""
    _authprovider: AuthProvider

    def __init__(self, authprovider: AuthProvider) -> None:
        self._authprovider = authprovider

    def api_call(self, endpoint: str, args: dict) -> dict[str, Any]:
        return self._authprovider.api_call(endpoint, args)

class AMPAPIAsync(AMPAPI):
    """
    Class for interacting with the AMP API asynchronously
    Note: This class assumes that the AuthProvider is also async
    """
    _authprovider: AuthProvider

    def __init__(self, authprovider: AuthProvider) -> None:
        self._authprovider = authprovider

    async def api_call(self, endpoint: str, args: dict) -> dict[str, Any]:
        return await self._authprovider.api_call(endpoint, args)
