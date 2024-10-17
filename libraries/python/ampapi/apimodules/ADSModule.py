# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class ADSModule(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the ADSModule class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def AddDatastore(self, newDatastore: InstanceDatastore) -> ActionResult:
        """
        Name Description Optional
        :param newDatastore: {InstanceDatastore}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/AddDatastore", { 
            "newDatastore": newDatastore,
        })
        return ActionResult(**response)

    async def AddDatastoreAsync(self, newDatastore: InstanceDatastore) -> ActionResult:
        """
        Name Description Optional
        :param newDatastore: {InstanceDatastore}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/AddDatastore", { 
            "newDatastore": newDatastore,
        })
        return ActionResult(**response)

    def ApplyInstanceConfiguration(self, InstanceID: UUID, Args: dict[str, str], RebuildConfiguration: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceID: {UUID}  False
        :param Args: {dict[str, str]}  False
        :param RebuildConfiguration: {bool}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/ApplyInstanceConfiguration", { 
            "InstanceID": InstanceID,
            "Args": Args,
            "RebuildConfiguration": RebuildConfiguration,
        })
        return ActionResult(**response)

    async def ApplyInstanceConfigurationAsync(self, InstanceID: UUID, Args: dict[str, str], RebuildConfiguration: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceID: {UUID}  False
        :param Args: {dict[str, str]}  False
        :param RebuildConfiguration: {bool}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/ApplyInstanceConfiguration", { 
            "InstanceID": InstanceID,
            "Args": Args,
            "RebuildConfiguration": RebuildConfiguration,
        })
        return ActionResult(**response)

    def ApplyTemplate(self, InstanceID: UUID, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceID: {UUID}  False
        :param TemplateID: {int}  False
        :param NewFriendlyName: {str}  True
        :param Secret: {str}  True
        :param RestartIfPreviouslyRunning: {bool}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/ApplyTemplate", { 
            "InstanceID": InstanceID,
            "TemplateID": TemplateID,
            "NewFriendlyName": NewFriendlyName,
            "Secret": Secret,
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning,
        })
        return ActionResult(**response)

    async def ApplyTemplateAsync(self, InstanceID: UUID, TemplateID: int, NewFriendlyName: str, Secret: str, RestartIfPreviouslyRunning: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceID: {UUID}  False
        :param TemplateID: {int}  False
        :param NewFriendlyName: {str}  True
        :param Secret: {str}  True
        :param RestartIfPreviouslyRunning: {bool}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/ApplyTemplate", { 
            "InstanceID": InstanceID,
            "TemplateID": TemplateID,
            "NewFriendlyName": NewFriendlyName,
            "Secret": Secret,
            "RestartIfPreviouslyRunning": RestartIfPreviouslyRunning,
        })
        return ActionResult(**response)

    def AttachADS(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Friendly: {str}  False
        :param IsHTTPS: {bool}  False
        :param Host: {str}  False
        :param Port: {int}  False
        :param InstanceID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/AttachADS", { 
            "Friendly": Friendly,
            "IsHTTPS": IsHTTPS,
            "Host": Host,
            "Port": Port,
            "InstanceID": InstanceID,
        })
        return ActionResult(**response)

    async def AttachADSAsync(self, Friendly: str, IsHTTPS: bool, Host: str, Port: int, InstanceID: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Friendly: {str}  False
        :param IsHTTPS: {bool}  False
        :param Host: {str}  False
        :param Port: {int}  False
        :param InstanceID: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/AttachADS", { 
            "Friendly": Friendly,
            "IsHTTPS": IsHTTPS,
            "Host": Host,
            "Port": Port,
            "InstanceID": InstanceID,
        })
        return ActionResult(**response)

    def CloneTemplate(self, Id: int, NewName: str) -> ActionResult:
        """
        Name Description Optional
        :param Id: {int}  False
        :param NewName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/CloneTemplate", { 
            "Id": Id,
            "NewName": NewName,
        })
        return ActionResult(**response)

    async def CloneTemplateAsync(self, Id: int, NewName: str) -> ActionResult:
        """
        Name Description Optional
        :param Id: {int}  False
        :param NewName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/CloneTemplate", { 
            "Id": Id,
            "NewName": NewName,
        })
        return ActionResult(**response)

    def ConvertToManaged(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/ConvertToManaged", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    async def ConvertToManagedAsync(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/ConvertToManaged", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    def CreateDeploymentTemplate(self, Name: str) -> ActionResult:
        """
        Name Description Optional
        :param Name: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/CreateDeploymentTemplate", { 
            "Name": Name,
        })
        return ActionResult(**response)

    async def CreateDeploymentTemplateAsync(self, Name: str) -> ActionResult:
        """
        Name Description Optional
        :param Name: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/CreateDeploymentTemplate", { 
            "Name": Name,
        })
        return ActionResult(**response)

    def CreateInstance(self, TargetADSInstance: UUID, NewInstanceId: UUID, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int, PostCreate: Any) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :param NewInstanceId: {UUID}  False
        :param Module: {str}  False
        :param InstanceName: {str}  False
        :param FriendlyName: {str}  False
        :param IPBinding: {str}  False
        :param PortNumber: {int}  False
        :param AdminUsername: {str}  False
        :param AdminPassword: {str}  False
        :param ProvisionSettings: {dict[str, str]}  False
        :param AutoConfigure: {bool} When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values. True
        :param StartOnBoot: {bool}  True
        :param DisplayImageSource: {str}  True
        :param TargetDatastore: {int}  True
        :param PostCreate: {Any}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/CreateInstance", { 
            "TargetADSInstance": TargetADSInstance,
            "NewInstanceId": NewInstanceId,
            "Module": Module,
            "InstanceName": InstanceName,
            "FriendlyName": FriendlyName,
            "IPBinding": IPBinding,
            "PortNumber": PortNumber,
            "AdminUsername": AdminUsername,
            "AdminPassword": AdminPassword,
            "ProvisionSettings": ProvisionSettings,
            "AutoConfigure": AutoConfigure,
            "StartOnBoot": StartOnBoot,
            "DisplayImageSource": DisplayImageSource,
            "TargetDatastore": TargetDatastore,
            "PostCreate": PostCreate,
        })
        return ActionResult(**response)

    async def CreateInstanceAsync(self, TargetADSInstance: UUID, NewInstanceId: UUID, Module: str, InstanceName: str, FriendlyName: str, IPBinding: str, PortNumber: int, AdminUsername: str, AdminPassword: str, ProvisionSettings: dict[str, str], AutoConfigure: bool, StartOnBoot: bool, DisplayImageSource: str, TargetDatastore: int, PostCreate: Any) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :param NewInstanceId: {UUID}  False
        :param Module: {str}  False
        :param InstanceName: {str}  False
        :param FriendlyName: {str}  False
        :param IPBinding: {str}  False
        :param PortNumber: {int}  False
        :param AdminUsername: {str}  False
        :param AdminPassword: {str}  False
        :param ProvisionSettings: {dict[str, str]}  False
        :param AutoConfigure: {bool} When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values. True
        :param StartOnBoot: {bool}  True
        :param DisplayImageSource: {str}  True
        :param TargetDatastore: {int}  True
        :param PostCreate: {Any}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/CreateInstance", { 
            "TargetADSInstance": TargetADSInstance,
            "NewInstanceId": NewInstanceId,
            "Module": Module,
            "InstanceName": InstanceName,
            "FriendlyName": FriendlyName,
            "IPBinding": IPBinding,
            "PortNumber": PortNumber,
            "AdminUsername": AdminUsername,
            "AdminPassword": AdminPassword,
            "ProvisionSettings": ProvisionSettings,
            "AutoConfigure": AutoConfigure,
            "StartOnBoot": StartOnBoot,
            "DisplayImageSource": DisplayImageSource,
            "TargetDatastore": TargetDatastore,
            "PostCreate": PostCreate,
        })
        return ActionResult(**response)

    def CreateLocalInstance(self, Instance: Any, PostCreate: Any) -> ActionResult:
        """
        Name Description Optional
        :param Instance: {Any}  False
        :param PostCreate: {Any}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/CreateLocalInstance", { 
            "Instance": Instance,
            "PostCreate": PostCreate,
        })
        return ActionResult(**response)

    async def CreateLocalInstanceAsync(self, Instance: Any, PostCreate: Any) -> ActionResult:
        """
        Name Description Optional
        :param Instance: {Any}  False
        :param PostCreate: {Any}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/CreateLocalInstance", { 
            "Instance": Instance,
            "PostCreate": PostCreate,
        })
        return ActionResult(**response)

    def DeleteDatastore(self, id: int) -> ActionResult:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/DeleteDatastore", { 
            "id": id,
        })
        return ActionResult(**response)

    async def DeleteDatastoreAsync(self, id: int) -> ActionResult:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/DeleteDatastore", { 
            "id": id,
        })
        return ActionResult(**response)

    def DeleteDeploymentTemplate(self, Id: int) -> ActionResult:
        """
        Name Description Optional
        :param Id: {int}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/DeleteDeploymentTemplate", { 
            "Id": Id,
        })
        return ActionResult(**response)

    async def DeleteDeploymentTemplateAsync(self, Id: int) -> ActionResult:
        """
        Name Description Optional
        :param Id: {int}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/DeleteDeploymentTemplate", { 
            "Id": Id,
        })
        return ActionResult(**response)

    def DeleteInstance(self, InstanceName: str) -> RunningTask:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/DeleteInstance", { 
            "InstanceName": InstanceName,
        })
        return RunningTask(**response)

    async def DeleteInstanceAsync(self, InstanceName: str) -> RunningTask:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/DeleteInstance", { 
            "InstanceName": InstanceName,
        })
        return RunningTask(**response)

    def DeleteInstanceUsers(self, InstanceId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })
        return ActionResult(**response)

    async def DeleteInstanceUsersAsync(self, InstanceId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/DeleteInstanceUsers", { 
            "InstanceId": InstanceId,
        })
        return ActionResult(**response)

    def DeployTemplate(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, ExtraProvisionSettings: dict[str, str], PostCreate: Any) -> RunningTask:
        """0: Do Nothing, 1: Update Once, 2: Update Always, 3: Update and Start Once, 4: Update and Start Always, 5. Start Always
        Name Description Optional
        :param TemplateID: {int} The ID of the template to be deployed, as per the Template Management UI in AMP itself. False
        :param NewUsername: {str} If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user. True
        :param NewPassword: {str} If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user. True
        :param NewEmail: {str} If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user. True
        :param RequiredTags: {list[str]} If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings. True
        :param Tag: {str} Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique. True
        :param FriendlyName: {str} A friendly name for this instance. If left blank, AMP will generate one for you. True
        :param Secret: {str} Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request. True
        :param ExtraProvisionSettings: {dict[str, str]} A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself. True
        :param PostCreate: {Any} 0: Do Nothing, 1: Update Once, 2: Update Always, 3: Update and Start Once, 4: Update and Start Always, 5. Start Always True
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/DeployTemplate", { 
            "TemplateID": TemplateID,
            "NewUsername": NewUsername,
            "NewPassword": NewPassword,
            "NewEmail": NewEmail,
            "RequiredTags": RequiredTags,
            "Tag": Tag,
            "FriendlyName": FriendlyName,
            "Secret": Secret,
            "ExtraProvisionSettings": ExtraProvisionSettings,
            "PostCreate": PostCreate,
        })
        return RunningTask(**response)

    async def DeployTemplateAsync(self, TemplateID: int, NewUsername: str, NewPassword: str, NewEmail: str, RequiredTags: list[str], Tag: str, FriendlyName: str, Secret: str, ExtraProvisionSettings: dict[str, str], PostCreate: Any) -> RunningTask:
        """0: Do Nothing, 1: Update Once, 2: Update Always, 3: Update and Start Once, 4: Update and Start Always, 5. Start Always
        Name Description Optional
        :param TemplateID: {int} The ID of the template to be deployed, as per the Template Management UI in AMP itself. False
        :param NewUsername: {str} If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user. True
        :param NewPassword: {str} If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user. True
        :param NewEmail: {str} If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user. True
        :param RequiredTags: {list[str]} If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings. True
        :param Tag: {str} Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique. True
        :param FriendlyName: {str} A friendly name for this instance. If left blank, AMP will generate one for you. True
        :param Secret: {str} Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request. True
        :param ExtraProvisionSettings: {dict[str, str]} A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself. True
        :param PostCreate: {Any} 0: Do Nothing, 1: Update Once, 2: Update Always, 3: Update and Start Once, 4: Update and Start Always, 5. Start Always True
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/DeployTemplate", { 
            "TemplateID": TemplateID,
            "NewUsername": NewUsername,
            "NewPassword": NewPassword,
            "NewEmail": NewEmail,
            "RequiredTags": RequiredTags,
            "Tag": Tag,
            "FriendlyName": FriendlyName,
            "Secret": Secret,
            "ExtraProvisionSettings": ExtraProvisionSettings,
            "PostCreate": PostCreate,
        })
        return RunningTask(**response)

    def DetatchTarget(self, Id: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/DetatchTarget", { 
            "Id": Id,
        })
        return ActionResult(**response)

    async def DetatchTargetAsync(self, Id: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/DetatchTarget", { 
            "Id": Id,
        })
        return ActionResult(**response)

    def ExtractEverywhere(self, SourceArchive: str) -> ActionResult:
        """
        Name Description Optional
        :param SourceArchive: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/ExtractEverywhere", { 
            "SourceArchive": SourceArchive,
        })
        return ActionResult(**response)

    async def ExtractEverywhereAsync(self, SourceArchive: str) -> ActionResult:
        """
        Name Description Optional
        :param SourceArchive: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/ExtractEverywhere", { 
            "SourceArchive": SourceArchive,
        })
        return ActionResult(**response)

    def GetApplicationEndpoints(self, instanceId: UUID) -> list[EndpointInfo]:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :returns: list[EndpointInfo]
        """
        response: dict = self.api_call("ADSModule/GetApplicationEndpoints", { 
            "instanceId": instanceId,
        })
        return [EndpointInfo(**x) for x in response]

    async def GetApplicationEndpointsAsync(self, instanceId: UUID) -> list[EndpointInfo]:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :returns: list[EndpointInfo]
        """
        response: dict = await self.api_call_async("ADSModule/GetApplicationEndpoints", { 
            "instanceId": instanceId,
        })
        return [EndpointInfo(**x) for x in response]

    def GetDatastore(self, id: int) -> InstanceDatastore:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: InstanceDatastore
        """
        response: dict = self.api_call("ADSModule/GetDatastore", { 
            "id": id,
        })
        return InstanceDatastore(**response)

    async def GetDatastoreAsync(self, id: int) -> InstanceDatastore:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: InstanceDatastore
        """
        response: dict = await self.api_call_async("ADSModule/GetDatastore", { 
            "id": id,
        })
        return InstanceDatastore(**response)

    def GetDatastoreInstances(self, datastoreId: int) -> list[dict]:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: list[dict]
        """
        response: dict = self.api_call("ADSModule/GetDatastoreInstances", { 
            "datastoreId": datastoreId,
        })
        return [dict(**x) for x in response]

    async def GetDatastoreInstancesAsync(self, datastoreId: int) -> list[dict]:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("ADSModule/GetDatastoreInstances", { 
            "datastoreId": datastoreId,
        })
        return [dict(**x) for x in response]

    def GetDatastores(self, ) -> list[InstanceDatastore]:
        """
        Name Description Optional
        :returns: list[InstanceDatastore]
        """
        response: dict = self.api_call("ADSModule/GetDatastores", { 
        })
        return [InstanceDatastore(**x) for x in response]

    async def GetDatastoresAsync(self, ) -> list[InstanceDatastore]:
        """
        Name Description Optional
        :returns: list[InstanceDatastore]
        """
        response: dict = await self.api_call_async("ADSModule/GetDatastores", { 
        })
        return [InstanceDatastore(**x) for x in response]

    def GetDeploymentTemplates(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("ADSModule/GetDeploymentTemplates", { 
        })
        return [Any(**x) for x in response]

    async def GetDeploymentTemplatesAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("ADSModule/GetDeploymentTemplates", { 
        })
        return [Any(**x) for x in response]

    def GetGroup(self, GroupId: UUID) -> IADSInstance:
        """
        Name Description Optional
        :param GroupId: {UUID}  False
        :returns: IADSInstance
        """
        response: dict = self.api_call("ADSModule/GetGroup", { 
            "GroupId": GroupId,
        })
        return IADSInstance(**response)

    async def GetGroupAsync(self, GroupId: UUID) -> IADSInstance:
        """
        Name Description Optional
        :param GroupId: {UUID}  False
        :returns: IADSInstance
        """
        response: dict = await self.api_call_async("ADSModule/GetGroup", { 
            "GroupId": GroupId,
        })
        return IADSInstance(**response)

    def GetInstance(self, InstanceId: UUID) -> Instance:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: Instance
        """
        response: dict = self.api_call("ADSModule/GetInstance", { 
            "InstanceId": InstanceId,
        })
        return Instance(**response)

    async def GetInstanceAsync(self, InstanceId: UUID) -> Instance:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: Instance
        """
        response: dict = await self.api_call_async("ADSModule/GetInstance", { 
            "InstanceId": InstanceId,
        })
        return Instance(**response)

    def GetInstanceNetworkInfo(self, InstanceName: str) -> list[Any]:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: list[Any]
        """
        response: dict = self.api_call("ADSModule/GetInstanceNetworkInfo", { 
            "InstanceName": InstanceName,
        })
        return [Any(**x) for x in response]

    async def GetInstanceNetworkInfoAsync(self, InstanceName: str) -> list[Any]:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("ADSModule/GetInstanceNetworkInfo", { 
            "InstanceName": InstanceName,
        })
        return [Any(**x) for x in response]

    def GetInstanceStatuses(self, ) -> list[InstanceStatus]:
        """
        Name Description Optional
        :returns: list[InstanceStatus]
        """
        response: dict = self.api_call("ADSModule/GetInstanceStatuses", { 
        })
        return [InstanceStatus(**x) for x in response]

    async def GetInstanceStatusesAsync(self, ) -> list[InstanceStatus]:
        """
        Name Description Optional
        :returns: list[InstanceStatus]
        """
        response: dict = await self.api_call_async("ADSModule/GetInstanceStatuses", { 
        })
        return [InstanceStatus(**x) for x in response]

    def GetInstances(self, ForceIncludeSelf: bool) -> list[IADSInstance]:
        """
        Name Description Optional
        :param ForceIncludeSelf: {bool}  True
        :returns: list[IADSInstance]
        """
        response: dict = self.api_call("ADSModule/GetInstances", { 
            "ForceIncludeSelf": ForceIncludeSelf,
        })
        return [IADSInstance(**x) for x in response]

    async def GetInstancesAsync(self, ForceIncludeSelf: bool) -> list[IADSInstance]:
        """
        Name Description Optional
        :param ForceIncludeSelf: {bool}  True
        :returns: list[IADSInstance]
        """
        response: dict = await self.api_call_async("ADSModule/GetInstances", { 
            "ForceIncludeSelf": ForceIncludeSelf,
        })
        return [IADSInstance(**x) for x in response]

    def GetLocalInstances(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("ADSModule/GetLocalInstances", { 
        })
        return [dict(**x) for x in response]

    async def GetLocalInstancesAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("ADSModule/GetLocalInstances", { 
        })
        return [dict(**x) for x in response]

    def GetProvisionArguments(self, ModuleName: str) -> list[Any]:
        """
        Name Description Optional
        :param ModuleName: {str}  False
        :returns: list[Any]
        """
        response: dict = self.api_call("ADSModule/GetProvisionArguments", { 
            "ModuleName": ModuleName,
        })
        return [Any(**x) for x in response]

    async def GetProvisionArgumentsAsync(self, ModuleName: str) -> list[Any]:
        """
        Name Description Optional
        :param ModuleName: {str}  False
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("ADSModule/GetProvisionArguments", { 
            "ModuleName": ModuleName,
        })
        return [Any(**x) for x in response]

    def GetProvisionFitness(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = self.api_call("ADSModule/GetProvisionFitness", { 
        })
        return dict(**response)

    async def GetProvisionFitnessAsync(self, ) -> dict:
        """
        Name Description Optional
        :returns: dict
        """
        response: dict = await self.api_call_async("ADSModule/GetProvisionFitness", { 
        })
        return dict(**response)

    def GetSupportedApplications(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = self.api_call("ADSModule/GetSupportedApplications", { 
        })
        return [Any(**x) for x in response]

    async def GetSupportedApplicationsAsync(self, ) -> list[Any]:
        """
        Name Description Optional
        :returns: list[Any]
        """
        response: dict = await self.api_call_async("ADSModule/GetSupportedApplications", { 
        })
        return [Any(**x) for x in response]

    def GetTargetInfo(self, ) -> RemoteTargetInfo:
        """
        Name Description Optional
        :returns: RemoteTargetInfo
        """
        response: dict = self.api_call("ADSModule/GetTargetInfo", { 
        })
        return RemoteTargetInfo(**response)

    async def GetTargetInfoAsync(self, ) -> RemoteTargetInfo:
        """
        Name Description Optional
        :returns: RemoteTargetInfo
        """
        response: dict = await self.api_call_async("ADSModule/GetTargetInfo", { 
        })
        return RemoteTargetInfo(**response)

    def HandoutInstanceConfigs(self, ForModule: str, SettingNode: str, Values: list[str]) -> ActionResult:
        """
        Name Description Optional
        :param ForModule: {str}  False
        :param SettingNode: {str}  False
        :param Values: {list[str]}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/HandoutInstanceConfigs", { 
            "ForModule": ForModule,
            "SettingNode": SettingNode,
            "Values": Values,
        })
        return ActionResult(**response)

    async def HandoutInstanceConfigsAsync(self, ForModule: str, SettingNode: str, Values: list[str]) -> ActionResult:
        """
        Name Description Optional
        :param ForModule: {str}  False
        :param SettingNode: {str}  False
        :param Values: {list[str]}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/HandoutInstanceConfigs", { 
            "ForModule": ForModule,
            "SettingNode": SettingNode,
            "Values": Values,
        })
        return ActionResult(**response)

    def ManageInstance(self, InstanceId: UUID) -> ActionResult[str]:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult[str]
        """
        response: dict = self.api_call("ADSModule/ManageInstance", { 
            "InstanceId": InstanceId,
        })
        return ActionResult[str](**response)

    async def ManageInstanceAsync(self, InstanceId: UUID) -> ActionResult[str]:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :returns: ActionResult[str]
        """
        response: dict = await self.api_call_async("ADSModule/ManageInstance", { 
            "InstanceId": InstanceId,
        })
        return ActionResult[str](**response)

    def ModifyCustomFirewallRule(self, instanceId: UUID, PortNumber: int, Range: int, Protocol: Any, Description: str, Open: bool) -> ActionResult:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :param PortNumber: {int}  False
        :param Range: {int}  False
        :param Protocol: {Any}  False
        :param Description: {str}  False
        :param Open: {bool}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/ModifyCustomFirewallRule", { 
            "instanceId": instanceId,
            "PortNumber": PortNumber,
            "Range": Range,
            "Protocol": Protocol,
            "Description": Description,
            "Open": Open,
        })
        return ActionResult(**response)

    async def ModifyCustomFirewallRuleAsync(self, instanceId: UUID, PortNumber: int, Range: int, Protocol: Any, Description: str, Open: bool) -> ActionResult:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :param PortNumber: {int}  False
        :param Range: {int}  False
        :param Protocol: {Any}  False
        :param Description: {str}  False
        :param Open: {bool}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/ModifyCustomFirewallRule", { 
            "instanceId": instanceId,
            "PortNumber": PortNumber,
            "Range": Range,
            "Protocol": Protocol,
            "Description": Description,
            "Open": Open,
        })
        return ActionResult(**response)

    def MoveInstanceDatastore(self, instanceId: UUID, datastoreId: int) -> RunningTask:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :param datastoreId: {int}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/MoveInstanceDatastore", { 
            "instanceId": instanceId,
            "datastoreId": datastoreId,
        })
        return RunningTask(**response)

    async def MoveInstanceDatastoreAsync(self, instanceId: UUID, datastoreId: int) -> RunningTask:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :param datastoreId: {int}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/MoveInstanceDatastore", { 
            "instanceId": instanceId,
            "datastoreId": datastoreId,
        })
        return RunningTask(**response)

    def ReactivateLocalInstances(self, ) -> RunningTask:
        """
        Name Description Optional
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/ReactivateLocalInstances", { 
        })
        return RunningTask(**response)

    async def ReactivateLocalInstancesAsync(self, ) -> RunningTask:
        """
        Name Description Optional
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/ReactivateLocalInstances", { 
        })
        return RunningTask(**response)

    def RefreshAppCache(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = self.api_call("ADSModule/RefreshAppCache", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RefreshAppCacheAsync(self, ) -> Void:
        """
        Name Description Optional
        :returns: Void
        """
        response: dict = await self.api_call_async("ADSModule/RefreshAppCache", { 
        })
        if response == None:
            response = {}
        return Void(**response)

    def RefreshGroup(self, GroupId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param GroupId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/RefreshGroup", { 
            "GroupId": GroupId,
        })
        return ActionResult(**response)

    async def RefreshGroupAsync(self, GroupId: UUID) -> ActionResult:
        """
        Name Description Optional
        :param GroupId: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/RefreshGroup", { 
            "GroupId": GroupId,
        })
        return ActionResult(**response)

    def RefreshInstanceConfig(self, InstanceId: str, AndUpdateInstance: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param AndUpdateInstance: {bool}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/RefreshInstanceConfig", { 
            "InstanceId": InstanceId,
            "AndUpdateInstance": AndUpdateInstance,
        })
        return ActionResult(**response)

    async def RefreshInstanceConfigAsync(self, InstanceId: str, AndUpdateInstance: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param AndUpdateInstance: {bool}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/RefreshInstanceConfig", { 
            "InstanceId": InstanceId,
            "AndUpdateInstance": AndUpdateInstance,
        })
        return ActionResult(**response)

    def RefreshRemoteConfigStores(self, force: bool) -> Void:
        """
        Name Description Optional
        :param force: {bool}  True
        :returns: Void
        """
        response: dict = self.api_call("ADSModule/RefreshRemoteConfigStores", { 
            "force": force,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def RefreshRemoteConfigStoresAsync(self, force: bool) -> Void:
        """
        Name Description Optional
        :param force: {bool}  True
        :returns: Void
        """
        response: dict = await self.api_call_async("ADSModule/RefreshRemoteConfigStores", { 
            "force": force,
        })
        if response == None:
            response = {}
        return Void(**response)

    def RegisterTarget(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str) -> ActionResult:
        """
        Name Description Optional
        :param controllerUrl: {str}  False
        :param myUrl: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :param friendlyName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/RegisterTarget", { 
            "controllerUrl": controllerUrl,
            "myUrl": myUrl,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
            "friendlyName": friendlyName,
        })
        return ActionResult(**response)

    async def RegisterTargetAsync(self, controllerUrl: str, myUrl: str, username: str, password: str, twoFactorToken: str, friendlyName: str) -> ActionResult:
        """
        Name Description Optional
        :param controllerUrl: {str}  False
        :param myUrl: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :param friendlyName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/RegisterTarget", { 
            "controllerUrl": controllerUrl,
            "myUrl": myUrl,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
            "friendlyName": friendlyName,
        })
        return ActionResult(**response)

    def RepairDatastore(self, id: int) -> RunningTask:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/RepairDatastore", { 
            "id": id,
        })
        return RunningTask(**response)

    async def RepairDatastoreAsync(self, id: int) -> RunningTask:
        """
        Name Description Optional
        :param id: {int}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/RepairDatastore", { 
            "id": id,
        })
        return RunningTask(**response)

    def RequestDatastoreSizeCalculation(self, datastoreId: int) -> RunningTask:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/RequestDatastoreSizeCalculation", { 
            "datastoreId": datastoreId,
        })
        return RunningTask(**response)

    async def RequestDatastoreSizeCalculationAsync(self, datastoreId: int) -> RunningTask:
        """
        Name Description Optional
        :param datastoreId: {int}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/RequestDatastoreSizeCalculation", { 
            "datastoreId": datastoreId,
        })
        return RunningTask(**response)

    def RestartInstance(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/RestartInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    async def RestartInstanceAsync(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/RestartInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    def Servers(self, id: str, Data: dict, RealIP: str) -> dict:
        """
        Name Description Optional
        :param id: {str}  False
        :param Data: {dict}  False
        :param RealIP: {str}  False
        :returns: dict
        """
        response: dict = self.api_call("ADSModule/Servers", { 
            "id": id,
            "Data": Data,
            "RealIP": RealIP,
        })
        return dict(**response)

    async def ServersAsync(self, id: str, Data: dict, RealIP: str) -> dict:
        """
        Name Description Optional
        :param id: {str}  False
        :param Data: {dict}  False
        :param RealIP: {str}  False
        :returns: dict
        """
        response: dict = await self.api_call_async("ADSModule/Servers", { 
            "id": id,
            "Data": Data,
            "RealIP": RealIP,
        })
        return dict(**response)

    def SetInstanceConfig(self, InstanceName: str, SettingNode: str, Value: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param SettingNode: {str}  False
        :param Value: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/SetInstanceConfig", { 
            "InstanceName": InstanceName,
            "SettingNode": SettingNode,
            "Value": Value,
        })
        return ActionResult(**response)

    async def SetInstanceConfigAsync(self, InstanceName: str, SettingNode: str, Value: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param SettingNode: {str}  False
        :param Value: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/SetInstanceConfig", { 
            "InstanceName": InstanceName,
            "SettingNode": SettingNode,
            "Value": Value,
        })
        return ActionResult(**response)

    def SetInstanceNetworkInfo(self, InstanceId: UUID, PortMappings: dict[str, int]) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :param PortMappings: {dict[str, int]}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/SetInstanceNetworkInfo", { 
            "InstanceId": InstanceId,
            "PortMappings": PortMappings,
        })
        return ActionResult(**response)

    async def SetInstanceNetworkInfoAsync(self, InstanceId: UUID, PortMappings: dict[str, int]) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {UUID}  False
        :param PortMappings: {dict[str, int]}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/SetInstanceNetworkInfo", { 
            "InstanceId": InstanceId,
            "PortMappings": PortMappings,
        })
        return ActionResult(**response)

    def SetInstanceSuspended(self, InstanceName: str, Suspended: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param Suspended: {bool}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/SetInstanceSuspended", { 
            "InstanceName": InstanceName,
            "Suspended": Suspended,
        })
        return ActionResult(**response)

    async def SetInstanceSuspendedAsync(self, InstanceName: str, Suspended: bool) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :param Suspended: {bool}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/SetInstanceSuspended", { 
            "InstanceName": InstanceName,
            "Suspended": Suspended,
        })
        return ActionResult(**response)

    def StartAllInstances(self, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/StartAllInstances", { 
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    async def StartAllInstancesAsync(self, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/StartAllInstances", { 
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    def StartInstance(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/StartInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    async def StartInstanceAsync(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/StartInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    def StopAllInstances(self, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/StopAllInstances", { 
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    async def StopAllInstancesAsync(self, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/StopAllInstances", { 
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    def StopInstance(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/StopInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    async def StopInstanceAsync(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/StopInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    def TestADSLoginDetails(self, url: str, username: str, password: str, twoFactorToken: str) -> ActionResult:
        """
        Name Description Optional
        :param url: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/TestADSLoginDetails", { 
            "url": url,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
        })
        return ActionResult(**response)

    async def TestADSLoginDetailsAsync(self, url: str, username: str, password: str, twoFactorToken: str) -> ActionResult:
        """
        Name Description Optional
        :param url: {str}  False
        :param username: {str}  False
        :param password: {str}  False
        :param twoFactorToken: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/TestADSLoginDetails", { 
            "url": url,
            "username": username,
            "password": password,
            "twoFactorToken": twoFactorToken,
        })
        return ActionResult(**response)

    def UpdateDatastore(self, updatedDatastore: InstanceDatastore) -> ActionResult:
        """
        Name Description Optional
        :param updatedDatastore: {InstanceDatastore}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpdateDatastore", { 
            "updatedDatastore": updatedDatastore,
        })
        return ActionResult(**response)

    async def UpdateDatastoreAsync(self, updatedDatastore: InstanceDatastore) -> ActionResult:
        """
        Name Description Optional
        :param updatedDatastore: {InstanceDatastore}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpdateDatastore", { 
            "updatedDatastore": updatedDatastore,
        })
        return ActionResult(**response)

    def UpdateDeploymentTemplate(self, templateToUpdate: Any) -> ActionResult:
        """
        Name Description Optional
        :param templateToUpdate: {Any}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpdateDeploymentTemplate", { 
            "templateToUpdate": templateToUpdate,
        })
        return ActionResult(**response)

    async def UpdateDeploymentTemplateAsync(self, templateToUpdate: Any) -> ActionResult:
        """
        Name Description Optional
        :param templateToUpdate: {Any}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpdateDeploymentTemplate", { 
            "templateToUpdate": templateToUpdate,
        })
        return ActionResult(**response)

    def UpdateInstanceInfo(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy: Any, ContainerMaxCPU: Any, ContainerImage: str, ContainerSwap: int, WelcomeMessage: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param FriendlyName: {str}  False
        :param Description: {str}  False
        :param StartOnBoot: {bool}  False
        :param Suspended: {bool}  False
        :param ExcludeFromFirewall: {bool}  False
        :param RunInContainer: {bool}  False
        :param ContainerMemory: {int}  False
        :param MemoryPolicy: {Any}  False
        :param ContainerMaxCPU: {Any}  False
        :param ContainerImage: {str}  False
        :param ContainerSwap: {int}  False
        :param WelcomeMessage: {str}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpdateInstanceInfo", { 
            "InstanceId": InstanceId,
            "FriendlyName": FriendlyName,
            "Description": Description,
            "StartOnBoot": StartOnBoot,
            "Suspended": Suspended,
            "ExcludeFromFirewall": ExcludeFromFirewall,
            "RunInContainer": RunInContainer,
            "ContainerMemory": ContainerMemory,
            "MemoryPolicy": MemoryPolicy,
            "ContainerMaxCPU": ContainerMaxCPU,
            "ContainerImage": ContainerImage,
            "ContainerSwap": ContainerSwap,
            "WelcomeMessage": WelcomeMessage,
        })
        return ActionResult(**response)

    async def UpdateInstanceInfoAsync(self, InstanceId: str, FriendlyName: str, Description: str, StartOnBoot: bool, Suspended: bool, ExcludeFromFirewall: bool, RunInContainer: bool, ContainerMemory: int, MemoryPolicy: Any, ContainerMaxCPU: Any, ContainerImage: str, ContainerSwap: int, WelcomeMessage: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: {str}  False
        :param FriendlyName: {str}  False
        :param Description: {str}  False
        :param StartOnBoot: {bool}  False
        :param Suspended: {bool}  False
        :param ExcludeFromFirewall: {bool}  False
        :param RunInContainer: {bool}  False
        :param ContainerMemory: {int}  False
        :param MemoryPolicy: {Any}  False
        :param ContainerMaxCPU: {Any}  False
        :param ContainerImage: {str}  False
        :param ContainerSwap: {int}  False
        :param WelcomeMessage: {str}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpdateInstanceInfo", { 
            "InstanceId": InstanceId,
            "FriendlyName": FriendlyName,
            "Description": Description,
            "StartOnBoot": StartOnBoot,
            "Suspended": Suspended,
            "ExcludeFromFirewall": ExcludeFromFirewall,
            "RunInContainer": RunInContainer,
            "ContainerMemory": ContainerMemory,
            "MemoryPolicy": MemoryPolicy,
            "ContainerMaxCPU": ContainerMaxCPU,
            "ContainerImage": ContainerImage,
            "ContainerSwap": ContainerSwap,
            "WelcomeMessage": WelcomeMessage,
        })
        return ActionResult(**response)

    def UpdateTarget(self, TargetID: UUID) -> Void:
        """
        Name Description Optional
        :param TargetID: {UUID}  False
        :returns: Void
        """
        response: dict = self.api_call("ADSModule/UpdateTarget", { 
            "TargetID": TargetID,
        })
        if response == None:
            response = {}
        return Void(**response)

    async def UpdateTargetAsync(self, TargetID: UUID) -> Void:
        """
        Name Description Optional
        :param TargetID: {UUID}  False
        :returns: Void
        """
        response: dict = await self.api_call_async("ADSModule/UpdateTarget", { 
            "TargetID": TargetID,
        })
        if response == None:
            response = {}
        return Void(**response)

    def UpdateTargetInfo(self, Id: UUID, FriendlyName: str, Url: URL, Description: str, Tags: list[str]) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param FriendlyName: {str}  False
        :param Url: {URL}  False
        :param Description: {str}  False
        :param Tags: {list[str]}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpdateTargetInfo", { 
            "Id": Id,
            "FriendlyName": FriendlyName,
            "Url": Url,
            "Description": Description,
            "Tags": Tags,
        })
        return ActionResult(**response)

    async def UpdateTargetInfoAsync(self, Id: UUID, FriendlyName: str, Url: URL, Description: str, Tags: list[str]) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :param FriendlyName: {str}  False
        :param Url: {URL}  False
        :param Description: {str}  False
        :param Tags: {list[str]}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpdateTargetInfo", { 
            "Id": Id,
            "FriendlyName": FriendlyName,
            "Url": Url,
            "Description": Description,
            "Tags": Tags,
        })
        return ActionResult(**response)

    def UpgradeAllInstances(self, RestartRunning: bool, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param RestartRunning: {bool}  False
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpgradeAllInstances", { 
            "RestartRunning": RestartRunning,
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    async def UpgradeAllInstancesAsync(self, RestartRunning: bool, TargetADSInstance: UUID) -> ActionResult:
        """
        Name Description Optional
        :param RestartRunning: {bool}  False
        :param TargetADSInstance: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpgradeAllInstances", { 
            "RestartRunning": RestartRunning,
            "TargetADSInstance": TargetADSInstance,
        })
        return ActionResult(**response)

    def UpgradeInstance(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/UpgradeInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    async def UpgradeInstanceAsync(self, InstanceName: str) -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: {str}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/UpgradeInstance", { 
            "InstanceName": InstanceName,
        })
        return ActionResult(**response)

    def CreateInstanceFromSpec(self, SpecId: UUID, TargetADSInstance: UUID, FriendlyName: str, PostCreate: Any, StartOnBoot: bool, TargetDatastore: int) -> ActionResult:
        """
        Name Description Optional
        :param SpecId: {UUID}  False
        :param TargetADSInstance: {UUID}  False
        :param FriendlyName: {str}  False
        :param PostCreate: {Any}  True
        :param StartOnBoot: {bool}  True
        :param TargetDatastore: {int}  True
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/CreateInstanceFromSpec", { 
            "SpecId": SpecId,
            "TargetADSInstance": TargetADSInstance,
            "FriendlyName": FriendlyName,
            "PostCreate": PostCreate,
            "StartOnBoot": StartOnBoot,
            "TargetDatastore": TargetDatastore,
        })
        return ActionResult(**response)

    async def CreateInstanceFromSpecAsync(self, SpecId: UUID, TargetADSInstance: UUID, FriendlyName: str, PostCreate: Any, StartOnBoot: bool, TargetDatastore: int) -> ActionResult:
        """
        Name Description Optional
        :param SpecId: {UUID}  False
        :param TargetADSInstance: {UUID}  False
        :param FriendlyName: {str}  False
        :param PostCreate: {Any}  True
        :param StartOnBoot: {bool}  True
        :param TargetDatastore: {int}  True
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/CreateInstanceFromSpec", { 
            "SpecId": SpecId,
            "TargetADSInstance": TargetADSInstance,
            "FriendlyName": FriendlyName,
            "PostCreate": PostCreate,
            "StartOnBoot": StartOnBoot,
            "TargetDatastore": TargetDatastore,
        })
        return ActionResult(**response)

    def DetachTarget(self, Id: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: ActionResult
        """
        response: dict = self.api_call("ADSModule/DetachTarget", { 
            "Id": Id,
        })
        return ActionResult(**response)

    async def DetachTargetAsync(self, Id: UUID) -> ActionResult:
        """
        Name Description Optional
        :param Id: {UUID}  False
        :returns: ActionResult
        """
        response: dict = await self.api_call_async("ADSModule/DetachTarget", { 
            "Id": Id,
        })
        return ActionResult(**response)

    def GetSupportedAppSummaries(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = self.api_call("ADSModule/GetSupportedAppSummaries", { 
        })
        return [dict(**x) for x in response]

    async def GetSupportedAppSummariesAsync(self, ) -> list[dict]:
        """
        Name Description Optional
        :returns: list[dict]
        """
        response: dict = await self.api_call_async("ADSModule/GetSupportedAppSummaries", { 
        })
        return [dict(**x) for x in response]

    def ReactivateInstance(self, instanceId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = self.api_call("ADSModule/ReactivateInstance", { 
            "instanceId": instanceId,
        })
        return RunningTask(**response)

    async def ReactivateInstanceAsync(self, instanceId: UUID) -> RunningTask:
        """
        Name Description Optional
        :param instanceId: {UUID}  False
        :returns: RunningTask
        """
        response: dict = await self.api_call_async("ADSModule/ReactivateInstance", { 
            "instanceId": instanceId,
        })
        return RunningTask(**response)

