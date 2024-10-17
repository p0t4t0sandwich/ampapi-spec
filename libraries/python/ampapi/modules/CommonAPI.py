#!/bin/python3
# author: p0t4t0sandich
# description: A Python library for the AMP API

from ampapi.ampapi import AMPAPI
from ampapi.apimodules.Core import Core
from ampapi.apimodules.EmailSenderPlugin import EmailSenderPlugin
from ampapi.apimodules.FileManagerPlugin import FileManagerPlugin
from ampapi.apimodules.LocalFileBackupPlugin import LocalFileBackupPlugin
from ampapi.types import LoginResult


class CommonAPI(AMPAPI):
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = ""):
        super().__init__(baseUri, username, password, rememberMeToken, sessionId)
        self.Core = Core(self)
        self.EmailSenderPlugin = EmailSenderPlugin(self)
        self.FileManagerPlugin = FileManagerPlugin(self)
        self.LocalFileBackupPlugin = LocalFileBackupPlugin(self)

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
            self.Core.sessionId = self.sessionId
            self.Core.rememberMeToken = self.rememberMeToken
            self.EmailSenderPlugin.sessionId = self.sessionId
            self.EmailSenderPlugin.rememberMeToken = self.rememberMeToken
            self.FileManagerPlugin.sessionId = self.sessionId
            self.FileManagerPlugin.rememberMeToken = self.rememberMeToken
            self.LocalFileBackupPlugin.sessionId = self.sessionId
            self.LocalFileBackupPlugin.rememberMeToken = self.rememberMeToken

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
            self.Core.sessionId = self.sessionId
            self.Core.rememberMeToken = self.rememberMeToken
            self.EmailSenderPlugin.sessionId = self.sessionId
            self.EmailSenderPlugin.rememberMeToken = self.rememberMeToken
            self.FileManagerPlugin.sessionId = self.sessionId
            self.FileManagerPlugin.rememberMeToken = self.rememberMeToken
            self.LocalFileBackupPlugin.sessionId = self.sessionId
            self.LocalFileBackupPlugin.rememberMeToken = self.rememberMeToken

        return loginResult
