#!/bin/python3

from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any

from ampapi import AMPAPI

# C# to Python
cs_to_py = {
    "Boolean": "bool",
    "DateTime": "str",
    "Dictionary": "dict",
    "Double": "float",
    "Float": "float",
    "Guid": "str",
    "Int32": "int",
    "Int64": "int",
    "JSONRawResponse": "Any",
    "List": "list",
    "Object": "Any",
    "String": "str",
    "Void": "None",
}

@dataclass
class TypeField:
    Name: str
    TypeName: str
    Description: str
    Optional: bool = None
    Value: int = None

@dataclass
class TypeDef:
    Description: str
    Fields: list[TypeField]
    SpecialNote: str = None
    SpecialType: str = None
    SerializesAs: str = None

class UpdateTypes:
    APISpec: dict[str, dict[str, Any]] = {}
    TypeSpec: dict[str, TypeDef] = {}

    def _load_api_spec(self) -> None:
        with open("./TypedAPISpec.json") as f:
            json_str: str = f.read()
            self.APISpec = json.loads(json_str)
            f.close()

    def _load_type_spec(self) -> None:
        with open("./TypeSpec.json") as f:
            json_str: str = f.read()
            for type_name, type_def in json.loads(json_str).items():
                self.TypeSpec[type_name] = TypeDef(
                    Description=type_def["Description"],
                    Fields=[TypeField(**field) for field in type_def["Fields"]],
                    SpecialNote=type_def.get("SpecialNote"),
                    SpecialType=type_def.get("SpecialType"),
                    SerializesAs=type_def.get("SerializesAs")
                )

    def __init__(self) -> None:
        self._load_api_spec()
        self._load_type_spec()

    def convert_type(self, type_name: str) -> str:
        if type_name in cs_to_py:
            return cs_to_py[type_name]
        return type_name

    def lookup_type(self, type_name: str) -> str | dict:
        if type_name in updater.TypeSpec:
            # Check if nested type is an enum
            if updater.TypeSpec[type_name].SpecialType == "Enum":
                return self.convert_type(updater.TypeSpec[type_name].SerializesAs)
            else:
                return_val = {}
                for field in updater.TypeSpec[type_name].Fields:
                    if field.Optional:
                        return_val[field.Name] = str(self.lookup_type(field.TypeName)) + "?"
                    else:
                        return_val[field.Name] = self.lookup_type(field.TypeName)
                return return_val
        elif "Dictionary" in type_name:
            split = type_name.split(", ")
            key_type = split[0].split("<")[1]
            value_type = split[1].split(">")[0]
            return {self.convert_type(key_type): self.lookup_type(value_type)}
        elif "List" in type_name:
            return [self.lookup_type(type_name.split("<")[1].split(">")[0])]
        elif type_name in cs_to_py:
            return self.convert_type(type_name)
        else:
            print(f"Type {type_name} not found in TypeSpec")
            return type_name

    def validate_response_obj(self, response: dict, type_graph: dict | list) -> bool:
        if isinstance(type_graph, list):
            if not all(self.validate_response_obj(item, type_graph[0]) for item in response):
                return False
        if type_graph == "str":
            return isinstance(response, str)
        if type_graph == "Any":
            return True
        for key, value in type_graph.items():
            optional = False
            if type(value) == str and value[-1] == "?":
                optional = True
                value = value[:-1]
            if key not in response:
                if not optional:
                    print(f"Key {key} not found in: [" + ", ".join(response.keys()) + "]")
                continue
            if value == "Any":
                continue
            if value == "{'str': 'str'}":
                if not all(isinstance(key, str) and isinstance(value, str) for key, value in response[key].items()):
                    return False
            elif isinstance(value, dict):
                if not self.validate_response_obj(response[key], value):
                    return False
            elif isinstance(value, list):
                if not all(self.validate_response_obj(item, value[0]) for item in response[key]):
                    return False
            elif not isinstance(response[key], getattr(__builtins__, value)):
                print(f"Key {key} has type {type(response[key])} but expected {value}")
                return False
        return True

    def validate_response(self, module: str, method: str, response: dict) -> bool:
        # Look up return type
        return_type = self.APISpec[module][method]["ReturnTypeName"]

        # Generate return object structure
        type_graph: dict | list = self.lookup_type(return_type)

        # Pretty json
        print(json.dumps(type_graph, indent=2))

        print(f"Return Type: {return_type}")

        valid = True
        if isinstance(type_graph, list):
            if not all(self.validate_response_obj(item, type_graph[0]) for item in response):
                valid = False
        elif return_type == "str" or type_graph == "str":
            if not isinstance(response, str):
                print(f"Expected str but got {response}")
                valid = False
        elif return_type == "bool" or type_graph == "bool":
            if not isinstance(response, bool):
                print(f"Expected bool but got {response}")
                valid = False
        elif type_graph == "None":
            if response != None:
                print(f"Expected None but got {response}")
                valid = False
        elif type_graph == "Any":
            pass
        else:
            for key, value in type_graph.items():
                optional = False
                if type(value) == str and value[-1] == "?":
                    optional = True
                    value = value[:-1]
                if value == "Any":
                    continue
                if key not in response:
                    if not optional:
                        print(f"Field {key} not found in type {return_type}: [" + ", ".join(response.keys()) + "]")
                        valid = False
                    continue
                if isinstance(value, dict):
                    if not self.validate_response_obj(response[key], value):
                        valid = False
                elif isinstance(value, list):
                    if not all(self.validate_response_obj(item, value[0]) for item in response[key]):
                        valid = False
                elif not isinstance(response[key], getattr(__builtins__, value)):
                    print(f"Key {key} has type {type(response[key])} but expected {value}")
                    valid = False

        return valid

