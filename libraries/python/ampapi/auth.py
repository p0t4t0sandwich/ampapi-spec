from abc import ABCMeta, abstractmethod
from aiohttp import ClientSession as async_request
from dataclass_wizard import LoadMeta, fromdict, fromlist
from requests import request as sync_request
from time import time
from typing import Any, Final, _GenericAlias, overload
from types import GenericAlias, MethodType, NoneType

from .types import ActionResult, ErrorResponse, LoginResponse, ModuleInfo

class APIException(Exception):
    def __init__(self, error: ErrorResponse) -> None:
        super().__init__(f"{error.Title}: {error.Message}\n{error.StackTrace}")

class LoginException(Exception):
    def __init__(self, login_response: LoginResponse) -> None:
        super().__init__(login_response.resultReason + ": " + login_response.result + "\n" + login_response)

def json_to_obj(json: dict[str, Any] | list[Any] | Any, ret_class: type) -> Any:
    if ret_class is None or isinstance(ret_class, NoneType):
        return None
    elif ret_class in [str, int, float, bool]:
        return ret_class(json)
    elif isinstance(json, dict):
        # Check to see if ret_class is a nested dict
        if hasattr(ret_class, "__args__") and len(ret_class.__args__) == 2:
            val_type = ret_class.__args__[1]
            dct = {}
            for key, value in json.items():
                dct[key] = json_to_obj(value, val_type)
            return dct
        # Handle ActionResult
        elif issubclass(type(ret_class), (_GenericAlias, GenericAlias)) and ret_class.__origin__ == ActionResult:
            args = ret_class.__args__
            ret_class = ActionResult
            if "result" in json.keys():
                if len(args) >= 1:
                    inner_type = args[0]
                    json["result"] = json_to_obj(json["result"], inner_type)
            else:
                json["result"] = None
        elif issubclass(ret_class, ActionResult):
            json["result"] = None
    elif isinstance(json, list):
        # Get list inner type
        inner_type = ret_class.__args__[0]
        return fromlist(inner_type, json)
    return fromdict(ret_class, json)

def strict_json_to_obj(json: dict[str, Any], ret_class: type) -> Any:
    LoadMeta(raise_on_unknown_json_key=True,debug_enabled=True).bind_to(ret_class)
    if ret_class is None or isinstance(ret_class, NoneType):
        return None
    elif ret_class in [str, int, float, bool]:
        return ret_class(json)
    elif isinstance(json, dict):
        # Check to see if ret_class is a nested dict
        if hasattr(ret_class, "__args__") and len(ret_class.__args__) == 2:
            val_type = ret_class.__args__[1]
            dct = {}
            for key, value in json.items():
                dct[key] = json_to_obj(value, val_type)
            return dct
        # Handle ActionResult
        elif issubclass(type(ret_class), (_GenericAlias, GenericAlias)) and ret_class.__origin__ == ActionResult:
            args = ret_class.__args__
            ret_class = ActionResult
            if "result" in json.keys():
                if len(args) >= 1:
                    inner_type = args[0]
                    LoadMeta(raise_on_unknown_json_key=True,debug_enabled=True).bind_to(inner_type)
                    json["result"] = json_to_obj(json["result"], inner_type)
            else:
                json["result"] = None
        elif issubclass(ret_class, ActionResult):
            json["result"] = None
    elif isinstance(json, list):
        # Get list inner type
        inner_type = ret_class.__args__[0]
        LoadMeta(raise_on_unknown_json_key=True,debug_enabled=True).bind_to(inner_type)
        return fromlist(inner_type, json)
    return fromdict(ret_class, json)

