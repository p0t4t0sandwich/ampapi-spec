from __future__ import annotations

from .ampapi import AMPAPI
from .auth import AuthProvider
from .types import *

class ADSModule(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def AddDatastore(self, newDatastore: 'InstanceDatastore') -> ActionResult:
        """
        Name Description Optional
        :param newDatastore: 
        :type newDatastore: InstanceDatastore
        :returns: ActionResult
        """
        return self.api_call("ADSModule/AddDatastore", {
            'newDatastore': newDatastore
        })

    def ApplyInstanceConfiguration(self, InstanceID: 'str', Args: 'dict[str, str]', RebuildConfiguration: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param InstanceID: 
        :type InstanceID: str
        :param Args: 
        :type Args: dict[str, str]
        :param RebuildConfiguration: 
        :type RebuildConfiguration: bool
        :returns: ActionResult
        """
        return self.api_call("ADSModule/ApplyInstanceConfiguration", {
            'InstanceID': InstanceID,
            'Args': Args,
            'RebuildConfiguration': RebuildConfiguration
        })

    def ApplyTemplate(self, InstanceID: 'str', TemplateID: 'int', NewFriendlyName: 'str', Secret: 'str', RestartIfPreviouslyRunning: 'bool') -> ActionResult:
        """Overlays an existing template on an existing instance. Used to perform package reconfigurations. Do not use this to 'transform' an existing application into another. The instance should be deleted and re-created in that situation.
        Name Description Optional
        :param InstanceID: 
        :type InstanceID: str
        :param TemplateID: 
        :type TemplateID: int
        :param NewFriendlyName: 
        :type NewFriendlyName: str
        :param Secret: 
        :type Secret: str
        :param RestartIfPreviouslyRunning: 
        :type RestartIfPreviouslyRunning: bool
        :returns: ActionResult
        """
        return self.api_call("ADSModule/ApplyTemplate", {
            'InstanceID': InstanceID,
            'TemplateID': TemplateID,
            'NewFriendlyName': NewFriendlyName,
            'Secret': Secret,
            'RestartIfPreviouslyRunning': RestartIfPreviouslyRunning
        })

    def AttachADS(self, Friendly: 'str', IsHTTPS: 'bool', Host: 'str', Port: 'int', InstanceID: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Friendly: 
        :type Friendly: str
        :param IsHTTPS: 
        :type IsHTTPS: bool
        :param Host: 
        :type Host: str
        :param Port: 
        :type Port: int
        :param InstanceID: 
        :type InstanceID: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/AttachADS", {
            'Friendly': Friendly,
            'IsHTTPS': IsHTTPS,
            'Host': Host,
            'Port': Port,
            'InstanceID': InstanceID
        })

    def CloneTemplate(self, Id: 'int', NewName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: int
        :param NewName: 
        :type NewName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/CloneTemplate", {
            'Id': Id,
            'NewName': NewName
        })

    def CreateDeploymentTemplate(self, Name: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Name: 
        :type Name: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/CreateDeploymentTemplate", {
            'Name': Name
        })

    def CreateInstance(self, TargetADSInstance: 'str', NewInstanceId: 'str', Module: 'str', InstanceName: 'str', FriendlyName: 'str', IPBinding: 'str', PortNumber: 'int', AdminUsername: 'str', AdminPassword: 'str', ProvisionSettings: 'dict[str, str]', AutoConfigure: 'bool', StartOnBoot: 'bool', DisplayImageSource: 'str', TargetDatastore: 'int', PostCreate: 'PostCreateAppActions') -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: 
        :type TargetADSInstance: str
        :param NewInstanceId: 
        :type NewInstanceId: str
        :param Module: 
        :type Module: str
        :param InstanceName: 
        :type InstanceName: str
        :param FriendlyName: 
        :type FriendlyName: str
        :param IPBinding: 
        :type IPBinding: str
        :param PortNumber: 
        :type PortNumber: int
        :param AdminUsername: 
        :type AdminUsername: str
        :param AdminPassword: 
        :type AdminPassword: str
        :param ProvisionSettings: 
        :type ProvisionSettings: dict[str, str]
        :param AutoConfigure: When enabled, all settings other than the Module, Target and FriendlyName are ignored and replaced with automatically generated values.
        :type AutoConfigure: bool
        :param StartOnBoot: 
        :type StartOnBoot: bool
        :param DisplayImageSource: 
        :type DisplayImageSource: str
        :param TargetDatastore: 
        :type TargetDatastore: int
        :param PostCreate: 
        :type PostCreate: PostCreateAppActions
        :returns: ActionResult
        """
        return self.api_call("ADSModule/CreateInstance", {
            'TargetADSInstance': TargetADSInstance,
            'NewInstanceId': NewInstanceId,
            'Module': Module,
            'InstanceName': InstanceName,
            'FriendlyName': FriendlyName,
            'IPBinding': IPBinding,
            'PortNumber': PortNumber,
            'AdminUsername': AdminUsername,
            'AdminPassword': AdminPassword,
            'ProvisionSettings': ProvisionSettings,
            'AutoConfigure': AutoConfigure,
            'StartOnBoot': StartOnBoot,
            'DisplayImageSource': DisplayImageSource,
            'TargetDatastore': TargetDatastore,
            'PostCreate': PostCreate
        })

    def CreateInstanceFromSpec(self, SpecId: 'str', TargetADSInstance: 'str', FriendlyName: 'str', PostCreate: 'PostCreateAppActions', StartOnBoot: 'bool', TargetDatastore: 'int') -> ActionResult:
        """
        Name Description Optional
        :param SpecId: 
        :type SpecId: str
        :param TargetADSInstance: 
        :type TargetADSInstance: str
        :param FriendlyName: 
        :type FriendlyName: str
        :param PostCreate: 
        :type PostCreate: PostCreateAppActions
        :param StartOnBoot: 
        :type StartOnBoot: bool
        :param TargetDatastore: 
        :type TargetDatastore: int
        :returns: ActionResult
        """
        return self.api_call("ADSModule/CreateInstanceFromSpec", {
            'SpecId': SpecId,
            'TargetADSInstance': TargetADSInstance,
            'FriendlyName': FriendlyName,
            'PostCreate': PostCreate,
            'StartOnBoot': StartOnBoot,
            'TargetDatastore': TargetDatastore
        })

    def CreateLocalInstance(self, Instance: 'LocalAMPInstance', PostCreate: 'PostCreateAppActions') -> ActionResult:
        """
        Name Description Optional
        :param Instance: 
        :type Instance: LocalAMPInstance
        :param PostCreate: 
        :type PostCreate: PostCreateAppActions
        :returns: ActionResult
        """
        return self.api_call("ADSModule/CreateLocalInstance", {
            'Instance': Instance,
            'PostCreate': PostCreate
        })

    def DeleteDatastore(self, id: 'int') -> ActionResult:
        """
        Name Description Optional
        :param id: 
        :type id: int
        :returns: ActionResult
        """
        return self.api_call("ADSModule/DeleteDatastore", {
            'id': id
        })

    def DeleteDeploymentTemplate(self, Id: 'int') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: int
        :returns: ActionResult
        """
        return self.api_call("ADSModule/DeleteDeploymentTemplate", {
            'Id': Id
        })

    def DeleteInstance(self, InstanceName: 'str') -> RunningTask:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: RunningTask
        """
        return self.api_call("ADSModule/DeleteInstance", {
            'InstanceName': InstanceName
        })

    def DeleteInstanceUsers(self, InstanceId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/DeleteInstanceUsers", {
            'InstanceId': InstanceId
        })

    def DeployTemplate(self, TemplateID: 'int', NewUsername: 'str', NewPassword: 'str', NewEmail: 'str', RequiredTags: 'list[str]', Tag: 'str', FriendlyName: 'str', Secret: 'str', ExtraProvisionSettings: 'dict[str, str]', PostCreate: 'PostCreateAppActions') -> RunningTask:
        """
        Name Description Optional
        :param TemplateID: The ID of the template to be deployed, as per the Template Management UI in AMP itself.
        :type TemplateID: int
        :param NewUsername: If specified, AMP will create a new user with this name for this instance. Must be unique. If this user already exists, this will be ignored but the new instance will be assigned to this user.
        :type NewUsername: str
        :param NewPassword: If 'NewUsername' is specified and the user doesn't already exist, the password that will be assigned to this user.
        :type NewPassword: str
        :param NewEmail: If 'NewUsername' is specified and the user doesn't already exist, the email address that will be assigned to this user.
        :type NewEmail: str
        :param RequiredTags: If specified, AMP will only deploy this template to targets that have every single 'tag' specified in their target configuration. You can adjust this via the controller by clicking 'Edit' on the target settings.
        :type RequiredTags: list[str]
        :param Tag: Unrelated to RequiredTags. This is to uniquely identify this instance to your own systems. It may be something like an order ID or service ID so you can find the associated instance again at a later time. If 'UseTagAsInstanceName' is enabled, then this will also be used as the instance name for the created instance - but it must be unique.
        :type Tag: str
        :param FriendlyName: A friendly name for this instance. If left blank, AMP will generate one for you.
        :type FriendlyName: str
        :param Secret: Must be a non-empty strong in order to get a callback on deployment state change. This secret will be passed back to you in the callback so you can verify the request.
        :type Secret: str
        :param ExtraProvisionSettings: A dictionary of setting nodes and values to create the new instance with. Identical in function to the provisioning arguments in the template itself.
        :type ExtraProvisionSettings: dict[str, str]
        :param PostCreate: 0: Do Nothing, 1: Update Once, 2: Update Always, 3: Update and Start Once, 4: Update and Start Always, 5. Start Always
        :type PostCreate: PostCreateAppActions
        :returns: RunningTask
        """
        return self.api_call("ADSModule/DeployTemplate", {
            'TemplateID': TemplateID,
            'NewUsername': NewUsername,
            'NewPassword': NewPassword,
            'NewEmail': NewEmail,
            'RequiredTags': RequiredTags,
            'Tag': Tag,
            'FriendlyName': FriendlyName,
            'Secret': Secret,
            'ExtraProvisionSettings': ExtraProvisionSettings,
            'PostCreate': PostCreate
        })

    def DetachTarget(self, Id: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/DetachTarget", {
            'Id': Id
        })

    def ExtractEverywhere(self, SourceArchive: 'str') -> ActionResult:
        """
        Name Description Optional
        :param SourceArchive: 
        :type SourceArchive: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/ExtractEverywhere", {
            'SourceArchive': SourceArchive
        })

    def GetApplicationEndpoints(self, instanceId: 'str') -> list[EndpointInfo]:
        """
        Name Description Optional
        :param instanceId: 
        :type instanceId: str
        :returns: list[EndpointInfo]
        """
        return self.api_call("ADSModule/GetApplicationEndpoints", {
            'instanceId': instanceId
        })

    def GetDatastore(self, id: 'int') -> InstanceDatastore:
        """
        Name Description Optional
        :param id: 
        :type id: int
        :returns: InstanceDatastore
        """
        return self.api_call("ADSModule/GetDatastore", {
            'id': id
        })

    def GetDatastoreInstances(self, datastoreId: 'int') -> list[InstanceSummary]:
        """
        Name Description Optional
        :param datastoreId: 
        :type datastoreId: int
        :returns: list[InstanceSummary]
        """
        return self.api_call("ADSModule/GetDatastoreInstances", {
            'datastoreId': datastoreId
        })

    def GetDatastores(self, ) -> list[InstanceDatastore]:
        """
        Name Description Optional

        :returns: list[InstanceDatastore]
        """
        return self.api_call("ADSModule/GetDatastores", {})

    def GetDeploymentTemplates(self, ) -> list[DeploymentTemplate]:
        """
        Name Description Optional

        :returns: list[DeploymentTemplate]
        """
        return self.api_call("ADSModule/GetDeploymentTemplates", {})

    def GetGroup(self, GroupId: 'str') -> IADSInstance:
        """
        Name Description Optional
        :param GroupId: 
        :type GroupId: str
        :returns: IADSInstance
        """
        return self.api_call("ADSModule/GetGroup", {
            'GroupId': GroupId
        })

    def GetInstance(self, InstanceId: 'str') -> InstanceSummary:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :returns: InstanceSummary
        """
        return self.api_call("ADSModule/GetInstance", {
            'InstanceId': InstanceId
        })

    def GetInstanceNetworkInfo(self, InstanceName: 'str') -> list[PortUsage]:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: list[PortUsage]
        """
        return self.api_call("ADSModule/GetInstanceNetworkInfo", {
            'InstanceName': InstanceName
        })

    def GetInstanceStatuses(self, ) -> list[InstanceStatus]:
        """
        Name Description Optional

        :returns: list[InstanceStatus]
        """
        return self.api_call("ADSModule/GetInstanceStatuses", {})

    def GetInstances(self, ForceIncludeSelf: 'bool') -> list[IADSInstance]:
        """
        Name Description Optional
        :param ForceIncludeSelf: 
        :type ForceIncludeSelf: bool
        :returns: list[IADSInstance]
        """
        return self.api_call("ADSModule/GetInstances", {
            'ForceIncludeSelf': ForceIncludeSelf
        })

    def GetLocalInstances(self, ) -> list[InstanceSummary]:
        """
        Name Description Optional

        :returns: list[InstanceSummary]
        """
        return self.api_call("ADSModule/GetLocalInstances", {})

    def GetProvisionArguments(self, ModuleName: 'str') -> list[ProvisionSettingInfo]:
        """
        Name Description Optional
        :param ModuleName: 
        :type ModuleName: str
        :returns: list[ProvisionSettingInfo]
        """
        return self.api_call("ADSModule/GetProvisionArguments", {
            'ModuleName': ModuleName
        })

    def GetProvisionFitness(self, ) -> ProvisionFitness:
        """
        Name Description Optional

        :returns: ProvisionFitness
        """
        return self.api_call("ADSModule/GetProvisionFitness", {})

    def GetSupportedAppSummaries(self, ) -> list[ApplicationSpecSummary]:
        """
        Name Description Optional

        :returns: list[ApplicationSpecSummary]
        """
        return self.api_call("ADSModule/GetSupportedAppSummaries", {})

    def GetSupportedApplications(self, ) -> list[ApplicationSpec]:
        """
        Name Description Optional

        :returns: list[ApplicationSpec]
        """
        return self.api_call("ADSModule/GetSupportedApplications", {})

    def GetTargetInfo(self, ) -> RemoteTargetInfo:
        """
        Name Description Optional

        :returns: RemoteTargetInfo
        """
        return self.api_call("ADSModule/GetTargetInfo", {})

    def HandoutInstanceConfigs(self, ForModule: 'str', SettingNode: 'str', Values: 'list[str]') -> ActionResult:
        """
        Name Description Optional
        :param ForModule: 
        :type ForModule: str
        :param SettingNode: 
        :type SettingNode: str
        :param Values: 
        :type Values: list[str]
        :returns: ActionResult
        """
        return self.api_call("ADSModule/HandoutInstanceConfigs", {
            'ForModule': ForModule,
            'SettingNode': SettingNode,
            'Values': Values
        })

    def ManageInstance(self, InstanceId: 'str') -> ActionResult[str]:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :returns: ActionResult[str]
        """
        return self.api_call("ADSModule/ManageInstance", {
            'InstanceId': InstanceId
        })

    def ModifyCustomFirewallRule(self, instanceId: 'str', PortNumber: 'int', Range: 'int', Protocol: 'PortProtocol', Description: 'str', Open: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param instanceId: 
        :type instanceId: str
        :param PortNumber: 
        :type PortNumber: int
        :param Range: 
        :type Range: int
        :param Protocol: 
        :type Protocol: PortProtocol
        :param Description: 
        :type Description: str
        :param Open: 
        :type Open: bool
        :returns: ActionResult
        """
        return self.api_call("ADSModule/ModifyCustomFirewallRule", {
            'instanceId': instanceId,
            'PortNumber': PortNumber,
            'Range': Range,
            'Protocol': Protocol,
            'Description': Description,
            'Open': Open
        })

    def MoveInstanceDatastore(self, instanceId: 'str', datastoreId: 'int') -> RunningTask:
        """
        Name Description Optional
        :param instanceId: 
        :type instanceId: str
        :param datastoreId: 
        :type datastoreId: int
        :returns: RunningTask
        """
        return self.api_call("ADSModule/MoveInstanceDatastore", {
            'instanceId': instanceId,
            'datastoreId': datastoreId
        })

    def ReactivateInstance(self, instanceId: 'str') -> RunningTask:
        """
        Name Description Optional
        :param instanceId: 
        :type instanceId: str
        :returns: RunningTask
        """
        return self.api_call("ADSModule/ReactivateInstance", {
            'instanceId': instanceId
        })

    def ReactivateLocalInstances(self, ) -> RunningTask:
        """
        Name Description Optional

        :returns: RunningTask
        """
        return self.api_call("ADSModule/ReactivateLocalInstances", {})

    def RefreshAppCache(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("ADSModule/RefreshAppCache", {})

    def RefreshGroup(self, GroupId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param GroupId: 
        :type GroupId: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/RefreshGroup", {
            'GroupId': GroupId
        })

    def RefreshInstanceConfig(self, InstanceId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/RefreshInstanceConfig", {
            'InstanceId': InstanceId
        })

    def RefreshRemoteConfigStores(self, force: 'bool') -> None:
        """
        Name Description Optional
        :param force: 
        :type force: bool
        :returns: None
        """
        return self.api_call("ADSModule/RefreshRemoteConfigStores", {
            'force': force
        })

    def RegisterTarget(self, controllerUrl: 'str', myUrl: 'str', username: 'str', password: 'str', twoFactorToken: 'str', friendlyName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param controllerUrl: 
        :type controllerUrl: str
        :param myUrl: 
        :type myUrl: str
        :param username: 
        :type username: str
        :param password: 
        :type password: str
        :param twoFactorToken: 
        :type twoFactorToken: str
        :param friendlyName: 
        :type friendlyName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/RegisterTarget", {
            'controllerUrl': controllerUrl,
            'myUrl': myUrl,
            'username': username,
            'password': password,
            'twoFactorToken': twoFactorToken,
            'friendlyName': friendlyName
        })

    def RepairDatastore(self, id: 'int') -> RunningTask:
        """
        Name Description Optional
        :param id: 
        :type id: int
        :returns: RunningTask
        """
        return self.api_call("ADSModule/RepairDatastore", {
            'id': id
        })

    def RequestDatastoreSizeCalculation(self, datastoreId: 'int') -> RunningTask:
        """
        Name Description Optional
        :param datastoreId: 
        :type datastoreId: int
        :returns: RunningTask
        """
        return self.api_call("ADSModule/RequestDatastoreSizeCalculation", {
            'datastoreId': datastoreId
        })

    def RestartInstance(self, InstanceName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/RestartInstance", {
            'InstanceName': InstanceName
        })

    def Servers(self, id: 'str', Data: 'dict[str, Any]', RealIP: 'str') -> dict[str, Any]:
        """
        Name Description Optional
        :param id: 
        :type id: str
        :param Data: 
        :type Data: dict[str, Any]
        :param RealIP: 
        :type RealIP: str
        :returns: dict[str, Any]
        """
        return self.api_call("ADSModule/Servers", {
            'id': id,
            'Data': Data,
            'RealIP': RealIP
        })

    def SetInstanceConfig(self, InstanceName: 'str', SettingNode: 'str', Value: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :param SettingNode: 
        :type SettingNode: str
        :param Value: 
        :type Value: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/SetInstanceConfig", {
            'InstanceName': InstanceName,
            'SettingNode': SettingNode,
            'Value': Value
        })

    def SetInstanceNetworkInfo(self, InstanceId: 'str', PortMappings: 'dict[str, int]') -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :param PortMappings: 
        :type PortMappings: dict[str, int]
        :returns: ActionResult
        """
        return self.api_call("ADSModule/SetInstanceNetworkInfo", {
            'InstanceId': InstanceId,
            'PortMappings': PortMappings
        })

    def SetInstanceSuspended(self, InstanceName: 'str', Suspended: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :param Suspended: 
        :type Suspended: bool
        :returns: ActionResult
        """
        return self.api_call("ADSModule/SetInstanceSuspended", {
            'InstanceName': InstanceName,
            'Suspended': Suspended
        })

    def StartAllInstances(self, TargetADSInstance: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: 
        :type TargetADSInstance: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/StartAllInstances", {
            'TargetADSInstance': TargetADSInstance
        })

    def StartInstance(self, InstanceName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/StartInstance", {
            'InstanceName': InstanceName
        })

    def StopAllInstances(self, TargetADSInstance: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TargetADSInstance: 
        :type TargetADSInstance: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/StopAllInstances", {
            'TargetADSInstance': TargetADSInstance
        })

    def StopInstance(self, InstanceName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/StopInstance", {
            'InstanceName': InstanceName
        })

    def TestADSLoginDetails(self, url: 'str', username: 'str', password: 'str', twoFactorToken: 'str') -> ActionResult:
        """
        Name Description Optional
        :param url: 
        :type url: str
        :param username: 
        :type username: str
        :param password: 
        :type password: str
        :param twoFactorToken: 
        :type twoFactorToken: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/TestADSLoginDetails", {
            'url': url,
            'username': username,
            'password': password,
            'twoFactorToken': twoFactorToken
        })

    def UpdateDatastore(self, updatedDatastore: 'InstanceDatastore') -> ActionResult:
        """
        Name Description Optional
        :param updatedDatastore: 
        :type updatedDatastore: InstanceDatastore
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpdateDatastore", {
            'updatedDatastore': updatedDatastore
        })

    def UpdateDeploymentTemplate(self, templateToUpdate: 'DeploymentTemplate') -> ActionResult:
        """
        Name Description Optional
        :param templateToUpdate: 
        :type templateToUpdate: DeploymentTemplate
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpdateDeploymentTemplate", {
            'templateToUpdate': templateToUpdate
        })

    def UpdateInstanceInfo(self, InstanceId: 'str', FriendlyName: 'str', Description: 'str', StartOnBoot: 'bool', Suspended: 'bool', ExcludeFromFirewall: 'bool', RunInContainer: 'bool', ContainerMemory: 'int', MemoryPolicy: 'ContainerMemoryPolicy', ContainerMaxCPU: 'float', ContainerImage: 'str', ContainerSwap: 'int', WelcomeMessage: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :param FriendlyName: 
        :type FriendlyName: str
        :param Description: 
        :type Description: str
        :param StartOnBoot: 
        :type StartOnBoot: bool
        :param Suspended: 
        :type Suspended: bool
        :param ExcludeFromFirewall: 
        :type ExcludeFromFirewall: bool
        :param RunInContainer: 
        :type RunInContainer: bool
        :param ContainerMemory: 
        :type ContainerMemory: int
        :param MemoryPolicy: 
        :type MemoryPolicy: ContainerMemoryPolicy
        :param ContainerMaxCPU: 
        :type ContainerMaxCPU: float
        :param ContainerImage: 
        :type ContainerImage: str
        :param ContainerSwap: 
        :type ContainerSwap: int
        :param WelcomeMessage: 
        :type WelcomeMessage: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpdateInstanceInfo", {
            'InstanceId': InstanceId,
            'FriendlyName': FriendlyName,
            'Description': Description,
            'StartOnBoot': StartOnBoot,
            'Suspended': Suspended,
            'ExcludeFromFirewall': ExcludeFromFirewall,
            'RunInContainer': RunInContainer,
            'ContainerMemory': ContainerMemory,
            'MemoryPolicy': MemoryPolicy,
            'ContainerMaxCPU': ContainerMaxCPU,
            'ContainerImage': ContainerImage,
            'ContainerSwap': ContainerSwap,
            'WelcomeMessage': WelcomeMessage
        })

    def UpdateTarget(self, TargetID: 'str') -> None:
        """
        Name Description Optional
        :param TargetID: 
        :type TargetID: str
        :returns: None
        """
        return self.api_call("ADSModule/UpdateTarget", {
            'TargetID': TargetID
        })

    def UpdateTargetInfo(self, Id: 'str', FriendlyName: 'str', Url: 'str', Description: 'str', Tags: 'list[str]') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :param FriendlyName: 
        :type FriendlyName: str
        :param Url: 
        :type Url: str
        :param Description: 
        :type Description: str
        :param Tags: 
        :type Tags: list[str]
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpdateTargetInfo", {
            'Id': Id,
            'FriendlyName': FriendlyName,
            'Url': Url,
            'Description': Description,
            'Tags': Tags
        })

    def UpgradeAllInstances(self, RestartRunning: 'bool', TargetADSInstance: 'str') -> ActionResult:
        """
        Name Description Optional
        :param RestartRunning: 
        :type RestartRunning: bool
        :param TargetADSInstance: 
        :type TargetADSInstance: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpgradeAllInstances", {
            'RestartRunning': RestartRunning,
            'TargetADSInstance': TargetADSInstance
        })

    def UpgradeInstance(self, InstanceName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceName: 
        :type InstanceName: str
        :returns: ActionResult
        """
        return self.api_call("ADSModule/UpgradeInstance", {
            'InstanceName': InstanceName
        })

class AnalyticsPlugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def GetAnalyticsSummary(self, PeriodDays: 'int', StartDate: 'str | None', Filters: 'dict[str, str]') -> Any:
        """
        Name Description Optional
        :param PeriodDays: 
        :type PeriodDays: int
        :param StartDate: 
        :type StartDate: str | None
        :param Filters: 
        :type Filters: dict[str, str]
        :returns: Any
        """
        return self.api_call("AnalyticsPlugin/GetAnalyticsSummary", {
            'PeriodDays': PeriodDays,
            'StartDate': StartDate,
            'Filters': Filters
        })

class Core(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def AcknowledgeAMPUpdate(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/AcknowledgeAMPUpdate", {})

    def ActivateAMPLicence(self, LicenceKey: 'str', QueryOnly: 'bool') -> ActionResult[LicenceInfo]:
        """
        Name Description Optional
        :param LicenceKey: 
        :type LicenceKey: str
        :param QueryOnly: 
        :type QueryOnly: bool
        :returns: ActionResult[LicenceInfo]
        """
        return self.api_call("Core/ActivateAMPLicence", {
            'LicenceKey': LicenceKey,
            'QueryOnly': QueryOnly
        })

    def AddEventTrigger(self, triggerId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param triggerId: 
        :type triggerId: str
        :returns: ActionResult
        """
        return self.api_call("Core/AddEventTrigger", {
            'triggerId': triggerId
        })

    def AddIntervalTrigger(self, months: 'list[int]', days: 'list[int]', hours: 'list[int]', minutes: 'list[int]', daysOfMonth: 'list[int]', description: 'str') -> ActionResult:
        """
        Name Description Optional
        :param months: 
        :type months: list[int]
        :param days: 
        :type days: list[int]
        :param hours: 
        :type hours: list[int]
        :param minutes: 
        :type minutes: list[int]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]
        :param description: 
        :type description: str
        :returns: ActionResult
        """
        return self.api_call("Core/AddIntervalTrigger", {
            'months': months,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'daysOfMonth': daysOfMonth,
            'description': description
        })

    def AddTask(self, TriggerID: 'str', MethodID: 'str', ParameterMapping: 'dict[str, str]') -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: 
        :type TriggerID: str
        :param MethodID: 
        :type MethodID: str
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]
        :returns: ActionResult
        """
        return self.api_call("Core/AddTask", {
            'TriggerID': TriggerID,
            'MethodID': MethodID,
            'ParameterMapping': ParameterMapping
        })

    def AsyncTest(self, ) -> str:
        """DEV: Async test method
        Name Description Optional

        :returns: str
        """
        return self.api_call("Core/AsyncTest", {})

    def CancelTask(self, TaskId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TaskId: 
        :type TaskId: str
        :returns: ActionResult
        """
        return self.api_call("Core/CancelTask", {
            'TaskId': TaskId
        })

    def ChangeTaskOrder(self, TriggerID: 'str', TaskID: 'str', NewOrder: 'int') -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: 
        :type TriggerID: str
        :param TaskID: 
        :type TaskID: str
        :param NewOrder: 
        :type NewOrder: int
        :returns: ActionResult
        """
        return self.api_call("Core/ChangeTaskOrder", {
            'TriggerID': TriggerID,
            'TaskID': TaskID,
            'NewOrder': NewOrder
        })

    def ChangeUserPassword(self, Username: 'str', OldPassword: 'str', NewPassword: 'str', TwoFactorPIN: 'str') -> ActionResult:
        """For a user to change their own password, requires knowing the old password
        Name Description Optional
        :param Username: 
        :type Username: str
        :param OldPassword: 
        :type OldPassword: str
        :param NewPassword: 
        :type NewPassword: str
        :param TwoFactorPIN: 
        :type TwoFactorPIN: str
        :returns: ActionResult
        """
        return self.api_call("Core/ChangeUserPassword", {
            'Username': Username,
            'OldPassword': OldPassword,
            'NewPassword': NewPassword,
            'TwoFactorPIN': TwoFactorPIN
        })

    def ConfirmTwoFactorSetup(self, Username: 'str', TwoFactorCode: 'str') -> ActionResult:
        """Completes two-factor setup by supplying a valid two factor code based on the secret provided by EnableTwoFactor
        Name Description Optional
        :param Username: 
        :type Username: str
        :param TwoFactorCode: 
        :type TwoFactorCode: str
        :returns: ActionResult
        """
        return self.api_call("Core/ConfirmTwoFactorSetup", {
            'Username': Username,
            'TwoFactorCode': TwoFactorCode
        })

    def CreateRole(self, Name: 'str', AsCommonRole: 'bool') -> ActionResult[str]:
        """
        Name Description Optional
        :param Name: 
        :type Name: str
        :param AsCommonRole: 
        :type AsCommonRole: bool
        :returns: ActionResult[str]
        """
        return self.api_call("Core/CreateRole", {
            'Name': Name,
            'AsCommonRole': AsCommonRole
        })

    def CreateTestTask(self, ) -> None:
        """DEV: Creates a non-ending task with 50% progress for testing purposes
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/CreateTestTask", {})

    def CreateUser(self, Username: 'str') -> ActionResult[str]:
        """
        Name Description Optional
        :param Username: 
        :type Username: str
        :returns: ActionResult[str]
        """
        return self.api_call("Core/CreateUser", {
            'Username': Username
        })

    def CurrentSessionHasPermission(self, PermissionNode: 'str') -> bool:
        """
        Name Description Optional
        :param PermissionNode: 
        :type PermissionNode: str
        :returns: bool
        """
        return self.api_call("Core/CurrentSessionHasPermission", {
            'PermissionNode': PermissionNode
        })

    def DeleteInstanceUsers(self, InstanceId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param InstanceId: 
        :type InstanceId: str
        :returns: ActionResult
        """
        return self.api_call("Core/DeleteInstanceUsers", {
            'InstanceId': InstanceId
        })

    def DeleteRole(self, RoleId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param RoleId: 
        :type RoleId: str
        :returns: ActionResult
        """
        return self.api_call("Core/DeleteRole", {
            'RoleId': RoleId
        })

    def DeleteTask(self, TriggerID: 'str', TaskID: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: 
        :type TriggerID: str
        :param TaskID: 
        :type TaskID: str
        :returns: ActionResult
        """
        return self.api_call("Core/DeleteTask", {
            'TriggerID': TriggerID,
            'TaskID': TaskID
        })

    def DeleteTrigger(self, TriggerID: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: 
        :type TriggerID: str
        :returns: ActionResult
        """
        return self.api_call("Core/DeleteTrigger", {
            'TriggerID': TriggerID
        })

    def DeleteUser(self, Username: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Username: 
        :type Username: str
        :returns: ActionResult
        """
        return self.api_call("Core/DeleteUser", {
            'Username': Username
        })

    def DisableTwoFactor(self, Password: 'str', TwoFactorCode: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Password: 
        :type Password: str
        :param TwoFactorCode: 
        :type TwoFactorCode: str
        :returns: ActionResult
        """
        return self.api_call("Core/DisableTwoFactor", {
            'Password': Password,
            'TwoFactorCode': TwoFactorCode
        })

    def DismissAllTasks(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("Core/DismissAllTasks", {})

    def DismissTask(self, TaskId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param TaskId: 
        :type TaskId: str
        :returns: ActionResult
        """
        return self.api_call("Core/DismissTask", {
            'TaskId': TaskId
        })

    def EditIntervalTrigger(self, Id: 'str', months: 'list[int]', days: 'list[int]', hours: 'list[int]', minutes: 'list[int]', daysOfMonth: 'list[int]', description: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :param months: 
        :type months: list[int]
        :param days: 
        :type days: list[int]
        :param hours: 
        :type hours: list[int]
        :param minutes: 
        :type minutes: list[int]
        :param daysOfMonth: 
        :type daysOfMonth: list[int]
        :param description: 
        :type description: str
        :returns: ActionResult
        """
        return self.api_call("Core/EditIntervalTrigger", {
            'Id': Id,
            'months': months,
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'daysOfMonth': daysOfMonth,
            'description': description
        })

    def EditTask(self, TriggerID: 'str', TaskID: 'str', ParameterMapping: 'dict[str, str]') -> ActionResult:
        """
        Name Description Optional
        :param TriggerID: 
        :type TriggerID: str
        :param TaskID: 
        :type TaskID: str
        :param ParameterMapping: 
        :type ParameterMapping: dict[str, str]
        :returns: ActionResult
        """
        return self.api_call("Core/EditTask", {
            'TriggerID': TriggerID,
            'TaskID': TaskID,
            'ParameterMapping': ParameterMapping
        })

    def EnableTwoFactor(self, Username: 'str', Password: 'str') -> ActionResult[TwoFactorSetupInfo]:
        """Sets up two-factor authentication for the given user. ConfirmTwoFactorSetup must be invoked to complete setup.
        Name Description Optional
        :param Username: 
        :type Username: str
        :param Password: 
        :type Password: str
        :returns: ActionResult[TwoFactorSetupInfo]
        """
        return self.api_call("Core/EnableTwoFactor", {
            'Username': Username,
            'Password': Password
        })

    def EndUserSession(self, Id: 'str') -> None:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :returns: None
        """
        return self.api_call("Core/EndUserSession", {
            'Id': Id
        })

    def GetAMPRolePermissions(self, RoleId: 'str') -> list[str]:
        """
        Name Description Optional
        :param RoleId: 
        :type RoleId: str
        :returns: list[str]
        """
        return self.api_call("Core/GetAMPRolePermissions", {
            'RoleId': RoleId
        })

    def GetAMPUserInfo(self, Username: 'str') -> UserInfo:
        """
        Name Description Optional
        :param Username: 
        :type Username: str
        :returns: UserInfo
        """
        return self.api_call("Core/GetAMPUserInfo", {
            'Username': Username
        })

    def GetAMPUsersSummary(self, ) -> list[UserInfoSummary]:
        """
        Name Description Optional

        :returns: list[UserInfoSummary]
        """
        return self.api_call("Core/GetAMPUsersSummary", {})

    def GetAPISpec(self, ) -> dict[str, dict[str, MethodInfoSummary]]:
        """
        Name Description Optional

        :returns: dict[str, dict[str, MethodInfoSummary]]
        """
        return self.api_call("Core/GetAPISpec", {})

    def GetActiveAMPSessions(self, ) -> list[WebSessionSummary]:
        """
        Name Description Optional

        :returns: list[WebSessionSummary]
        """
        return self.api_call("Core/GetActiveAMPSessions", {})

    def GetAllAMPUserInfo(self, ) -> list[UserInfo]:
        """
        Name Description Optional

        :returns: list[UserInfo]
        """
        return self.api_call("Core/GetAllAMPUserInfo", {})

    def GetAuditLogEntries(self, Before: 'str | None', Count: 'int') -> list[IAuditLogEntry]:
        """
        Name Description Optional
        :param Before: 
        :type Before: str | None
        :param Count: 
        :type Count: int
        :returns: list[IAuditLogEntry]
        """
        return self.api_call("Core/GetAuditLogEntries", {
            'Before': Before,
            'Count': Count
        })

    def GetAuthenticationRequirements(self, username: 'str') -> list[AuthenticationRequirement]:
        """
        Name Description Optional
        :param username: 
        :type username: str
        :returns: list[AuthenticationRequirement]
        """
        return self.api_call("Core/GetAuthenticationRequirements", {
            'username': username
        })

    def GetConfig(self, node: 'str') -> SettingSpec:
        """
        Name Description Optional
        :param node: 
        :type node: str
        :returns: SettingSpec
        """
        return self.api_call("Core/GetConfig", {
            'node': node
        })

    def GetConfigs(self, nodes: 'list[str]') -> list[SettingSpec]:
        """
        Name Description Optional
        :param nodes: 
        :type nodes: list[str]
        :returns: list[SettingSpec]
        """
        return self.api_call("Core/GetConfigs", {
            'nodes': nodes
        })

    def GetDiagnosticsInfo(self, ) -> dict[str, str]:
        """
        Name Description Optional

        :returns: dict[str, str]
        """
        return self.api_call("Core/GetDiagnosticsInfo", {})

    def GetModuleInfo(self, ) -> ModuleInfo:
        """
        Name Description Optional

        :returns: ModuleInfo
        """
        return self.api_call("Core/GetModuleInfo", {})

    def GetNewGuid(self, ) -> str:
        """
        Name Description Optional

        :returns: str
        """
        return self.api_call("Core/GetNewGuid", {})

    def GetPermissionsSpec(self, ) -> list[IPermissionsTreeNode]:
        """
        Name Description Optional

        :returns: list[IPermissionsTreeNode]
        """
        return self.api_call("Core/GetPermissionsSpec", {})

    def GetPortSummaries(self, ) -> list[ListeningPortSummary]:
        """
        Name Description Optional

        :returns: list[ListeningPortSummary]
        """
        return self.api_call("Core/GetPortSummaries", {})

    def GetProvisionSpec(self, ) -> list[SettingSpec]:
        """
        Name Description Optional

        :returns: list[SettingSpec]
        """
        return self.api_call("Core/GetProvisionSpec", {})

    def GetRemoteLoginToken(self, Description: 'str', IsTemporary: 'bool') -> str:
        """
        Name Description Optional
        :param Description: 
        :type Description: str
        :param IsTemporary: 
        :type IsTemporary: bool
        :returns: str
        """
        return self.api_call("Core/GetRemoteLoginToken", {
            'Description': Description,
            'IsTemporary': IsTemporary
        })

    def GetRole(self, RoleId: 'str') -> AuthRoleSummary:
        """
        Name Description Optional
        :param RoleId: 
        :type RoleId: str
        :returns: AuthRoleSummary
        """
        return self.api_call("Core/GetRole", {
            'RoleId': RoleId
        })

    def GetRoleData(self, ) -> list[AuthRoleSummary]:
        """
        Name Description Optional

        :returns: list[AuthRoleSummary]
        """
        return self.api_call("Core/GetRoleData", {})

    def GetRoleIds(self, ) -> dict[str, str]:
        """
        Name Description Optional

        :returns: dict[str, str]
        """
        return self.api_call("Core/GetRoleIds", {})

    def GetScheduleData(self, ) -> ScheduleInfo:
        """
        Name Description Optional

        :returns: ScheduleInfo
        """
        return self.api_call("Core/GetScheduleData", {})

    def GetSettingValues(self, SettingNode: 'str', WithRefresh: 'bool') -> dict[str, str]:
        """
        Name Description Optional
        :param SettingNode: 
        :type SettingNode: str
        :param WithRefresh: 
        :type WithRefresh: bool
        :returns: dict[str, str]
        """
        return self.api_call("Core/GetSettingValues", {
            'SettingNode': SettingNode,
            'WithRefresh': WithRefresh
        })

    def GetSettingsSpec(self, ) -> dict[str, SettingSpec]:
        """
        Name Description Optional

        :returns: dict[str, SettingSpec]
        """
        return self.api_call("Core/GetSettingsSpec", {})

    def GetStatus(self, ) -> StatusResponse:
        """
        Name Description Optional

        :returns: StatusResponse
        """
        return self.api_call("Core/GetStatus", {})

    def GetTasks(self, ) -> list[RunningTask]:
        """
        Name Description Optional

        :returns: list[RunningTask]
        """
        return self.api_call("Core/GetTasks", {})

    def GetTimeIntervalTrigger(self, Id: 'str') -> TimeIntervalTrigger:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :returns: TimeIntervalTrigger
        """
        return self.api_call("Core/GetTimeIntervalTrigger", {
            'Id': Id
        })

    def GetUpdateInfo(self, ) -> UpdateInfo:
        """
        Name Description Optional

        :returns: UpdateInfo
        """
        return self.api_call("Core/GetUpdateInfo", {})

    def GetUpdates(self, ) -> UpdateResponse:
        """Gets changes to the server status, in addition to any notifications or console output that have occured since the last time GetUpdates() was called by the current session.
        Name Description Optional

        :returns: UpdateResponse
        """
        return self.api_call("Core/GetUpdates", {})

    def GetUserActionsSpec(self, ) -> Any:
        """
        Name Description Optional

        :returns: Any
        """
        return self.api_call("Core/GetUserActionsSpec", {})

    def GetUserInfo(self, UID: 'str') -> SimpleUser:
        """Provides information about a given in-application user (as opposed to AMP system users)
        Name Description Optional
        :param UID: 
        :type UID: str
        :returns: SimpleUser
        """
        return self.api_call("Core/GetUserInfo", {
            'UID': UID
        })

    def GetUserList(self, ) -> dict[str, str]:
        """Returns a list of in-application users
        Name Description Optional

        :returns: dict[str, str]
        """
        return self.api_call("Core/GetUserList", {})

    def GetWebauthnChallenge(self, ) -> ActionResult[str]:
        """
        Name Description Optional

        :returns: ActionResult[str]
        """
        return self.api_call("Core/GetWebauthnChallenge", {})

    def GetWebauthnCredentialIDs(self, username: 'str') -> WebauthnLoginInfo:
        """
        Name Description Optional
        :param username: 
        :type username: str
        :returns: WebauthnLoginInfo
        """
        return self.api_call("Core/GetWebauthnCredentialIDs", {
            'username': username
        })

    def GetWebauthnCredentialSummaries(self, ) -> list[WebauthnCredentialSummary]:
        """
        Name Description Optional

        :returns: list[WebauthnCredentialSummary]
        """
        return self.api_call("Core/GetWebauthnCredentialSummaries", {})

    def GetWebserverMetrics(self, ) -> Any:
        """
        Name Description Optional

        :returns: Any
        """
        return self.api_call("Core/GetWebserverMetrics", {})

    def Kill(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/Kill", {})

    def Login(self, username: 'str', password: 'str', token: 'str', rememberMe: 'bool') -> LoginResponse:
        """
        Name Description Optional
        :param username: 
        :type username: str
        :param password: 
        :type password: str
        :param token: 
        :type token: str
        :param rememberMe: 
        :type rememberMe: bool
        :returns: LoginResponse
        """
        return self.api_call("Core/Login", {
            'username': username,
            'password': password,
            'token': token,
            'rememberMe': rememberMe
        })

    def Logout(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/Logout", {})

    def RefreshSettingValueList(self, Node: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Node: 
        :type Node: str
        :returns: ActionResult
        """
        return self.api_call("Core/RefreshSettingValueList", {
            'Node': Node
        })

    def RefreshSettingsSourceCache(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/RefreshSettingsSourceCache", {})

    def RenameRole(self, RoleId: 'str', NewName: 'str') -> ActionResult:
        """
        Name Description Optional
        :param RoleId: 
        :type RoleId: str
        :param NewName: 
        :type NewName: str
        :returns: ActionResult
        """
        return self.api_call("Core/RenameRole", {
            'RoleId': RoleId,
            'NewName': NewName
        })

    def ResetUserPassword(self, Username: 'str', NewPassword: 'str') -> ActionResult:
        """For administrative users to alter the password of another user
        Name Description Optional
        :param Username: 
        :type Username: str
        :param NewPassword: 
        :type NewPassword: str
        :returns: ActionResult
        """
        return self.api_call("Core/ResetUserPassword", {
            'Username': Username,
            'NewPassword': NewPassword
        })

    def Restart(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("Core/Restart", {})

    def RestartAMP(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/RestartAMP", {})

    def Resume(self, ) -> None:
        """Allows the service to be re-started after previously being suspended.
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/Resume", {})

    def RevokeWebauthnCredential(self, ID: 'int') -> ActionResult:
        """
        Name Description Optional
        :param ID: 
        :type ID: int
        :returns: ActionResult
        """
        return self.api_call("Core/RevokeWebauthnCredential", {
            'ID': ID
        })

    def RunEventTriggerImmediately(self, triggerId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param triggerId: 
        :type triggerId: str
        :returns: ActionResult
        """
        return self.api_call("Core/RunEventTriggerImmediately", {
            'triggerId': triggerId
        })

    def RunSecurityCheck(self, ) -> list[SecurityCheckResult]:
        """
        Name Description Optional

        :returns: list[SecurityCheckResult]
        """
        return self.api_call("Core/RunSecurityCheck", {})

    def SendConsoleMessage(self, message: 'str') -> None:
        """
        Name Description Optional
        :param message: 
        :type message: str
        :returns: None
        """
        return self.api_call("Core/SendConsoleMessage", {
            'message': message
        })

    def SetAMPRolePermission(self, RoleId: 'str', PermissionNode: 'str', Enabled: 'bool | None') -> ActionResult:
        """
        Name Description Optional
        :param RoleId: 
        :type RoleId: str
        :param PermissionNode: 
        :type PermissionNode: str
        :param Enabled: 
        :type Enabled: bool | None
        :returns: ActionResult
        """
        return self.api_call("Core/SetAMPRolePermission", {
            'RoleId': RoleId,
            'PermissionNode': PermissionNode,
            'Enabled': Enabled
        })

    def SetAMPUserRoleMembership(self, UserId: 'str', RoleId: 'str', IsMember: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param UserId: 
        :type UserId: str
        :param RoleId: 
        :type RoleId: str
        :param IsMember: 
        :type IsMember: bool
        :returns: ActionResult
        """
        return self.api_call("Core/SetAMPUserRoleMembership", {
            'UserId': UserId,
            'RoleId': RoleId,
            'IsMember': IsMember
        })

    def SetConfig(self, node: 'str', value: 'str') -> ActionResult:
        """
        Name Description Optional
        :param node: 
        :type node: str
        :param value: 
        :type value: str
        :returns: ActionResult
        """
        return self.api_call("Core/SetConfig", {
            'node': node,
            'value': value
        })

    def SetConfigs(self, data: 'dict[str, str]') -> bool:
        """
        Name Description Optional
        :param data: 
        :type data: dict[str, str]
        :returns: bool
        """
        return self.api_call("Core/SetConfigs", {
            'data': data
        })

    def SetTriggerEnabled(self, Id: 'str', Enabled: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param Id: 
        :type Id: str
        :param Enabled: 
        :type Enabled: bool
        :returns: ActionResult
        """
        return self.api_call("Core/SetTriggerEnabled", {
            'Id': Id,
            'Enabled': Enabled
        })

    def Sleep(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("Core/Sleep", {})

    def Start(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("Core/Start", {})

    def Stop(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/Stop", {})

    def Suspend(self, ) -> None:
        """Prevents the current instance from being started, and stops it if it's currently running.
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/Suspend", {})

    def UpdateAMPInstance(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/UpdateAMPInstance", {})

    def UpdateAccountInfo(self, EmailAddress: 'str', TwoFactorPIN: 'str') -> ActionResult:
        """
        Name Description Optional
        :param EmailAddress: 
        :type EmailAddress: str
        :param TwoFactorPIN: 
        :type TwoFactorPIN: str
        :returns: ActionResult
        """
        return self.api_call("Core/UpdateAccountInfo", {
            'EmailAddress': EmailAddress,
            'TwoFactorPIN': TwoFactorPIN
        })

    def UpdateApplication(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("Core/UpdateApplication", {})

    def UpdateUserInfo(self, Username: 'str', Disabled: 'bool', PasswordExpires: 'bool', CannotChangePassword: 'bool', MustChangePassword: 'bool', EmailAddress: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Username: 
        :type Username: str
        :param Disabled: 
        :type Disabled: bool
        :param PasswordExpires: 
        :type PasswordExpires: bool
        :param CannotChangePassword: 
        :type CannotChangePassword: bool
        :param MustChangePassword: 
        :type MustChangePassword: bool
        :param EmailAddress: 
        :type EmailAddress: str
        :returns: ActionResult
        """
        return self.api_call("Core/UpdateUserInfo", {
            'Username': Username,
            'Disabled': Disabled,
            'PasswordExpires': PasswordExpires,
            'CannotChangePassword': CannotChangePassword,
            'MustChangePassword': MustChangePassword,
            'EmailAddress': EmailAddress
        })

    def UpgradeAMP(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("Core/UpgradeAMP", {})

    def WebauthnRegister(self, attestationObject: 'str', clientDataJSON: 'str', description: 'str') -> ActionResult:
        """
        Name Description Optional
        :param attestationObject: 
        :type attestationObject: str
        :param clientDataJSON: 
        :type clientDataJSON: str
        :param description: 
        :type description: str
        :returns: ActionResult
        """
        return self.api_call("Core/WebauthnRegister", {
            'attestationObject': attestationObject,
            'clientDataJSON': clientDataJSON,
            'description': description
        })

class EmailSenderPlugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def TestSMTPSettings(self, ) -> ActionResult:
        """
        Name Description Optional

        :returns: ActionResult
        """
        return self.api_call("EmailSenderPlugin/TestSMTPSettings", {})

class FileManagerPlugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def AppendFileChunk(self, Filename: 'str', Data: 'str', Delete: 'bool') -> None:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :param Data: 
        :type Data: str
        :param Delete: 
        :type Delete: bool
        :returns: None
        """
        return self.api_call("FileManagerPlugin/AppendFileChunk", {
            'Filename': Filename,
            'Data': Data,
            'Delete': Delete
        })

    def CalculateFileMD5Sum(self, FilePath: 'str') -> ActionResult[str]:
        """
        Name Description Optional
        :param FilePath: 
        :type FilePath: str
        :returns: ActionResult[str]
        """
        return self.api_call("FileManagerPlugin/CalculateFileMD5Sum", {
            'FilePath': FilePath
        })

    def ChangeExclusion(self, ModifyPath: 'str', AsDirectory: 'bool', Exclude: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param ModifyPath: 
        :type ModifyPath: str
        :param AsDirectory: 
        :type AsDirectory: bool
        :param Exclude: 
        :type Exclude: bool
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/ChangeExclusion", {
            'ModifyPath': ModifyPath,
            'AsDirectory': AsDirectory,
            'Exclude': Exclude
        })

    def CopyFile(self, Origin: 'str', TargetDirectory: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Origin: 
        :type Origin: str
        :param TargetDirectory: 
        :type TargetDirectory: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/CopyFile", {
            'Origin': Origin,
            'TargetDirectory': TargetDirectory
        })

    def CreateArchive(self, PathToArchive: 'str') -> ActionResult:
        """
        Name Description Optional
        :param PathToArchive: 
        :type PathToArchive: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/CreateArchive", {
            'PathToArchive': PathToArchive
        })

    def CreateDirectory(self, NewPath: 'str') -> ActionResult:
        """Creates a new directory. The parent directory must already exist.
        Name Description Optional
        :param NewPath: 
        :type NewPath: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/CreateDirectory", {
            'NewPath': NewPath
        })

    def DownloadFileFromURL(self, Source: 'str', TargetDirectory: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Source: 
        :type Source: str
        :param TargetDirectory: 
        :type TargetDirectory: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/DownloadFileFromURL", {
            'Source': Source,
            'TargetDirectory': TargetDirectory
        })

    def Dummy(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("FileManagerPlugin/Dummy", {})

    def EmptyTrash(self, TrashDirectoryName: 'str') -> ActionResult:
        """Empties a trash bin
        Name Description Optional
        :param TrashDirectoryName: 
        :type TrashDirectoryName: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/EmptyTrash", {
            'TrashDirectoryName': TrashDirectoryName
        })

    def ExtractArchive(self, ArchivePath: 'str', DestinationPath: 'str') -> ActionResult:
        """
        Name Description Optional
        :param ArchivePath: 
        :type ArchivePath: str
        :param DestinationPath: 
        :type DestinationPath: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/ExtractArchive", {
            'ArchivePath': ArchivePath,
            'DestinationPath': DestinationPath
        })

    def GetDirectoryListing(self, Dir: 'str') -> list[DirectoryListing]:
        """
        Name Description Optional
        :param Dir: 
        :type Dir: str
        :returns: list[DirectoryListing]
        """
        return self.api_call("FileManagerPlugin/GetDirectoryListing", {
            'Dir': Dir
        })

    def GetFileChunk(self, Filename: 'str', Position: 'int', Length: 'int') -> FileChunkData:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :param Position: 
        :type Position: int
        :param Length: 
        :type Length: int
        :returns: FileChunkData
        """
        return self.api_call("FileManagerPlugin/GetFileChunk", {
            'Filename': Filename,
            'Position': Position,
            'Length': Length
        })

    def ReadFileChunk(self, Filename: 'str', Offset: 'int', ChunkSize: 'int') -> ActionResult[str]:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :param Offset: 
        :type Offset: int
        :param ChunkSize: 
        :type ChunkSize: int
        :returns: ActionResult[str]
        """
        return self.api_call("FileManagerPlugin/ReadFileChunk", {
            'Filename': Filename,
            'Offset': Offset,
            'ChunkSize': ChunkSize
        })

    def ReleaseFileUploadLock(self, Filename: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/ReleaseFileUploadLock", {
            'Filename': Filename
        })

    def RenameDirectory(self, oldDirectory: 'str', NewDirectoryName: 'str') -> ActionResult:
        """Renames a directory
        Name Description Optional
        :param oldDirectory: The full path to the old directory
        :type oldDirectory: str
        :param NewDirectoryName: The name component of the new directory (not the full path)
        :type NewDirectoryName: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/RenameDirectory", {
            'oldDirectory': oldDirectory,
            'NewDirectoryName': NewDirectoryName
        })

    def RenameFile(self, Filename: 'str', NewFilename: 'str') -> ActionResult:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :param NewFilename: 
        :type NewFilename: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/RenameFile", {
            'Filename': Filename,
            'NewFilename': NewFilename
        })

    def TrashDirectory(self, DirectoryName: 'str') -> ActionResult:
        """Moves a directory to trash, files must be trashed before they can be deleted.
        Name Description Optional
        :param DirectoryName: 
        :type DirectoryName: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/TrashDirectory", {
            'DirectoryName': DirectoryName
        })

    def TrashFile(self, Filename: 'str') -> ActionResult:
        """Moves a file to trash, files must be trashed before they can be deleted.
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/TrashFile", {
            'Filename': Filename
        })

    def WriteFileChunk(self, Filename: 'str', Data: 'str', Offset: 'int', FinalChunk: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param Filename: 
        :type Filename: str
        :param Data: 
        :type Data: str
        :param Offset: 
        :type Offset: int
        :param FinalChunk: 
        :type FinalChunk: bool
        :returns: ActionResult
        """
        return self.api_call("FileManagerPlugin/WriteFileChunk", {
            'Filename': Filename,
            'Data': Data,
            'Offset': Offset,
            'FinalChunk': FinalChunk
        })

class GenericModule(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def ImportConfig(self, filename: 'str') -> dict[str, str]:
        """
        Name Description Optional
        :param filename: 
        :type filename: str
        :returns: dict[str, str]
        """
        return self.api_call("GenericModule/ImportConfig", {
            'filename': filename
        })

    def ReloadGenericConfig(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("GenericModule/ReloadGenericConfig", {})

class LocalFileBackupPlugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def DeleteFromS3(self, BackupId: 'str') -> ActionResult:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :returns: ActionResult
        """
        return self.api_call("LocalFileBackupPlugin/DeleteFromS3", {
            'BackupId': BackupId
        })

    def DeleteLocalBackup(self, BackupId: 'str') -> None:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :returns: None
        """
        return self.api_call("LocalFileBackupPlugin/DeleteLocalBackup", {
            'BackupId': BackupId
        })

    def DownloadFromS3(self, BackupId: 'str') -> RunningTask:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :returns: RunningTask
        """
        return self.api_call("LocalFileBackupPlugin/DownloadFromS3", {
            'BackupId': BackupId
        })

    def GetBackups(self, ) -> list[BackupManifest]:
        """
        Name Description Optional

        :returns: list[BackupManifest]
        """
        return self.api_call("LocalFileBackupPlugin/GetBackups", {})

    def RefreshBackupList(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("LocalFileBackupPlugin/RefreshBackupList", {})

    def RestoreBackup(self, BackupId: 'str', DeleteExistingData: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :param DeleteExistingData: 
        :type DeleteExistingData: bool
        :returns: ActionResult
        """
        return self.api_call("LocalFileBackupPlugin/RestoreBackup", {
            'BackupId': BackupId,
            'DeleteExistingData': DeleteExistingData
        })

    def SetBackupSticky(self, BackupId: 'str', Sticky: 'bool') -> None:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :param Sticky: 
        :type Sticky: bool
        :returns: None
        """
        return self.api_call("LocalFileBackupPlugin/SetBackupSticky", {
            'BackupId': BackupId,
            'Sticky': Sticky
        })

    def TakeBackup(self, Title: 'str', Description: 'str', Sticky: 'bool', WasCreatedAutomatically: 'bool') -> ActionResult:
        """
        Name Description Optional
        :param Title: 
        :type Title: str
        :param Description: 
        :type Description: str
        :param Sticky: 
        :type Sticky: bool
        :param WasCreatedAutomatically: 
        :type WasCreatedAutomatically: bool
        :returns: ActionResult
        """
        return self.api_call("LocalFileBackupPlugin/TakeBackup", {
            'Title': Title,
            'Description': Description,
            'Sticky': Sticky,
            'WasCreatedAutomatically': WasCreatedAutomatically
        })

    def UploadToS3(self, BackupId: 'str') -> RunningTask:
        """
        Name Description Optional
        :param BackupId: 
        :type BackupId: str
        :returns: RunningTask
        """
        return self.api_call("LocalFileBackupPlugin/UploadToS3", {
            'BackupId': BackupId
        })

class MinecraftModule(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def AcceptEULA(self, ) -> bool:
        """
        Name Description Optional

        :returns: bool
        """
        return self.api_call("MinecraftModule/AcceptEULA", {})

    def AddOPEntry(self, UserOrUUID: 'str') -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: 
        :type UserOrUUID: str
        :returns: ActionResult
        """
        return self.api_call("MinecraftModule/AddOPEntry", {
            'UserOrUUID': UserOrUUID
        })

    def AddToWhitelist(self, UserOrUUID: 'str') -> ActionResult:
        """
        Name Description Optional
        :param UserOrUUID: 
        :type UserOrUUID: str
        :returns: ActionResult
        """
        return self.api_call("MinecraftModule/AddToWhitelist", {
            'UserOrUUID': UserOrUUID
        })

    def BanUserByID(self, ID: 'str') -> None:
        """
        Name Description Optional
        :param ID: 
        :type ID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/BanUserByID", {
            'ID': ID
        })

    def BukGetCategories(self, ) -> dict[str, Any]:
        """
        Name Description Optional

        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetCategories", {})

    def BukGetInstallUpdatePlugin(self, pluginId: 'int') -> RunningTask:
        """
        Name Description Optional
        :param pluginId: 
        :type pluginId: int
        :returns: RunningTask
        """
        return self.api_call("MinecraftModule/BukGetInstallUpdatePlugin", {
            'pluginId': pluginId
        })

    def BukGetInstalledPlugins(self, ) -> dict[str, Any]:
        """
        Name Description Optional

        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetInstalledPlugins", {})

    def BukGetPluginInfo(self, PluginId: 'int') -> dict[str, Any]:
        """
        Name Description Optional
        :param PluginId: 
        :type PluginId: int
        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetPluginInfo", {
            'PluginId': PluginId
        })

    def BukGetPluginsForCategory(self, CategoryId: 'str', PageNumber: 'int', PageSize: 'int') -> dict[str, Any]:
        """
        Name Description Optional
        :param CategoryId: 
        :type CategoryId: str
        :param PageNumber: 
        :type PageNumber: int
        :param PageSize: 
        :type PageSize: int
        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetPluginsForCategory", {
            'CategoryId': CategoryId,
            'PageNumber': PageNumber,
            'PageSize': PageSize
        })

    def BukGetPopularPlugins(self, ) -> dict[str, Any]:
        """
        Name Description Optional

        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetPopularPlugins", {})

    def BukGetRemovePlugin(self, PluginId: 'int') -> None:
        """
        Name Description Optional
        :param PluginId: 
        :type PluginId: int
        :returns: None
        """
        return self.api_call("MinecraftModule/BukGetRemovePlugin", {
            'PluginId': PluginId
        })

    def BukGetSearch(self, Query: 'str', PageNumber: 'int', PageSize: 'int') -> dict[str, Any]:
        """
        Name Description Optional
        :param Query: 
        :type Query: str
        :param PageNumber: 
        :type PageNumber: int
        :param PageSize: 
        :type PageSize: int
        :returns: dict[str, Any]
        """
        return self.api_call("MinecraftModule/BukGetSearch", {
            'Query': Query,
            'PageNumber': PageNumber,
            'PageSize': PageSize
        })

    def ClearInventoryByID(self, ID: 'str') -> None:
        """
        Name Description Optional
        :param ID: 
        :type ID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/ClearInventoryByID", {
            'ID': ID
        })

    def GetFailureReason(self, ) -> str:
        """
        Name Description Optional

        :returns: str
        """
        return self.api_call("MinecraftModule/GetFailureReason", {})

    def GetHeadByUUID(self, id: 'str') -> str:
        """Get a skin as a base64 string
        Name Description Optional
        :param id: 
        :type id: str
        :returns: str
        """
        return self.api_call("MinecraftModule/GetHeadByUUID", {
            'id': id
        })

    def GetOPWhitelist(self, ) -> UserAccessData:
        """
        Name Description Optional

        :returns: UserAccessData
        """
        return self.api_call("MinecraftModule/GetOPWhitelist", {})

    def GetWhitelist(self, ) -> list[WhitelistEntry]:
        """
        Name Description Optional

        :returns: list[WhitelistEntry]
        """
        return self.api_call("MinecraftModule/GetWhitelist", {})

    def KickUserByID(self, ID: 'str') -> None:
        """
        Name Description Optional
        :param ID: 
        :type ID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/KickUserByID", {
            'ID': ID
        })

    def KillByID(self, ID: 'str') -> None:
        """
        Name Description Optional
        :param ID: 
        :type ID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/KillByID", {
            'ID': ID
        })

    def LoadOPList(self, ) -> list[OPEntry]:
        """
        Name Description Optional

        :returns: list[OPEntry]
        """
        return self.api_call("MinecraftModule/LoadOPList", {})

    def RemoveOPEntry(self, UserOrUUID: 'str') -> None:
        """
        Name Description Optional
        :param UserOrUUID: 
        :type UserOrUUID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/RemoveOPEntry", {
            'UserOrUUID': UserOrUUID
        })

    def RemoveWhitelistEntry(self, UserOrUUID: 'str') -> None:
        """
        Name Description Optional
        :param UserOrUUID: 
        :type UserOrUUID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/RemoveWhitelistEntry", {
            'UserOrUUID': UserOrUUID
        })

    def SmiteByID(self, ID: 'str') -> None:
        """Strike a player with lightning
        Name Description Optional
        :param ID: 
        :type ID: str
        :returns: None
        """
        return self.api_call("MinecraftModule/SmiteByID", {
            'ID': ID
        })

class RCONPlugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def Dummy(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("RCONPlugin/Dummy", {})

class steamcmdplugin(AMPAPI):
    def __init__(self, authprovider: AuthProvider) -> None:
        super().__init__(authprovider)

    def CancelSteamGuard(self, ) -> None:
        """
        Name Description Optional

        :returns: None
        """
        return self.api_call("steamcmdplugin/CancelSteamGuard", {})

    def SteamGuardCode(self, code: 'str') -> None:
        """
        Name Description Optional
        :param code: 
        :type code: str
        :returns: None
        """
        return self.api_call("steamcmdplugin/SteamGuardCode", {
            'code': code
        })

    def SteamUsernamePassword(self, username: 'str', password: 'str') -> None:
        """
        Name Description Optional
        :param username: 
        :type username: str
        :param password: 
        :type password: str
        :returns: None
        """
        return self.api_call("steamcmdplugin/SteamUsernamePassword", {
            'username': username,
            'password': password
        })