if __name__ == "__main__":
    updater = UpdateTypes()

    api = AMPAPI("http://localhost:8080")
    api.Login("api_user", "api_user123!")

    spec = {
        "ADSModule": {
            # "GetApplicationEndpoints": {"instanceId": "5fba16ec-9475-40f9-a517-33b4176c6def"},
            # "GetDatastore": {"id": 1}
            # "GetDatastoreInstances": {"datastoreId": 1}
            # "GetDatastores": {},
            # "GetDeploymentTemplates": {},
            # "GetGroup": {"GroupId": "5fba16ec-9475-40f9-a517-33b4176c6def"}, # Missing fields, needs further testing
            # "GetInstance": {"InstanceId": "5fba16ec-9475-40f9-a517-33b4176c6def"}, # Missing fields, needs further testing
            # "GetInstanceNetworkInfo": {"InstanceName": "ADS01"},
            # "GetInstanceStatuses": {},
            # "GetInstances": {"ForceIncludeSelf": True},
            # "GetLocalInstances": {}, # Missing fields, needs further testing
            # "GetProvisionArguments": {"ModuleName": "Minecraft"}, # Missing fields, needs further testing
            # "GetProvisionFitness": {}
            # "GetSupportedApplications": {} # Missing fields, needs further testing
            # "GetTargetInfo": {}
            # "ManageInstance": {"InstanceId": "5fba16ec-9475-40f9-a517-33b4176c6def"} # ActionResult<String> generic needs some more parsing
            # "RefreshAppCache": {}
            # "GetSupportedAppSummaries": {} # Missing fields, needs further testing
        },
        "AnalyticsPlugin": {
            # "GetAnalyticsSummary": {}
        },
        "Core": {
            # "AcknowledgeAMPUpdate": {}
            # "ActivateAMPLicence": {"LicenceKey": "0000-0000-0000-0000-0000-0000-0000-0000", "QueryOnly": True}, # ActionResult<LicenceInfo> generic needs some more parsing
            # "AsyncTest": {}
            # "CreateRole": {"Name": "TestRole", "AsCommonRole": False}, # ActionResult<Guid> generic needs some more parsing
            # "CreateUser": {"Username": "testuser"} # ActionResult<Guid> generic needs some more parsing
            # "CurrentSessionHasPermission": {"PermissionNode": "thing.test"}
            # "EnableTwoFactor": {"Username": "api_user", "Password": "api_user123!"}, # ActionResult<TwoFactorSetupInfo> generic needs some more parsing
            # "GetAMPRolePermissions": {"RoleId": "57e8d684-88c1-43ab-9cae-48c795a7e012"}
            # "GetAMPUserInfo": {"Username": "api_user"} # Missing fields, needs further testing
            # "GetAMPUsersSummary": {} # Missing fields, needs further testing
            # "GetAPISpec": {} # Cannot handle nested Dictionary<> types
            # "GetActiveAMPSessions": {}
            # "GetAllAMPUserInfo": {} # Missing fields, needs further testing
            # "GetAuditLogEntries": {"Before": "2024-10-12T00:00:00Z", "Count": 10}
            # "GetConfig": {"node": "ADSModule.Network.DefaultAppIPBinding"} # Missing fields, needs further testing
            # "GetConfigs": {"nodes": ["ADSModule.Network.DefaultAppIPBinding"]} # Missing fields, needs further testing
            # "GetDiagnosticsInfo": {} # Apparently Dictionary<String, String> converted to {str: str} is a bit weird
            # "GetModuleInfo": {}
            # "GetNewGuid": {}
            # "GetPermissionsSpec": {} # Recursive type, needs to be reworked. Could maybe just turn the inner value into Object?
            # "GetPortSummaries": {}
            # "GetProvisionSpec": {}
            # "GetRemoteLoginToken": {"Description": "Test", "IsTemporary": True}
            # "GetRole": {"RoleId": "57e8d684-88c1-43ab-9cae-48c795a7e012"}
            # "GetRoleData": {}
            # "GetRoleIds": {} # Needs some work to convert Dictionary<Guid, String> to {str: str}
            # "GetScheduleData": {}
            # "GetSettingValues": {"SettingNode": "ADSModule.Network.DefaultAppIPBinding", "WithRefresh": True} # Apparently Dictionary<String, String> converted to {str: str} is a bit weird
            # "GetSettingsSpec": {} # Dictionary<String, SettingSpec> needs some work
            # "GetStatus": {},
            # "GetTasks": {}
            # "GetTimeIntervalTrigger": {"Id": "bd0ce7c3-ab80-48ac-b134-174b63acb04b"} # Needs some tinkering
            # "GetUpdateInfo": {}
            # "GetUpdates": {}
            # "GetUserActionsSpec": {}
            # "GetUserList": {} # Apparently Dictionary<String, String> converted to {str: str} is a bit weird
            # "GetWebauthnChallenge": {} # ActionResult<String> generic needs some more parsing
            # "GetWebauthnCredentialIDs": {"username": "api_user"}
            # "GetWebauthnCredentialSummaries": {}
            # "Login": {"username": "api_user", "password": "api_user123!", "token": "", "rememberMe": False}
            # "SetConfigs": {"data": {"ADSModule.Network.DefaultAppIPBinding": "0.0.0.0"}}
            # "GetAuthenticationRequirements": {"username": "api_user"}
        },
        "FileManagerPlugin": {
            # "GetDirectoryListing": {"Dir": "./"}
            # "GetFileChunk": {"Filename": "__VDS__ADS01/WebRoot/Scripts/API.js", "Position": 0, "Length": 100}
        },
        "LocalFileBackupPlugin": {
            # "GetBackups": {} # Some serialization issue
        }
    }

    for module, methods in spec.items():
        for method in methods:
            print("----------------------------------------")
            print(f"Method: {module}.{method}")
            response = api.APICall(f"{module}/{method}", methods[method])
            # print(json.dumps(response, indent=2))
            if response != None and not isinstance(response, bool) and "Title" in response and "Message" in response and "StackTrace" in response:
                print(f"Error: {response['Title']}")
                print(f"Message: {response['Message']}")
                print(f"StackTrace: {response['StackTrace']}")
                print("----------------------------------------")
                continue
            valid = updater.validate_response(module, method, response)
            print(f"Response is valid: {valid}")
            print("----------------------------------------")
