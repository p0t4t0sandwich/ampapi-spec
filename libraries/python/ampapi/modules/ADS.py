#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from ampapi.apimodules.ADSModule import ADSModule
from ampapi.modules.CommonAPI import CommonAPI
from ampapi.modules.GenericModule import GenericModule
from ampapi.modules.Minecraft import Minecraft
from ampapi.types import LoginResult


class ADS(CommonAPI):
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = ""):
        super().__init__(baseUri, username, password, rememberMeToken, sessionId)
        self.ADSModule = ADSModule(self)

    def Login(self) -> LoginResult:
        """
        Simplified login function
        :returns: The result of the login
        :rtype: LoginResult
        """
        loginResult: LoginResult = super().Login()
        if loginResult.success == True:
            self.rememberMeToken = loginResult.rememberMeToken
            self.sessionId = loginResult.sessionID

            # Update the session ID and remember me token of submodules
            self.ADSModule.sessionId = self.sessionId
            self.ADSModule.rememberMeToken = self.rememberMeToken

        return loginResult

    async def LoginAsync(self) -> LoginResult:
        """
        Simplified login function
        :returns: The result of the login
        :rtype: LoginResult
        """
        loginResult: LoginResult = await super().LoginAsync()
        if loginResult.success == True:
            self.rememberMeToken = loginResult.rememberMeToken
            self.sessionId = loginResult.sessionID

            # Update the session ID and remember me token of submodules
            self.ADSModule.sessionId = self.sessionId
            self.ADSModule.rememberMeToken = self.rememberMeToken

        return loginResult

    def InstanceLogin(self, instance_id: str, module: str) -> CommonAPI:
        """
        Proxies a login request to an instance and returns a new AMPAPI for that instance.
        :param instance_id: The instance ID to login to
        :param module: The module the instance is running
        :returns: A new AMPAPI instance for the instance
        """
        data = {
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": True,
        }

        loginResult: LoginResult = LoginResult(**(self.api_call("ADSModule/Servers/" + instance_id + "/API/Core/Login", data)))

        if loginResult.success == True:
            newBaseUri = self.baseUri + "API/ADSModule/Servers/" + instance_id
            rememberMeToken: str = loginResult.rememberMeToken
            sessionId: str = loginResult.sessionID

            # Return the correct module
            newInstance: CommonAPI = None

            if module == "ADS":
                newInstance = ADS(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            elif module == "GenericModule":
                newInstance = GenericModule(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            elif module == "Minecraft":
                newInstance = Minecraft(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            else:
                newInstance = CommonAPI(newBaseUri, self.username, self.password, rememberMeToken, sessionId)

            newInstance.Login()
            return newInstance
        else:
            return None

    async def InstanceLoginAsync(self, instance_id: str, module: str) -> CommonAPI:
        """
        Proxies a login request to an instance and returns a new AMPAPI for that instance.
        :param instance_id: The instance ID to login to
        :param module: The module the instance is running
        :returns: A new AMPAPI instance for the instance
        """
        data = {
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": True,
        }

        loginResult: LoginResult = LoginResult(**(await self.api_call_async("ADSModule/Servers/" + instance_id + "/API/Core/Login", data)))

        if loginResult.success == True:
            newBaseUri = self.baseUri + "API/ADSModule/Servers/" + instance_id
            rememberMeToken: str = loginResult.rememberMeToken
            sessionId: str = loginResult.sessionID

            # Return the correct module
            newInstance: CommonAPI = None

            if module == "ADS":
                newInstance = ADS(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            elif module == "GenericModule":
                newInstance = GenericModule(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            elif module == "Minecraft":
                newInstance = Minecraft(newBaseUri, self.username, self.password, rememberMeToken, sessionId)
            else:
                newInstance = CommonAPI(newBaseUri, self.username, self.password, rememberMeToken, sessionId)

            await newInstance.LoginAsync()
            return newInstance
        else:
            return None
