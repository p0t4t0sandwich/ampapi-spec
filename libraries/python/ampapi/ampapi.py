from typing import Any

from .auth import AuthProvider

class AMPAPI():
    """Class for interacting with the AMP API"""
    _authprovider: AuthProvider

    def __init__(self, authprovider: AuthProvider) -> None:
        self._authprovider = authprovider

    def api_call(self, endpoint: str, args: dict) -> dict[str, Any]:
        return self._authprovider.api_call(endpoint, args)
