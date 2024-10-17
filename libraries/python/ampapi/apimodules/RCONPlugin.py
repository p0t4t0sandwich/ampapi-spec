# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class RCONPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the RCONPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def Dummy(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("RCONPlugin/Dummy", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def DummyAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("RCONPlugin/Dummy", { 
        })
        if response == None:
            response = {}
        return Void(**response)

