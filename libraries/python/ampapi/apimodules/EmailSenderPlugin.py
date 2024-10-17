# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class EmailSenderPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the EmailSenderPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def TestSMTPSettings(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("EmailSenderPlugin/TestSMTPSettings", { 
        })
        return ActionResult(**response)

    async def TestSMTPSettingsAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("EmailSenderPlugin/TestSMTPSettings", { 
        })
        return ActionResult(**response)

