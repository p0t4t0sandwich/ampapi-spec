#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from ampapi.apimodules.GenericModule import GenericModule as GenericModuleAlias
from ampapi.apimodules.RCONPlugin import RCONPlugin
from ampapi.apimodules.steamcmdplugin import steamcmdplugin
from ampapi.modules.CommonAPI import CommonAPI
from ampapi.types import LoginResult

class GenericModule(CommonAPI):
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = ""):
        super().__init__(baseUri, username, password, rememberMeToken, sessionId)
        self.GenericModule = GenericModuleAlias(self)
        self.RCONPlugin = RCONPlugin(self)
        self.steamcmdplugin = steamcmdplugin(self)

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
            self.GenericModule.sessionId = self.sessionId
            self.GenericModule.rememberMeToken = self.rememberMeToken
            self.RCONPlugin.sessionId = self.sessionId
            self.RCONPlugin.rememberMeToken = self.rememberMeToken
            self.steamcmdplugin.sessionId = self.sessionId
            self.steamcmdplugin.rememberMeToken = self.rememberMeToken

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
            self.GenericModule.sessionId = self.sessionId
            self.GenericModule.rememberMeToken = self.rememberMeToken
            self.RCONPlugin.sessionId = self.sessionId
            self.RCONPlugin.rememberMeToken = self.rememberMeToken
            self.steamcmdplugin.sessionId = self.sessionId
            self.steamcmdplugin.rememberMeToken = self.rememberMeToken

        return loginResult
