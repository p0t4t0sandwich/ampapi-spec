from abc import ABCMeta, abstractmethod
from collections import namedtuple
from typing import Any, Final, overload

from requests import request as sync_request

from .types import APIError, LoginResponse

class AMPAPIException(Exception):
    def __init__(self, error: APIError) -> None:
        super().__init__(f"{error.Title}: {error.Message}\n{error.StackTrace}")

_headers: dict = {
    "Content-Type": "application/json",
    "Accept": "text/javascript",
    "User-Agent": "ampapi-py/1.4.0"
}

def api_call(endpoint: str, requestMethod: str, args: dict) -> dict[str, Any]:
    """
    Top-level function to make AMP API calls
    :param endpoint: The endpoint to call
    :type endpoint: str
    :param requestMethod: The request method to use
    :type requestMethod: str
    :param data: The data to send to the endpoint
    :type args: dict
    :returns: json dict with the result of the API call
    """
    response: dict[str, Any] = sync_request(requestMethod, endpoint, headers=_headers, json=args)
    if isinstance(response, dict) and "StackTrace" in response.keys():
        raise AMPAPIException(APIError(**response))
    return response

class AuthProvider(metaclass=ABCMeta):
    """
    Abstract class for authentication providers
    """
    dataSource: Final[str]
    requestMethod: Final[str]
    username: Final[str]
    password: Final[str]
    token: str
    rememberMe: Final[bool]
    sessionId: str
    instanceName: str
    instanceId: str

    @abstractmethod
    def __init__(self, panelUrl: str = "", requestMethod = "", username: str = "", password: str = "", token: str = "", rememberMe: bool = False, sessionId: str = "") -> None:
        pass

    @abstractmethod
    def api_call(self, endpoint: str, args: dict = {}) -> dict[str, Any]:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type args: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: Any
        """
        pass

    @abstractmethod
    def Login(self, rememberMe: bool = False) -> LoginResponse:
        pass

class AuthStore:
    _authProviders: dict[str, AuthProvider] = {}

    def __init__(self) -> None:
        pass

    def get(self, instanceId: str) -> AuthProvider:
        return self._authProviders[instanceId]

    @overload
    def add(self, authProvider: AuthProvider) -> None:
        self.add(authProvider.instanceId, authProvider)

    def add(self, instanceId: str, authProvider: AuthProvider) -> None:
        self._authProviders[instanceId] = authProvider

    def remove(self, instanceId: str) -> None:
        del self._authProviders[instanceId]

class BasicAuthProvider(AuthProvider):
    def __init__(self, panelUrl: str = "", requestMethod: str = "POST", username: str = "", password: str = "", token: str = "", rememberMe: bool = False, sessionId: str = "") -> None:
        if panelUrl == "":
            raise ValueError("Panel URL must be defined")
        if username == "" and sessionId == "":
            raise ValueError("Username must be defined")
        if password == "" and token == "" and sessionId == "":
            raise ValueError("You must provide a Password, Token, or a SessionId")
        if rememberMe:
            raise ValueError("This AuthProvider does not support rememberMe")

        if not panelUrl.endswith("/"):
            panelUrl += "/"
        self.dataSource = panelUrl + "API/"
        self.requestMethod = requestMethod
        self.username = username
        self.password = password
        self.token = token
        self.rememberMe = rememberMe
        self.sessionId = sessionId

    def api_call(self, endpoint: str, args: dict = {}) -> dict[str, Any]:
        if self.sessionId == "":
            self.Login()
        args.set("SESSIONID", self.sessionId)
        return api_call(self.dataSource + endpoint, self.requestMethod, args)

    def Login(self, rememberMe: bool = False) -> LoginResponse:
        args: dict[str, Any] = {
            "username": self.username,
            "password": self.password,
            "token": self.token,
            "rememberMe": False
        }
        response: dict[str, Any] = api_call(self.dataSource + "Core/Login", self.requestMethod, args)
        loginResponse = LoginResponse(**response)
        self.sessionId = loginResponse.sessionID
        return loginResponse
