# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class MinecraftModule(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the MinecraftModule class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AcceptEULA(self, ) -> bool:
        """
        Name Description Optional
        :returns: bool
        """
        response: dict = self.api_call("MinecraftModule/AcceptEULA", { 
        })
        return bool(**response)

    async def AcceptEULAAsync(self, ) -> bool:
        """
        Name Description Optional
        :returns: bool
        """
        response: dict = await self.api_call_async("MinecraftModule/AcceptEULA", { 
        })
        return bool(**response)

    def AddOPEntry(self, UserOrUUID: str) -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("MinecraftModule/AddOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        return ActionResult(**response)

    async def AddOPEntryAsync(self, UserOrUUID: str) -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("MinecraftModule/AddOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        return ActionResult(**response)

    def AddToWhitelist(self, UserOrUUID: str) -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("MinecraftModule/AddToWhitelist", { 
            "UserOrUUID": UserOrUUID,
        })
        return ActionResult(**response)

    async def AddToWhitelistAsync(self, UserOrUUID: str) -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("MinecraftModule/AddToWhitelist", { 
            "UserOrUUID": UserOrUUID,
        })
        return ActionResult(**response)

    def BanUserByID(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/BanUserByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def BanUserByIDAsync(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/BanUserByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def BukGetCategories(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetCategories", { 
        })
        return dict(**response)

    async def BukGetCategoriesAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetCategories", { 
        })
        return dict(**response)

    def BukGetInstallUpdatePlugin(self, pluginId: int) -> RunningTask:
        """
        Name Description Optional
        :param pluginId: {int}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("MinecraftModule/BukGetInstallUpdatePlugin", { 
            "pluginId": pluginId,
        })
        return RunningTask(**response)

    async def BukGetInstallUpdatePluginAsync(self, pluginId: int) -> RunningTask:
        """
        Name Description Optional
        :param pluginId: {int}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetInstallUpdatePlugin", { 
            "pluginId": pluginId,
        })
        return RunningTask(**response)

    def BukGetInstalledPlugins(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetInstalledPlugins", { 
        })
        return dict(**response)

    async def BukGetInstalledPluginsAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetInstalledPlugins", { 
        })
        return dict(**response)

    def BukGetPluginInfo(self, PluginId: int) -> dict:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetPluginInfo", { 
            "PluginId": PluginId,
        })
        return dict(**response)

    async def BukGetPluginInfoAsync(self, PluginId: int) -> dict:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetPluginInfo", { 
            "PluginId": PluginId,
        })
        return dict(**response)

    def BukGetPluginsForCategory(self, CategoryId: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param CategoryId: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetPluginsForCategory", { 
            "CategoryId": CategoryId,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })
        return dict(**response)

    async def BukGetPluginsForCategoryAsync(self, CategoryId: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param CategoryId: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetPluginsForCategory", { 
            "CategoryId": CategoryId,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })
        return dict(**response)

    def BukGetPopularPlugins(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetPopularPlugins", { 
        })
        return dict(**response)

    async def BukGetPopularPluginsAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetPopularPlugins", { 
        })
        return dict(**response)

    def BukGetRemovePlugin(self, PluginId: int) -> Void:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/BukGetRemovePlugin", { 
            "PluginId": PluginId,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def BukGetRemovePluginAsync(self, PluginId: int) -> Void:
        """
        Name Description Optional
        :param PluginId: {int}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetRemovePlugin", { 
            "PluginId": PluginId,
        })
        if response == None:
            response = {}
        return Void(**response)

    def BukGetSearch(self, Query: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param Query: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/BukGetSearch", { 
            "Query": Query,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })
        return dict(**response)

    async def BukGetSearchAsync(self, Query: str, PageNumber: int, PageSize: int) -> dict:
        """
        Name Description Optional
        :param Query: {str}  False
        :param PageNumber: {int}  False
        :param PageSize: {int}  False
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/BukGetSearch", { 
            "Query": Query,
            "PageNumber": PageNumber,
            "PageSize": PageSize,
        })
        return dict(**response)

    def ClearInventoryByID(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/ClearInventoryByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def ClearInventoryByIDAsync(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/ClearInventoryByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def GetFailureReason(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        response: dict = self.api_call("MinecraftModule/GetFailureReason", { 
        })
        return str(**response)

    async def GetFailureReasonAsync(self, ) -> str:
        """
        Name Description Optional
        :returns: str
        """
        response: dict = await self.api_call_async("MinecraftModule/GetFailureReason", { 
        })
        return str(**response)

    def GetHeadByUUID(self, id: str) -> str:
        """
        Name Description Optional
        :param id: {str}  False
        :returns: str
        """
        response: dict = self.api_call("MinecraftModule/GetHeadByUUID", { 
            "id": id,
        })
        return str(**response)

    async def GetHeadByUUIDAsync(self, id: str) -> str:
        """
        Name Description Optional
        :param id: {str}  False
        :returns: str
        """
        response: dict = await self.api_call_async("MinecraftModule/GetHeadByUUID", { 
            "id": id,
        })
        return str(**response)

    def GetOPWhitelist(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = self.api_call("MinecraftModule/GetOPWhitelist", { 
        })
        return dict(**response)

    async def GetOPWhitelistAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = await self.api_call_async("MinecraftModule/GetOPWhitelist", { 
        })
        return dict(**response)

    def GetWhitelist(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("MinecraftModule/GetWhitelist", { 
        })
        return [dict(**x) for x in response]

    async def GetWhitelistAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("MinecraftModule/GetWhitelist", { 
        })
        return [dict(**x) for x in response]

    def KickUserByID(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/KickUserByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def KickUserByIDAsync(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/KickUserByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def KillByID(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/KillByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def KillByIDAsync(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/KillByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def LoadOPList(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("MinecraftModule/LoadOPList", { 
        })
        return [dict(**x) for x in response]

    async def LoadOPListAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("MinecraftModule/LoadOPList", { 
        })
        return [dict(**x) for x in response]

    def RemoveOPEntry(self, UserOrUUID: str) -> Void:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/RemoveOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RemoveOPEntryAsync(self, UserOrUUID: str) -> Void:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/RemoveOPEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def RemoveWhitelistEntry(self, UserOrUUID: str) -> Void:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/RemoveWhitelistEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RemoveWhitelistEntryAsync(self, UserOrUUID: str) -> Void:
        """
        Name Description Optional
        :param UserOrUUID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/RemoveWhitelistEntry", { 
            "UserOrUUID": UserOrUUID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def SmiteByID(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("MinecraftModule/SmiteByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SmiteByIDAsync(self, ID: str) -> Void:
        """
        Name Description Optional
        :param ID: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("MinecraftModule/SmiteByID", { 
            "ID": ID,
        })
        if response == None:
            response = {}
        return Void(**response)

