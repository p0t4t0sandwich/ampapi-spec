# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class steamcmdplugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the steamcmdplugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def CancelSteamGuard(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("steamcmdplugin/CancelSteamGuard", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def CancelSteamGuardAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("steamcmdplugin/CancelSteamGuard", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def SteamGuardCode(self, code: str) -> Void:
        """
        Name Description Optional
        :param code: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("steamcmdplugin/SteamGuardCode", { 
            "code": code,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SteamGuardCodeAsync(self, code: str) -> Void:
        """
        Name Description Optional
        :param code: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("steamcmdplugin/SteamGuardCode", { 
            "code": code,
        })
        if response == None:
            response = {}
        return Void(**response)

    def SteamUsernamePassword(self, username: str, password: str) -> Void:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("steamcmdplugin/SteamUsernamePassword", { 
            "username": username,
            "password": password,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SteamUsernamePasswordAsync(self, username: str, password: str) -> Void:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("steamcmdplugin/SteamUsernamePassword", { 
            "username": username,
            "password": password,
        })
        if response == None:
            response = {}
        return Void(**response)

