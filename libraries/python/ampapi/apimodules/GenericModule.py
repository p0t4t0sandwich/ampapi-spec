# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class GenericModule(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the GenericModule class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def ImportConfig(self, filename: str) -> dict[str, str]:
        """
        Name Description Optional
        :param filename: {str}  False
        :returns: dict[str, str]
        """
        response: dict = self.api_call("GenericModule/ImportConfig", { 
            "filename": filename,
        })
        return response

    async def ImportConfigAsync(self, filename: str) -> dict[str, str]:
        """
        Name Description Optional
        :param filename: {str}  False
        :returns: dict[str, str]
        """
        response: dict = await self.api_call_async("GenericModule/ImportConfig", { 
            "filename": filename,
        })
        return response

    def ReloadGenericConfig(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("GenericModule/ReloadGenericConfig", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def ReloadGenericConfigAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("GenericModule/ReloadGenericConfig", { 
        })
        if response == None:
            response = {}
        return Void(**response)

