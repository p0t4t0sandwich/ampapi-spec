#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from ampapi.apimodules.MinecraftModule import MinecraftModule
from ampapi.modules.CommonAPI import CommonAPI
from ampapi.types import LoginResult

class Minecraft(CommonAPI):
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = ""):
        super().__init__(baseUri, username, password, rememberMeToken, sessionId)
        self.MinecraftModule = MinecraftModule(self)

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
            self.MinecraftModule.sessionId = self.sessionId
            self.MinecraftModule.rememberMeToken = self.rememberMeToken

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
            self.MinecraftModule.sessionId = self.sessionId
            self.MinecraftModule.rememberMeToken = self.rememberMeToken

        return loginResult
