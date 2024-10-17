# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class LocalFileBackupPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the LocalFileBackupPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def DeleteFromS3(self, BackupId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("LocalFileBackupPlugin/DeleteFromS3", { 
            "BackupId": BackupId,
        })
        return ActionResult(**response)

    async def DeleteFromS3Async(self, BackupId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/DeleteFromS3", { 
            "BackupId": BackupId,
        })
        return ActionResult(**response)

    def DeleteLocalBackup(self, BackupId: UUID) -> Void:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: Void
        """
        response: dict = self.api_call("LocalFileBackupPlugin/DeleteLocalBackup", { 
            "BackupId": BackupId,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def DeleteLocalBackupAsync(self, BackupId: UUID) -> Void:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/DeleteLocalBackup", { 
            "BackupId": BackupId,
        })
        if response == None:
            response = {}
        return Void(**response)

    def DownloadFromS3(self, BackupId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("LocalFileBackupPlugin/DownloadFromS3", { 
            "BackupId": BackupId,
        })
        return RunningTask(**response)

    async def DownloadFromS3Async(self, BackupId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/DownloadFromS3", { 
            "BackupId": BackupId,
        })
        return RunningTask(**response)

    def GetBackups(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("LocalFileBackupPlugin/GetBackups", { 
        })
        return [Any(**x) for x in response]

    async def GetBackupsAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/GetBackups", { 
        })
        return [Any(**x) for x in response]

    def RestoreBackup(self, BackupId: UUID, DeleteExistingData: bool) -> ActionResult:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :param DeleteExistingData: {bool}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("LocalFileBackupPlugin/RestoreBackup", { 
            "BackupId": BackupId,
            "DeleteExistingData": DeleteExistingData,
        })
        return ActionResult(**response)

    async def RestoreBackupAsync(self, BackupId: UUID, DeleteExistingData: bool) -> ActionResult:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :param DeleteExistingData: {bool}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/RestoreBackup", { 
            "BackupId": BackupId,
            "DeleteExistingData": DeleteExistingData,
        })
        return ActionResult(**response)

    def SetBackupSticky(self, BackupId: UUID, Sticky: bool) -> Void:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :param Sticky: {bool}  False
        :returns: Void
        """
        response: dict = self.api_call("LocalFileBackupPlugin/SetBackupSticky", { 
            "BackupId": BackupId,
            "Sticky": Sticky,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SetBackupStickyAsync(self, BackupId: UUID, Sticky: bool) -> Void:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :param Sticky: {bool}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/SetBackupSticky", { 
            "BackupId": BackupId,
            "Sticky": Sticky,
        })
        if response == None:
            response = {}
        return Void(**response)

    def TakeBackup(self, Title: str, Description: str, Sticky: bool, WasCreatedAutomatically: bool) -> ActionResult:
        """
        Name Description Optional
        :param Title: {str}  False
        :param Description: {str}  False
        :param Sticky: {bool}  False
        :param WasCreatedAutomatically: {bool}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("LocalFileBackupPlugin/TakeBackup", { 
            "Title": Title,
            "Description": Description,
            "Sticky": Sticky,
            "WasCreatedAutomatically": WasCreatedAutomatically,
        })
        return ActionResult(**response)

    async def TakeBackupAsync(self, Title: str, Description: str, Sticky: bool, WasCreatedAutomatically: bool) -> ActionResult:
        """
        Name Description Optional
        :param Title: {str}  False
        :param Description: {str}  False
        :param Sticky: {bool}  False
        :param WasCreatedAutomatically: {bool}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/TakeBackup", { 
            "Title": Title,
            "Description": Description,
            "Sticky": Sticky,
            "WasCreatedAutomatically": WasCreatedAutomatically,
        })
        return ActionResult(**response)

    def UploadToS3(self, BackupId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("LocalFileBackupPlugin/UploadToS3", { 
            "BackupId": BackupId,
        })
        return RunningTask(**response)

    async def UploadToS3Async(self, BackupId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param BackupId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/UploadToS3", { 
            "BackupId": BackupId,
        })
        return RunningTask(**response)

    def RefreshBackupList(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("LocalFileBackupPlugin/RefreshBackupList", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RefreshBackupListAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("LocalFileBackupPlugin/RefreshBackupList", { 
        })
        if response == None:
            response = {}
        return Void(**response)