_headers: dict[str, str] = {
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
    response = sync_request(requestMethod, endpoint, headers=_headers, json=args)
    response_json: dict[str, Any] = response.json()
    if isinstance(response_json, dict) and "StackTrace" in response_json.keys():
        raise APIException(fromdict(ErrorResponse, response_json))
    return response_json

async def api_call_async(endpoint: str, requestMethod: str, args: dict) -> dict[str, Any]:
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
    async with async_request() as session:
        response = await session.request(requestMethod, endpoint, headers=_headers, json=args)
        response_json: dict[str, Any] = await response.json()
        if isinstance(response_json, dict) and "StackTrace" in response_json.keys():
            raise APIException(fromdict(ErrorResponse, response_json))
        return response_json

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
    _instanceName: str = ""
    _instanceId: str = ""

    @property
    def instanceName(self) -> str:
        if self._instanceName == "":
            self.UpdateModuleInfo()
        return self._instanceName

    @instanceName.setter
    def instanceName(self, value: str) -> None:
        self._instanceName = value

    @instanceName.deleter
    def instanceName(self) -> None:
        self._instanceName = ""

    @property
    def instanceId(self) -> str:
        if self._instanceId == "":
            self.UpdateModuleInfo()
        return self._instanceId

    @instanceId.setter
    def instanceId(self, value: str) -> None:
        self._instanceId = value

    @instanceId.deleter
    def instanceId(self) -> None:
        self._instanceId = ""

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

    @abstractmethod
    def UpdateModuleInfo(self) -> ModuleInfo:
        pass

class AuthProviderAsync(AuthProvider, metaclass=ABCMeta):
    @property
    async def instanceName(self) -> str:
        if self._instanceName == "":
            await self.UpdateModuleInfo()
        return self._instanceName

    @property
    async def instanceId(self) -> str:
        if self._instanceId == "":
            await self.UpdateModuleInfo()
        return self._instanceId

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
    def __init__(self,
                panelUrl: str = "",
                requestMethod: str = "POST",
                username: str = "",
                password: str = "",
                token: str = "",
                rememberMe: bool = False,
                sessionId: str = "") -> None:
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
        args["SESSIONID"] = self.sessionId
        return api_call(self.dataSource + endpoint, self.requestMethod, args)

    def Login(self, rememberMe: bool = False) -> LoginResponse:
        args: dict[str, Any] = {
            "username": self.username,
            "password": self.password,
            "token": self.token,
            "rememberMe": False
        }
        response: dict[str, Any] = api_call(self.dataSource + "Core/Login", self.requestMethod, args)
        login_response = fromdict(LoginResponse, response)
        if not login_response.success:
            raise LoginException(login_response)
        self.sessionId = login_response.sessionID
        return login_response

    def UpdateModuleInfo(self) -> ModuleInfo:
        response: dict[str, Any] = self.api_call("Core/GetModuleInfo")
        module_info = fromdict(ModuleInfo, response)
        self._instanceName = module_info.InstanceName
        self._instanceId = module_info.InstanceId
        return module_info

class BasicAuthProviderAsync(AuthProviderAsync):
    def __init__(self,
                panelUrl: str = "",
                requestMethod: str = "POST",
                username: str = "",
                password: str = "",
                token: str = "",
                rememberMe: bool = False,
                sessionId: str = "") -> None:
        if panelUrl == "":
            raise ValueError("Panel URL must be defined")
        if username == "" and sessionId == "":
            raise ValueError("Username must be defined")
        if password == "" and token == "" and sessionId == "":
            raise ValueError("You must provide a Password, Token, or a SessionId")
        if not panelUrl.endswith("/"):
            panelUrl += "/"
        self.dataSource = panelUrl + "API/"
        self.requestMethod = requestMethod
        self.username = username
        self.password = password
        self.token = token
        self.rememberMe = rememberMe
        self.sessionId = sessionId

    async def api_call(self, endpoint: str, args: dict = {}) -> dict[str, Any]:
        if self.sessionId == "":
            await self.Login()
        args["SESSIONID"] = self.sessionId
        return await api_call_async(self.dataSource + endpoint, self.requestMethod, args)

    async def Login(self, rememberMe: bool = False) -> LoginResponse:
        args: dict[str, Any] = {
            "username": self.username,
            "password": self.password,
            "token": self.token,
            "rememberMe": False
        }
        response: dict[str, Any] = await api_call_async(self.dataSource + "Core/Login", self.requestMethod, args)
        login_response = fromdict(LoginResponse, response)
        if not login_response.success:
            raise LoginException(login_response)
        self.sessionId = login_response.sessionID
        return login_response

    async def UpdateModuleInfo(self) -> ModuleInfo:
        response: dict[str, Any] = await self.api_call("Core/GetModuleInfo")
        module_info = fromdict(ModuleInfo, response)
        self._instanceName = module_info.InstanceName
        self._instanceId = module_info.InstanceId
        return module_info

class RefreshingAuthProvider(BasicAuthProvider):
    relogInterval: Final[int]
    relogCallback: MethodType
    _lastCall: int = round(time())

    def __init__(self,
                panelUrl: str = "",
                requestMethod: str = "POST",
                username: str = "",
                password: str = "",
                token: str = "",
                rememberMe: bool = True,
                sessionId: str = "",
                relogInterval: int = 60 * 5,
                relogCallback: MethodType = None) -> None:
        if panelUrl == "":
            raise ValueError("Panel URL must be defined")
        if username == "" and sessionId == "":
            raise ValueError("Username must be defined for refreshing auth")
        if password == "" and token == "" and sessionId == "":
            raise ValueError("You must provide a Password or a valid RememberMe Token for refreshing auth")
        if not panelUrl.endswith("/"):
            panelUrl += "/"
        self.relogInterval = relogInterval
        if not relogCallback is None:
            self.relogCallback = relogCallback
        else:
            self.relogCallback = self.Login
        self.dataSource = panelUrl + "API/"
        self.requestMethod = requestMethod
        self.username = username
        self.password = password
        self.token = token
        self.rememberMe = rememberMe
        self.sessionId = sessionId

    def api_call(self, endpoint: str, args: dict = {}) -> dict[str, Any]:
        now: int = round(time())
        if now - self._lastCall > self.relogInterval:
            print("Relogging")
            self.relogCallback()

        self._lastCall = now
        if self.sessionId == "":
            self.Login()
        args["SESSIONID"] = self.sessionId
        return api_call(self.dataSource + endpoint, self.requestMethod, args)

    def Login(self, rememberMe: bool = True) -> LoginResponse:
        args: dict[str, Any] = { "username": self.username }
        if rememberMe and self.token != "":
            args["password"] = ""
            args["token"] = self.token
        else:
            args["password"] = self.password
            args["token"] = ""
        args["rememberMe"] = rememberMe

        response: dict[str, Any] = api_call(self.dataSource + "Core/Login", self.requestMethod, args)
        login_response = fromdict(LoginResponse, response)
        if not login_response.success:
            raise LoginException(login_response)
        self.token = login_response.rememberMeToken
        self.sessionId = login_response.sessionID
        return login_response

class RefreshingAuthProviderAsync(BasicAuthProviderAsync):
    relogInterval: Final[int]
    relogCallback: MethodType
    _lastCall: int = round(time())

    def __init__(self,
                panelUrl: str = "",
                requestMethod: str = "POST",
                username: str = "",
                password: str = "",
                token: str = "",
                rememberMe: bool = True,
                sessionId: str = "",
                relogInterval: int = 60 * 5,
                relogCallback: MethodType = None) -> None:
        if panelUrl == "":
            raise ValueError("Panel URL must be defined")
        if username == "" and sessionId == "":
            raise ValueError("Username must be defined for refreshing auth")
        if password == "" and token == "" and sessionId == "":
            raise ValueError("You must provide a Password or a valid RememberMe Token for refreshing auth")
        if not panelUrl.endswith("/"):
            panelUrl += "/"
        self.relogInterval = relogInterval
        if not relogCallback is None:
            self.relogCallback = relogCallback
        else:
            self.relogCallback = self.Login
        self.dataSource = panelUrl + "API/"
        self.requestMethod = requestMethod
        self.username = username
        self.password = password
        self.token = token
        self.rememberMe = rememberMe
        self.sessionId = sessionId

    async def api_call(self, endpoint: str, args: dict = {}) -> dict[str, Any]:
        now: int = round(time())
        if now - self._lastCall > self.relogInterval:
            await self.relogCallback()

        self._lastCall = now
        if self.sessionId == "":
            await self.Login()
        args["SESSIONID"] = self.sessionId
        return await api_call_async(self.dataSource + endpoint, self.requestMethod, args)

    async def Login(self, rememberMe: bool = True) -> LoginResponse:
        args: dict[str, Any] = { "username": self.username }
        if rememberMe and self.token != "":
            args["password"] = ""
            args["token"] = self.token
        else:
            args["password"] = self.password
            args["token"] = ""
        args["rememberMe"] = rememberMe

        response: dict[str, Any] = await api_call_async(self.dataSource + "Core/Login", self.requestMethod, args)
        login_response = fromdict(LoginResponse, response)
        if not login_response.success:
            raise LoginException(login_response)
        self.token = login_response.rememberMeToken
        self.sessionId = login_response.sessionID
        return login_response
