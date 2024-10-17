# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class Core(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the Core class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AcknowledgeAMPUpdate(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/AcknowledgeAMPUpdate", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def AcknowledgeAMPUpdateAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/AcknowledgeAMPUpdate", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def ActivateAMPLicence(self, LicenceKey: str, QueryOnly: bool) -> ActionResult[LicenceInfo]:
        """
        Name Description Optional
        :param LicenceKey: {str}  False
        :param QueryOnly: {bool}  True
        :returns: ActionResult[LicenceInfo]
        """
        response: dict = self.api_call("Core/ActivateAMPLicence", { 
            "LicenceKey": LicenceKey,
            "QueryOnly": QueryOnly,
        })
        return ActionResult[LicenceInfo](**response)

    async def ActivateAMPLicenceAsync(self, LicenceKey: str, QueryOnly: bool) -> ActionResult[LicenceInfo]:
        """
        Name Description Optional
        :param LicenceKey: {str}  False
        :param QueryOnly: {bool}  True
        :returns: ActionResult[LicenceInfo]
        """
        response: dict = await self.api_call_async("Core/ActivateAMPLicence", { 
            "LicenceKey": LicenceKey,
            "QueryOnly": QueryOnly,
        })
        return ActionResult[LicenceInfo](**response)

    def AddEventTrigger(self, triggerId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param triggerId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/AddEventTrigger", { 
            "triggerId": triggerId,
        })
        return ActionResult(**response)

    async def AddEventTriggerAsync(self, triggerId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param triggerId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/AddEventTrigger", { 
            "triggerId": triggerId,
        })
        return ActionResult(**response)

    def AddIntervalTrigger(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> ActionResult:
        """
        Name Description Optional
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/AddIntervalTrigger", { 
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })
        return ActionResult(**response)

    async def AddIntervalTriggerAsync(self, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> ActionResult:
        """
        Name Description Optional
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/AddIntervalTrigger", { 
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })
        return ActionResult(**response)

    def AddTask(self, TriggerID: UUID, MethodID: str, ParameterMapping: dict[str, str]) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param MethodID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/AddTask", { 
            "TriggerID": TriggerID,
            "MethodID": MethodID,
            "ParameterMapping": ParameterMapping,
        })
        return ActionResult(**response)

    async def AddTaskAsync(self, TriggerID: UUID, MethodID: str, ParameterMapping: dict[str, str]) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param MethodID: {str}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/AddTask", { 
            "TriggerID": TriggerID,
            "MethodID": MethodID,
            "ParameterMapping": ParameterMapping,
        })
        return ActionResult(**response)

    def AsyncTest(self, ) -> str:
        """
     * DEV: Async test method
        Name Description Optional
        :returns: str
        """
        response: dict = self.api_call("Core/AsyncTest", { 
        })
        return str(**response)

    async def AsyncTestAsync(self, ) -> str:
        """
     * DEV: Async test method
        Name Description Optional
        :returns: str
        """
        response: dict = await self.api_call_async("Core/AsyncTest", { 
        })
        return str(**response)

    def CancelTask(self, TaskId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TaskId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/CancelTask", { 
            "TaskId": TaskId,
        })
        return ActionResult(**response)

    async def CancelTaskAsync(self, TaskId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TaskId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/CancelTask", { 
            "TaskId": TaskId,
        })
        return ActionResult(**response)

    def ChangeTaskOrder(self, TriggerID: UUID, TaskID: UUID, NewOrder: int) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :param NewOrder: {int}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/ChangeTaskOrder", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "NewOrder": NewOrder,
        })
        return ActionResult(**response)

    async def ChangeTaskOrderAsync(self, TriggerID: UUID, TaskID: UUID, NewOrder: int) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :param NewOrder: {int}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/ChangeTaskOrder", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "NewOrder": NewOrder,
        })
        return ActionResult(**response)

    def ChangeUserPassword(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param OldPassword: {str}  False
        :param NewPassword: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/ChangeUserPassword", { 
            "Username": Username,
            "OldPassword": OldPassword,
            "NewPassword": NewPassword,
            "TwoFactorPIN": TwoFactorPIN,
        })
        return ActionResult(**response)

    async def ChangeUserPasswordAsync(self, Username: str, OldPassword: str, NewPassword: str, TwoFactorPIN: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param OldPassword: {str}  False
        :param NewPassword: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/ChangeUserPassword", { 
            "Username": Username,
            "OldPassword": OldPassword,
            "NewPassword": NewPassword,
            "TwoFactorPIN": TwoFactorPIN,
        })
        return ActionResult(**response)

    def ConfirmTwoFactorSetup(self, Username: str, TwoFactorCode: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/ConfirmTwoFactorSetup", { 
            "Username": Username,
            "TwoFactorCode": TwoFactorCode,
        })
        return ActionResult(**response)

    async def ConfirmTwoFactorSetupAsync(self, Username: str, TwoFactorCode: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/ConfirmTwoFactorSetup", { 
            "Username": Username,
            "TwoFactorCode": TwoFactorCode,
        })
        return ActionResult(**response)

    def CreateRole(self, Name: str, AsCommonRole: bool) -> ActionResult[UUID]:
        """
        Name Description Optional
        :param Name: {str}  False
        :param AsCommonRole: {bool}  True
        :returns: ActionResult[UUID]
        """
        response: dict = self.api_call("Core/CreateRole", { 
            "Name": Name,
            "AsCommonRole": AsCommonRole,
        })
        return ActionResult[UUID](**response)

    async def CreateRoleAsync(self, Name: str, AsCommonRole: bool) -> ActionResult[UUID]:
        """
        Name Description Optional
        :param Name: {str}  False
        :param AsCommonRole: {bool}  True
        :returns: ActionResult[UUID]
        """
        response: dict = await self.api_call_async("Core/CreateRole", { 
            "Name": Name,
            "AsCommonRole": AsCommonRole,
        })
        return ActionResult[UUID](**response)

    def CreateTestTask(self, ) -> Void:
        """
     * DEV: Creates a non-ending task with 50% progress for testing purposes
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/CreateTestTask", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def CreateTestTaskAsync(self, ) -> Void:
        """
     * DEV: Creates a non-ending task with 50% progress for testing purposes
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/CreateTestTask", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def CreateUser(self, Username: str) -> ActionResult[UUID]:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: ActionResult[UUID]
        """
        response: dict = self.api_call("Core/CreateUser", { 
            "Username": Username,
        })
        return ActionResult[UUID](**response)

    async def CreateUserAsync(self, Username: str) -> ActionResult[UUID]:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: ActionResult[UUID]
        """
        response: dict = await self.api_call_async("Core/CreateUser", { 
            "Username": Username,
        })
        return ActionResult[UUID](**response)

    def CurrentSessionHasPermission(self, PermissionNode: str) -> bool:
        """
        Name Description Optional
        :param PermissionNode: {str}  False
        :returns: bool
        """
        response: dict = self.api_call("Core/CurrentSessionHasPermission", { 
            "PermissionNode": PermissionNode,
        })
        return bool(**response)

    async def CurrentSessionHasPermissionAsync(self, PermissionNode: str) -> bool:
        """
        Name Description Optional
        :param PermissionNode: {str}  False
        :returns: bool
        """
        response: dict = await self.api_call_async("Core/CurrentSessionHasPermission", { 
            "PermissionNode": PermissionNode,
        })
        return bool(**response)

    def DeleteInstanceUsers(self, InstanceId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })
        return ActionResult(**response)

    async def DeleteInstanceUsersAsync(self, InstanceId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })
        return ActionResult(**response)

    def DeleteRole(self, RoleId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DeleteRole", { 
            "RoleId": RoleId,
        })
        return ActionResult(**response)

    async def DeleteRoleAsync(self, RoleId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DeleteRole", { 
            "RoleId": RoleId,
        })
        return ActionResult(**response)

    def DeleteTask(self, TriggerID: UUID, TaskID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DeleteTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
        })
        return ActionResult(**response)

    async def DeleteTaskAsync(self, TriggerID: UUID, TaskID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DeleteTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
        })
        return ActionResult(**response)

    def DeleteTrigger(self, TriggerID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DeleteTrigger", { 
            "TriggerID": TriggerID,
        })
        return ActionResult(**response)

    async def DeleteTriggerAsync(self, TriggerID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DeleteTrigger", { 
            "TriggerID": TriggerID,
        })
        return ActionResult(**response)

    def DeleteUser(self, Username: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DeleteUser", { 
            "Username": Username,
        })
        return ActionResult(**response)

    async def DeleteUserAsync(self, Username: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DeleteUser", { 
            "Username": Username,
        })
        return ActionResult(**response)

    def DisableTwoFactor(self, Password: str, TwoFactorCode: str) -> ActionResult:
        """
        Name Description Optional
        :param Password: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DisableTwoFactor", { 
            "Password": Password,
            "TwoFactorCode": TwoFactorCode,
        })
        return ActionResult(**response)

    async def DisableTwoFactorAsync(self, Password: str, TwoFactorCode: str) -> ActionResult:
        """
        Name Description Optional
        :param Password: {str}  False
        :param TwoFactorCode: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DisableTwoFactor", { 
            "Password": Password,
            "TwoFactorCode": TwoFactorCode,
        })
        return ActionResult(**response)

    def DismissAllTasks(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DismissAllTasks", { 
        })
        return ActionResult(**response)

    async def DismissAllTasksAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DismissAllTasks", { 
        })
        return ActionResult(**response)

    def DismissTask(self, TaskId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TaskId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/DismissTask", { 
            "TaskId": TaskId,
        })
        return ActionResult(**response)

    async def DismissTaskAsync(self, TaskId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TaskId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/DismissTask", { 
            "TaskId": TaskId,
        })
        return ActionResult(**response)

    def EditIntervalTrigger(self, Id: UUID, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/EditIntervalTrigger", { 
            "Id": Id,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })
        return ActionResult(**response)

    async def EditIntervalTriggerAsync(self, Id: UUID, months: list[int], days: list[int], hours: list[int], minutes: list[int], daysOfMonth: list[int], description: str) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param months: {list[int]}  False
        :param days: {list[int]}  False
        :param hours: {list[int]}  False
        :param minutes: {list[int]}  False
        :param daysOfMonth: {list[int]}  False
        :param description: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/EditIntervalTrigger", { 
            "Id": Id,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "daysOfMonth": daysOfMonth,
            "description": description,
        })
        return ActionResult(**response)

    def EditTask(self, TriggerID: UUID, TaskID: UUID, ParameterMapping: dict[str, str]) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/EditTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "ParameterMapping": ParameterMapping,
        })
        return ActionResult(**response)

    async def EditTaskAsync(self, TriggerID: UUID, TaskID: UUID, ParameterMapping: dict[str, str]) -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: {UUID}  False
        :param TaskID: {UUID}  False
        :param ParameterMapping: {dict[str, str]}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/EditTask", { 
            "TriggerID": TriggerID,
            "TaskID": TaskID,
            "ParameterMapping": ParameterMapping,
        })
        return ActionResult(**response)

    def EnableTwoFactor(self, Username: str, Password: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Password: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = self.api_call("Core/EnableTwoFactor", { 
            "Username": Username,
            "Password": Password,
        })
        return ActionResult[Any](**response)

    async def EnableTwoFactorAsync(self, Username: str, Password: str) -> ActionResult[Any]:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Password: {str}  False
        :returns: ActionResult[Any]
        """
        response: dict = await self.api_call_async("Core/EnableTwoFactor", { 
            "Username": Username,
            "Password": Password,
        })
        return ActionResult[Any](**response)

    def EndUserSession(self, Id: UUID) -> Void:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: Void
        """
        response: dict = self.api_call("Core/EndUserSession", { 
            "Id": Id,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def EndUserSessionAsync(self, Id: UUID) -> Void:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/EndUserSession", { 
            "Id": Id,
        })
        if response == None:
            response = {}
        return Void(**response)

    def GetAMPRolePermissions(self, RoleId: UUID) -> list[str]:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: list[str]
        """
        response: dict = self.api_call("Core/GetAMPRolePermissions", { 
            "RoleId": RoleId,
        })
        return [str(**x) for x in response]

    async def GetAMPRolePermissionsAsync(self, RoleId: UUID) -> list[str]:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: list[str]
        """
        response: dict = await self.api_call_async("Core/GetAMPRolePermissions", { 
            "RoleId": RoleId,
        })
        return [str(**x) for x in response]

    def GetAMPUserInfo(self, Username: str) -> UserInfo:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: UserInfo
        """
        response: dict = self.api_call("Core/GetAMPUserInfo", { 
            "Username": Username,
        })
        return UserInfo(**response)

    async def GetAMPUserInfoAsync(self, Username: str) -> UserInfo:
        """
        Name Description Optional
        :param Username: {str}  False
        :returns: UserInfo
        """
        response: dict = await self.api_call_async("Core/GetAMPUserInfo", { 
            "Username": Username,
        })
        return UserInfo(**response)

    def GetAMPUsersSummary(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetAMPUsersSummary", { 
        })
        return [Any(**x) for x in response]

    async def GetAMPUsersSummaryAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetAMPUsersSummary", { 
        })
        return [Any(**x) for x in response]

    def GetAPISpec(self, ) -> dict[str, dict[str, Any]]:
        """
        Name Description Optional
        :returns: dict[str, dict[str, Any]]
        """
        response: dict = self.api_call("Core/GetAPISpec", { 
        })
        return response

    async def GetAPISpecAsync(self, ) -> dict[str, dict[str, Any]]:
        """
        Name Description Optional
        :returns: dict[str, dict[str, Any]]
        """
        response: dict = await self.api_call_async("Core/GetAPISpec", { 
        })
        return response

    def GetActiveAMPSessions(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetActiveAMPSessions", { 
        })
        return [Any(**x) for x in response]

    async def GetActiveAMPSessionsAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetActiveAMPSessions", { 
        })
        return [Any(**x) for x in response]

    def GetAllAMPUserInfo(self, ) -> list[UserInfo]:
        """
        Name Description Optional
        :returns: list[UserInfo]
        """
        response: dict = self.api_call("Core/GetAllAMPUserInfo", { 
        })
        return [UserInfo(**x) for x in response]

    async def GetAllAMPUserInfoAsync(self, ) -> list[UserInfo]:
        """
        Name Description Optional
        :returns: list[UserInfo]
        """
        response: dict = await self.api_call_async("Core/GetAllAMPUserInfo", { 
        })
        return [UserInfo(**x) for x in response]

    def GetAuditLogEntries(self, Before: Any, Count: int) -> list[Any]:
        """
        Name Description Optional
        :param Before: {Any}  False
        :param Count: {int}  False
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetAuditLogEntries", { 
            "Before": Before,
            "Count": Count,
        })
        return [Any(**x) for x in response]

    async def GetAuditLogEntriesAsync(self, Before: Any, Count: int) -> list[Any]:
        """
        Name Description Optional
        :param Before: {Any}  False
        :param Count: {int}  False
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetAuditLogEntries", { 
            "Before": Before,
            "Count": Count,
        })
        return [Any(**x) for x in response]

    def GetConfig(self, node: str) -> dict:
        """
        Name Description Optional
        :param node: {str}  False
        :returns: dict
        """
        response: dict = self.api_call("Core/GetConfig", { 
            "node": node,
        })
        return dict(**response)

    async def GetConfigAsync(self, node: str) -> dict:
        """
        Name Description Optional
        :param node: {str}  False
        :returns: dict
        """
        response: dict = await self.api_call_async("Core/GetConfig", { 
            "node": node,
        })
        return dict(**response)

    def GetConfigs(self, nodes: list[str]) -> list[dict]:
        """
        Name Description Optional
        :param nodes: {list[str]}  False
        :returns: list[dict]
        """
        response: dict = self.api_call("Core/GetConfigs", { 
            "nodes": nodes,
        })
        return [dict(**x) for x in response]

    async def GetConfigsAsync(self, nodes: list[str]) -> list[dict]:
        """
        Name Description Optional
        :param nodes: {list[str]}  False
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("Core/GetConfigs", { 
            "nodes": nodes,
        })
        return [dict(**x) for x in response]

    def GetDiagnosticsInfo(self, ) -> dict[str, str]:
        """
        Name Description Optional
        :returns: dict[str, str]
        """
        response: dict = self.api_call("Core/GetDiagnosticsInfo", { 
        })
        return response

    async def GetDiagnosticsInfoAsync(self, ) -> dict[str, str]:
        """
        Name Description Optional
        :returns: dict[str, str]
        """
        response: dict = await self.api_call_async("Core/GetDiagnosticsInfo", { 
        })
        return response

    def GetModuleInfo(self, ) -> ModuleInfo:
        """
        Name Description Optional
        :returns: ModuleInfo
        """
        response: dict = self.api_call("Core/GetModuleInfo", { 
        })
        return ModuleInfo(**response)

    async def GetModuleInfoAsync(self, ) -> ModuleInfo:
        """
        Name Description Optional
        :returns: ModuleInfo
        """
        response: dict = await self.api_call_async("Core/GetModuleInfo", { 
        })
        return ModuleInfo(**response)

    def GetNewGuid(self, ) -> UUID:
        """
        Name Description Optional
        :returns: UUID
        """
        response: dict = self.api_call("Core/GetNewGuid", { 
        })
        return UUID(**response)

    async def GetNewGuidAsync(self, ) -> UUID:
        """
        Name Description Optional
        :returns: UUID
        """
        response: dict = await self.api_call_async("Core/GetNewGuid", { 
        })
        return UUID(**response)

    def GetPermissionsSpec(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetPermissionsSpec", { 
        })
        return [Any(**x) for x in response]

    async def GetPermissionsSpecAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetPermissionsSpec", { 
        })
        return [Any(**x) for x in response]

    def GetPortSummaries(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetPortSummaries", { 
        })
        return [Any(**x) for x in response]

    async def GetPortSummariesAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetPortSummaries", { 
        })
        return [Any(**x) for x in response]

    def GetProvisionSpec(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("Core/GetProvisionSpec", { 
        })
        return [dict(**x) for x in response]

    async def GetProvisionSpecAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("Core/GetProvisionSpec", { 
        })
        return [dict(**x) for x in response]

    def GetRemoteLoginToken(self, Description: str, IsTemporary: bool) -> str:
        """
        Name Description Optional
        :param Description: {str}  True
        :param IsTemporary: {bool}  True
        :returns: str
        """
        response: dict = self.api_call("Core/GetRemoteLoginToken", { 
            "Description": Description,
            "IsTemporary": IsTemporary,
        })
        return str(**response)

    async def GetRemoteLoginTokenAsync(self, Description: str, IsTemporary: bool) -> str:
        """
        Name Description Optional
        :param Description: {str}  True
        :param IsTemporary: {bool}  True
        :returns: str
        """
        response: dict = await self.api_call_async("Core/GetRemoteLoginToken", { 
            "Description": Description,
            "IsTemporary": IsTemporary,
        })
        return str(**response)

    def GetRole(self, RoleId: UUID) -> Any:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: Any
        """
        response: dict = self.api_call("Core/GetRole", { 
            "RoleId": RoleId,
        })
        return Any(**response)

    async def GetRoleAsync(self, RoleId: UUID) -> Any:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetRole", { 
            "RoleId": RoleId,
        })
        return Any(**response)

    def GetRoleData(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetRoleData", { 
        })
        return [Any(**x) for x in response]

    async def GetRoleDataAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetRoleData", { 
        })
        return [Any(**x) for x in response]

    def GetRoleIds(self, ) -> dict[UUID, str]:
        """
        Name Description Optional
        :returns: dict[UUID, str]
        """
        response: dict = self.api_call("Core/GetRoleIds", { 
        })
        return response

    async def GetRoleIdsAsync(self, ) -> dict[UUID, str]:
        """
        Name Description Optional
        :returns: dict[UUID, str]
        """
        response: dict = await self.api_call_async("Core/GetRoleIds", { 
        })
        return response

    def GetScheduleData(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = self.api_call("Core/GetScheduleData", { 
        })
        return Any(**response)

    async def GetScheduleDataAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetScheduleData", { 
        })
        return Any(**response)

    def GetSettingValues(self, SettingNode: str, WithRefresh: bool) -> dict[str, str]:
        """
        Name Description Optional
        :param SettingNode: {str}  False
        :param WithRefresh: {bool}  True
        :returns: dict[str, str]
        """
        response: dict = self.api_call("Core/GetSettingValues", { 
            "SettingNode": SettingNode,
            "WithRefresh": WithRefresh,
        })
        return response

    async def GetSettingValuesAsync(self, SettingNode: str, WithRefresh: bool) -> dict[str, str]:
        """
        Name Description Optional
        :param SettingNode: {str}  False
        :param WithRefresh: {bool}  True
        :returns: dict[str, str]
        """
        response: dict = await self.api_call_async("Core/GetSettingValues", { 
            "SettingNode": SettingNode,
            "WithRefresh": WithRefresh,
        })
        return response

    def GetSettingsSpec(self, ) -> dict[str, SettingSpec]:
        """
        Name Description Optional
        :returns: dict[str, SettingSpec]
        """
        response: dict = self.api_call("Core/GetSettingsSpec", { 
        })
        return response

    async def GetSettingsSpecAsync(self, ) -> dict[str, SettingSpec]:
        """
        Name Description Optional
        :returns: dict[str, SettingSpec]
        """
        response: dict = await self.api_call_async("Core/GetSettingsSpec", { 
        })
        return response

    def GetStatus(self, ) -> Status:
        """
        Name Description Optional
        :returns: Status
        """
        response: dict = self.api_call("Core/GetStatus", { 
        })
        return Status(**response)

    async def GetStatusAsync(self, ) -> Status:
        """
        Name Description Optional
        :returns: Status
        """
        response: dict = await self.api_call_async("Core/GetStatus", { 
        })
        return Status(**response)

    def GetTasks(self, ) -> list[RunningTask]:
        """
        Name Description Optional
        :returns: list[RunningTask]
        """
        response: dict = self.api_call("Core/GetTasks", { 
        })
        return [RunningTask(**x) for x in response]

    async def GetTasksAsync(self, ) -> list[RunningTask]:
        """
        Name Description Optional
        :returns: list[RunningTask]
        """
        response: dict = await self.api_call_async("Core/GetTasks", { 
        })
        return [RunningTask(**x) for x in response]

    def GetTimeIntervalTrigger(self, Id: UUID) -> Any:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: Any
        """
        response: dict = self.api_call("Core/GetTimeIntervalTrigger", { 
            "Id": Id,
        })
        return Any(**response)

    async def GetTimeIntervalTriggerAsync(self, Id: UUID) -> Any:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetTimeIntervalTrigger", { 
            "Id": Id,
        })
        return Any(**response)

    def GetUpdateInfo(self, ) -> UpdateInfo:
        """
        Name Description Optional
        :returns: UpdateInfo
        """
        response: dict = self.api_call("Core/GetUpdateInfo", { 
        })
        return UpdateInfo(**response)

    async def GetUpdateInfoAsync(self, ) -> UpdateInfo:
        """
        Name Description Optional
        :returns: UpdateInfo
        """
        response: dict = await self.api_call_async("Core/GetUpdateInfo", { 
        })
        return UpdateInfo(**response)

    def GetUpdates(self, ) -> Updates:
        """
     * Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
        Name Description Optional
        :returns: Updates
        """
        response: dict = self.api_call("Core/GetUpdates", { 
        })
        return Updates(**response)

    async def GetUpdatesAsync(self, ) -> Updates:
        """
     * Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
        Name Description Optional
        :returns: Updates
        """
        response: dict = await self.api_call_async("Core/GetUpdates", { 
        })
        return Updates(**response)

    def GetUserActionsSpec(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = self.api_call("Core/GetUserActionsSpec", { 
        })
        return Any(**response)

    async def GetUserActionsSpecAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetUserActionsSpec", { 
        })
        return Any(**response)

    def GetUserInfo(self, UID: str) -> Any:
        """
        Name Description Optional
        :param UID: {str}  False
        :returns: Any
        """
        response: dict = self.api_call("Core/GetUserInfo", { 
            "UID": UID,
        })
        return Any(**response)

    async def GetUserInfoAsync(self, UID: str) -> Any:
        """
        Name Description Optional
        :param UID: {str}  False
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetUserInfo", { 
            "UID": UID,
        })
        return Any(**response)

    def GetUserList(self, ) -> dict[str, str]:
        """
     * Returns a list of in-application users
        Name Description Optional
        :returns: dict[str, str]
        """
        response: dict = self.api_call("Core/GetUserList", { 
        })
        return response

    async def GetUserListAsync(self, ) -> dict[str, str]:
        """
     * Returns a list of in-application users
        Name Description Optional
        :returns: dict[str, str]
        """
        response: dict = await self.api_call_async("Core/GetUserList", { 
        })
        return response

    def GetWebauthnChallenge(self, ) -> ActionResult[str]:
        """
        Name Description Optional
        :returns: ActionResult[str]
        """
        response: dict = self.api_call("Core/GetWebauthnChallenge", { 
        })
        return ActionResult[str](**response)

    async def GetWebauthnChallengeAsync(self, ) -> ActionResult[str]:
        """
        Name Description Optional
        :returns: ActionResult[str]
        """
        response: dict = await self.api_call_async("Core/GetWebauthnChallenge", { 
        })
        return ActionResult[str](**response)

    def GetWebauthnCredentialIDs(self, username: str) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: Any
        """
        response: dict = self.api_call("Core/GetWebauthnCredentialIDs", { 
            "username": username,
        })
        return Any(**response)

    async def GetWebauthnCredentialIDsAsync(self, username: str) -> Any:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetWebauthnCredentialIDs", { 
            "username": username,
        })
        return Any(**response)

    def GetWebauthnCredentialSummaries(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetWebauthnCredentialSummaries", { 
        })
        return [Any(**x) for x in response]

    async def GetWebauthnCredentialSummariesAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetWebauthnCredentialSummaries", { 
        })
        return [Any(**x) for x in response]

    def GetWebserverMetrics(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = self.api_call("Core/GetWebserverMetrics", { 
        })
        return Any(**response)

    async def GetWebserverMetricsAsync(self, ) -> Any:
        """
        Name Description Optional
        :returns: Any
        """
        response: dict = await self.api_call_async("Core/GetWebserverMetrics", { 
        })
        return Any(**response)

    def Kill(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/Kill", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def KillAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/Kill", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def Login(self, username: str, password: str, token: str, rememberMe: bool) -> LoginResult:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :param token: {str}  False
        :param rememberMe: {bool}  False
        :returns: LoginResult
        """
        response: dict = self.api_call("Core/Login", { 
            "username": username,
            "password": password,
            "token": token,
            "rememberMe": rememberMe,
        })
        return LoginResult(**response)

    async def LoginAsync(self, username: str, password: str, token: str, rememberMe: bool) -> LoginResult:
        """
        Name Description Optional
        :param username: {str}  False
        :param password: {str}  False
        :param token: {str}  False
        :param rememberMe: {bool}  False
        :returns: LoginResult
        """
        response: dict = await self.api_call_async("Core/Login", { 
            "username": username,
            "password": password,
            "token": token,
            "rememberMe": rememberMe,
        })
        return LoginResult(**response)

    def Logout(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/Logout", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def LogoutAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/Logout", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def RefreshSettingValueList(self, Node: str) -> ActionResult:
        """
        Name Description Optional
        :param Node: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/RefreshSettingValueList", { 
            "Node": Node,
        })
        return ActionResult(**response)

    async def RefreshSettingValueListAsync(self, Node: str) -> ActionResult:
        """
        Name Description Optional
        :param Node: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/RefreshSettingValueList", { 
            "Node": Node,
        })
        return ActionResult(**response)

    def RefreshSettingsSourceCache(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/RefreshSettingsSourceCache", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RefreshSettingsSourceCacheAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/RefreshSettingsSourceCache", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def RenameRole(self, RoleId: UUID, NewName: str) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :param NewName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/RenameRole", { 
            "RoleId": RoleId,
            "NewName": NewName,
        })
        return ActionResult(**response)

    async def RenameRoleAsync(self, RoleId: UUID, NewName: str) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :param NewName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/RenameRole", { 
            "RoleId": RoleId,
            "NewName": NewName,
        })
        return ActionResult(**response)

    def ResetUserPassword(self, Username: str, NewPassword: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param NewPassword: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/ResetUserPassword", { 
            "Username": Username,
            "NewPassword": NewPassword,
        })
        return ActionResult(**response)

    async def ResetUserPasswordAsync(self, Username: str, NewPassword: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param NewPassword: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/ResetUserPassword", { 
            "Username": Username,
            "NewPassword": NewPassword,
        })
        return ActionResult(**response)

    def Restart(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/Restart", { 
        })
        return ActionResult(**response)

    async def RestartAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/Restart", { 
        })
        return ActionResult(**response)

    def RestartAMP(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/RestartAMP", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RestartAMPAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/RestartAMP", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def Resume(self, ) -> Void:
        """
     * Allows the service to be re-started after previously being suspended.
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/Resume", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def ResumeAsync(self, ) -> Void:
        """
     * Allows the service to be re-started after previously being suspended.
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/Resume", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def RevokeWebauthnCredential(self, ID: int) -> ActionResult:
        """
        Name Description Optional
        :param ID: {int}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/RevokeWebauthnCredential", { 
            "ID": ID,
        })
        return ActionResult(**response)

    async def RevokeWebauthnCredentialAsync(self, ID: int) -> ActionResult:
        """
        Name Description Optional
        :param ID: {int}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/RevokeWebauthnCredential", { 
            "ID": ID,
        })
        return ActionResult(**response)

    def RunEventTriggerImmediately(self, triggerId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param triggerId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/RunEventTriggerImmediately", { 
            "triggerId": triggerId,
        })
        return ActionResult(**response)

    async def RunEventTriggerImmediatelyAsync(self, triggerId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param triggerId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/RunEventTriggerImmediately", { 
            "triggerId": triggerId,
        })
        return ActionResult(**response)

    def SendConsoleMessage(self, message: str) -> Void:
        """
        Name Description Optional
        :param message: {str}  False
        :returns: Void
        """
        response: dict = self.api_call("Core/SendConsoleMessage", { 
            "message": message,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SendConsoleMessageAsync(self, message: str) -> Void:
        """
        Name Description Optional
        :param message: {str}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/SendConsoleMessage", { 
            "message": message,
        })
        if response == None:
            response = {}
        return Void(**response)

    def SetAMPRolePermission(self, RoleId: UUID, PermissionNode: str, Enabled: bool) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :param PermissionNode: {str}  False
        :param Enabled: {bool}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/SetAMPRolePermission", { 
            "RoleId": RoleId,
            "PermissionNode": PermissionNode,
            "Enabled": Enabled,
        })
        return ActionResult(**response)

    async def SetAMPRolePermissionAsync(self, RoleId: UUID, PermissionNode: str, Enabled: bool) -> ActionResult:
        """
        Name Description Optional
        :param RoleId: {UUID}  False
        :param PermissionNode: {str}  False
        :param Enabled: {bool}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/SetAMPRolePermission", { 
            "RoleId": RoleId,
            "PermissionNode": PermissionNode,
            "Enabled": Enabled,
        })
        return ActionResult(**response)

    def SetAMPUserRoleMembership(self, UserId: UUID, RoleId: UUID, IsMember: bool) -> ActionResult:
        """
        Name Description Optional
        :param UserId: {UUID}  False
        :param RoleId: {UUID}  False
        :param IsMember: {bool}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/SetAMPUserRoleMembership", { 
            "UserId": UserId,
            "RoleId": RoleId,
            "IsMember": IsMember,
        })
        return ActionResult(**response)

    async def SetAMPUserRoleMembershipAsync(self, UserId: UUID, RoleId: UUID, IsMember: bool) -> ActionResult:
        """
        Name Description Optional
        :param UserId: {UUID}  False
        :param RoleId: {UUID}  False
        :param IsMember: {bool}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/SetAMPUserRoleMembership", { 
            "UserId": UserId,
            "RoleId": RoleId,
            "IsMember": IsMember,
        })
        return ActionResult(**response)

    def SetConfig(self, node: str, value: str) -> ActionResult:
        """
        Name Description Optional
        :param node: {str}  False
        :param value: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/SetConfig", { 
            "node": node,
            "value": value,
        })
        return ActionResult(**response)

    async def SetConfigAsync(self, node: str, value: str) -> ActionResult:
        """
        Name Description Optional
        :param node: {str}  False
        :param value: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/SetConfig", { 
            "node": node,
            "value": value,
        })
        return ActionResult(**response)

    def SetConfigs(self, data: dict[str, str]) -> bool:
        """
        Name Description Optional
        :param data: {dict[str, str]}  False
        :returns: bool
        """
        response: dict = self.api_call("Core/SetConfigs", { 
            "data": data,
        })
        return bool(**response)

    async def SetConfigsAsync(self, data: dict[str, str]) -> bool:
        """
        Name Description Optional
        :param data: {dict[str, str]}  False
        :returns: bool
        """
        response: dict = await self.api_call_async("Core/SetConfigs", { 
            "data": data,
        })
        return bool(**response)

    def SetTriggerEnabled(self, Id: UUID, Enabled: bool) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param Enabled: {bool}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/SetTriggerEnabled", { 
            "Id": Id,
            "Enabled": Enabled,
        })
        return ActionResult(**response)

    async def SetTriggerEnabledAsync(self, Id: UUID, Enabled: bool) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param Enabled: {bool}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/SetTriggerEnabled", { 
            "Id": Id,
            "Enabled": Enabled,
        })
        return ActionResult(**response)

    def Sleep(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/Sleep", { 
        })
        return ActionResult(**response)

    async def SleepAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/Sleep", { 
        })
        return ActionResult(**response)

    def Start(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/Start", { 
        })
        return ActionResult(**response)

    async def StartAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/Start", { 
        })
        return ActionResult(**response)

    def Stop(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/Stop", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def StopAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/Stop", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def Suspend(self, ) -> Void:
        """
     * Prevents the current instance from being started, and stops it if it's currently running.
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/Suspend", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def SuspendAsync(self, ) -> Void:
        """
     * Prevents the current instance from being started, and stops it if it's currently running.
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/Suspend", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def UpdateAMPInstance(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/UpdateAMPInstance", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def UpdateAMPInstanceAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/UpdateAMPInstance", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def UpdateAccountInfo(self, EmailAddress: str, TwoFactorPIN: str) -> ActionResult:
        """
        Name Description Optional
        :param EmailAddress: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/UpdateAccountInfo", { 
            "EmailAddress": EmailAddress,
            "TwoFactorPIN": TwoFactorPIN,
        })
        return ActionResult(**response)

    async def UpdateAccountInfoAsync(self, EmailAddress: str, TwoFactorPIN: str) -> ActionResult:
        """
        Name Description Optional
        :param EmailAddress: {str}  False
        :param TwoFactorPIN: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/UpdateAccountInfo", { 
            "EmailAddress": EmailAddress,
            "TwoFactorPIN": TwoFactorPIN,
        })
        return ActionResult(**response)

    def UpdateApplication(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/UpdateApplication", { 
        })
        return ActionResult(**response)

    async def UpdateApplicationAsync(self, ) -> ActionResult:
        """
        Name Description Optional
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/UpdateApplication", { 
        })
        return ActionResult(**response)

    def UpdateUserInfo(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Disabled: {bool}  False
        :param PasswordExpires: {bool}  False
        :param CannotChangePassword: {bool}  False
        :param MustChangePassword: {bool}  False
        :param EmailAddress: {str}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/UpdateUserInfo", { 
            "Username": Username,
            "Disabled": Disabled,
            "PasswordExpires": PasswordExpires,
            "CannotChangePassword": CannotChangePassword,
            "MustChangePassword": MustChangePassword,
            "EmailAddress": EmailAddress,
        })
        return ActionResult(**response)

    async def UpdateUserInfoAsync(self, Username: str, Disabled: bool, PasswordExpires: bool, CannotChangePassword: bool, MustChangePassword: bool, EmailAddress: str) -> ActionResult:
        """
        Name Description Optional
        :param Username: {str}  False
        :param Disabled: {bool}  False
        :param PasswordExpires: {bool}  False
        :param CannotChangePassword: {bool}  False
        :param MustChangePassword: {bool}  False
        :param EmailAddress: {str}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/UpdateUserInfo", { 
            "Username": Username,
            "Disabled": Disabled,
            "PasswordExpires": PasswordExpires,
            "CannotChangePassword": CannotChangePassword,
            "MustChangePassword": MustChangePassword,
            "EmailAddress": EmailAddress,
        })
        return ActionResult(**response)

    def UpgradeAMP(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("Core/UpgradeAMP", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def UpgradeAMPAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("Core/UpgradeAMP", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def WebauthnRegister(self, attestationObject: str, clientDataJSON: str, description: str) -> ActionResult:
        """
        Name Description Optional
        :param attestationObject: {str}  False
        :param clientDataJSON: {str}  False
        :param description: {str}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("Core/WebauthnRegister", { 
            "attestationObject": attestationObject,
            "clientDataJSON": clientDataJSON,
            "description": description,
        })
        return ActionResult(**response)

    async def WebauthnRegisterAsync(self, attestationObject: str, clientDataJSON: str, description: str) -> ActionResult:
        """
        Name Description Optional
        :param attestationObject: {str}  False
        :param clientDataJSON: {str}  False
        :param description: {str}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("Core/WebauthnRegister", { 
            "attestationObject": attestationObject,
            "clientDataJSON": clientDataJSON,
            "description": description,
        })
        return ActionResult(**response)

    def GetAuthenticationRequirements(self, username: str) -> list[Any]:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: list[Any]
        """
        response: dict = self.api_call("Core/GetAuthenticationRequirements", { 
            "username": username,
        })
        return [Any(**x) for x in response]

    async def GetAuthenticationRequirementsAsync(self, username: str) -> list[Any]:
        """
        Name Description Optional
        :param username: {str}  False
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("Core/GetAuthenticationRequirements", { 
            "username": username,
        })
        return [Any(**x) for x in response]

    def RunSecurityCheck(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("Core/RunSecurityCheck", { 
        })
        return [dict(**x) for x in response]

    async def RunSecurityCheckAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("Core/RunSecurityCheck", { 
        })
        return [dict(**x) for x in response]

