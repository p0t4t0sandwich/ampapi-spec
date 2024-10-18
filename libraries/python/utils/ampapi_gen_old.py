#!/bin/python3
from __future__ import annotations

import requests
import json

import sys


type_dict = {
    # Generic types
    "ActionResult": "ActionResult",
    "ActionResult<Guid>": "ActionResult[UUID]",
    "ActionResult<LicenceInfo>": "ActionResult[LicenceInfo]",
    "ActionResult<String>": "ActionResult[str]",
    "ActionResult<TwoFactorSetupInfo>": "ActionResult[Any]",
    "RunningTask": "RunningTask",
    "IEnumerable<RunningTask>": "list[RunningTask]",

    # Primitive types
    "Boolean": "bool",
    "Guid": "UUID",
    "Int32": "int",
    "Int32[]": "list[int]",
    "Int64": "int",
    "JObject": "dict",
    "Object": "Any",
    "String": "str",
    "String[]": "list[str]",
    "Uri": "URL",
    "Void": "Void",

    # Nested types
    "Dictionary<String, Dictionary<String, MethodInfoSummary>>": "dict[str, dict[str, Any]]",
    "Dictionary<String, Int32>": "dict[str, int]",
    "Dictionary<String, SettingSpec>": "dict[str, SettingSpec]",
    "Dictionary<String, String>": "dict[str, str]",
    "IDictionary<Guid, String>": "dict[UUID, str]",
    "IDictionary<String, String>": "dict[str, str]",
    "IEnumerable<ApplicationSpec>": "list[Any]",
    "IEnumerable<AuthenticationRequirement>": "list[Any]",
    "IEnumerable<AuthRoleSummary>": "list[Any]",
    "IEnumerable<BackupManifest>": "list[Any]",
    "IEnumerable<DeploymentTemplate>": "list[Any]",
    "IEnumerable<EndpointInfo>": "list[EndpointInfo]",
    "IEnumerable<FileDirectory>": "list[FileDirectory]",
    "IEnumerable<IADSInstance>": "list[IADSInstance]",
    "IEnumerable<IAuditLogEntry>": "list[Any]",
    "IEnumerable<InstanceDatastore>": "list[InstanceDatastore]",
    "IEnumerable<InstanceStatus>": "list[InstanceStatus]",
    "IEnumerable<JObject>": "list[dict]",
    "IEnumerable<ListeningPortSummary>": "list[Any]",
    "IEnumerable<PortUsage>": "list[Any]",
    "IEnumerable<ProvisionSettingInfo>": "list[Any]",
    "IEnumerable<String>": "list[str]",
    "IEnumerable<UserInfo>": "list[UserInfo]",
    "IEnumerable<UserInfoSummary>": "list[Any]",
    "IEnumerable<WebauthnCredentialSummary>": "list[Any]",
    "IEnumerable<WebSessionSummary>": "list[Any]",
    "IList<IPermissionsTreeNode>": "list[Any]",
    "List<JObject>": "list[dict]",
    "List<String>": "list[str]",
    "Nullable<Boolean>": "bool",
    "Nullable<DateTime>": "Any",

    # Object types
    "AuthRoleSummary": "Any",
    "ContainerMemoryPolicy": "Any",
    "DeploymentTemplate": "Any",
    "FileChunkData": "Any",
    "IADSInstance": "IADSInstance",
    "Instance": "Instance",
    "InstanceDatastore": "InstanceDatastore",
    "IPAddress": "str",
    "LocalAMPInstance": "Any",
    "LoginResult": "LoginResult",
    "ModuleInfo": "ModuleInfo",
    "PortProtocol": "Any",
    "PostCreateAppActions": "Any",
    "RemoteTargetInfo": "RemoteTargetInfo",
    "ScheduleInfo": "Any",
    "SimpleUser": "Any",
    "Single": "Any",
    "Status": "Status",
    "TimeIntervalTrigger": "Any",
    "UpdateInfo": "UpdateInfo",
    "Updates": "Updates",
    "UserInfo": "UserInfo",
    "WebauthnLoginInfo": "Any",
}

custom_types = {
    # API.ADSModule.GetInstance
    # "ADSModule.GetInstance": "Result[Instance]",
}

def generate_apimodule_method(module: str, method: str, method_spec: dict):
    # Read the template file
    api_module_method_template = ""
    with open("templates/api_module_method.txt", "r") as tf:
        api_module_method_template = tf.read()
        tf.close()

    # Get the method description
    description = ""
    if "Description" in method_spec.keys():
        description = "\n     * " + method_spec["Description"]

    # Get the method parameters
    parameters_docs = ""
    methodParams = method_spec["Parameters"]
    if len(methodParams) > 0:
        parameters_docs += "\n"
    for i in range(len(methodParams)):
        api_module_method_parameter_doc_template = ""
        with open("templates/api_module_method_parameter_doc.txt", "r") as tf:
            api_module_method_parameter_doc_template = tf.read()
            tf.close()

        name = methodParams[i]["Name"]
        type_name = methodParams[i]["TypeName"]

        # Print out the type if it hasn't been added to the type_dict
        if not type_name in type_dict.keys(): print(type_name)

        description = methodParams[i]["Description"]
        optional = methodParams[i]["Optional"]
        if optional == "true": type_name += ", " + optional

        template = api_module_method_parameter_doc_template\
            .replace("%METHOD_PARAMETER_NAME%", name)\
            .replace("%METHOD_PARAMETER_TYPE%", type_dict[type_name])\
            .replace("%METHOD_PARAMETER_DESCRIPTION%", description)\
            .replace("%METHOD_PARAMETER_OPTIONAL%", str(optional))

        parameters_docs += template
    parameters_docs = parameters_docs[:-1]

    # Get the method return type
    return_type = method_spec["ReturnTypeName"]

    # Print out the type if it hasn't been added to the type_dict
    if not return_type in type_dict.keys(): print(return_type)
    return_type = type_dict[return_type]

    # Get the method parameters
    parameters = ""
    for i in range(len(methodParams)):
        name = methodParams[i]["Name"]
        type_name = methodParams[i]["TypeName"]

        # Print out the type if it hasn't been added to the type_dict
        if not type_name in type_dict.keys(): print(type_name)
        parameters += f"{name}: {type_dict[type_name]}, "

    parameters = parameters[:-2]

    # Get the parameters for the data map
    map_string = ""
    if len(methodParams) > 0:
        map_string += "\n"
    for i in range(len(methodParams)):
        api_module_method_parameter_map_template = ""
        with open("templates/api_module_method_parameter_map.txt", "r") as tf:
            api_module_method_parameter_map_template = tf.read()
            tf.close()

        name = methodParams[i]["Name"]
        map_string += api_module_method_parameter_map_template.replace("%METHOD_PARAMETER_NAME%", name)
    map_string = map_string[:-1]

    # Custom mapping for list types
    return_type_serializer = return_type + "(**response)"
    if return_type.startswith("list["):
        inner = return_type[5:-1]
        if inner.startswith("dict["):
            return_type_serializer = f"[{inner[5:-1]}(**x) for x in response]"
        else:
            return_type_serializer = f"[{inner}(**x) for x in response]"

    elif return_type.startswith("dict["):
        return_type_serializer = f"response"

    # Replace placeholders
    template = api_module_method_template\
        .replace("%METHOD_DESCRIPTION%", description)\
        .replace("%METHOD_PARAMETER_DOC%", parameters_docs)\
        .replace("%MODULE_NAME%", module)\
        .replace("%METHOD_NAME%", method)\
        .replace("%METHOD_PARAMETERS%", parameters)\
        .replace("%METHOD_RETURN_TYPE%", return_type)\
        .replace("%METHOD_RETURN_SERIALIZER%", return_type_serializer)\
        .replace("%METHOD_PARAMETER_MAP%", map_string)

    # End result will return a string
    # TODO: Simple replace is here to fix a bug with the Void return type
    return template.replace("return Void(**response)", "if response == None:\n            response = {}\n        return Void(**response)")

def generate_apimodule(module: str, methods: dict):
    # Read the template file
    api_module_template = ""
    with open("templates/api_module.txt", "r") as tf:
        api_module_template = tf.read()
        tf.close()

    # Create a new file called f{module}.java
    f = open(f"../ampapi/plugins/{module}.py","w+")
    f.write(api_module_template.replace("%MODULE_NAME%", module))

    for method in methods.keys():
        f.write(generate_apimodule_method(module, method, methods[method]))

    f.close()

def generate_spec(spec: dict):
    for module in spec.keys():
        if module == "CommonCorePlugin": continue
        generate_apimodule(module, spec[module])

def load_custom_types(spec: dict):
    for type_index in custom_types.keys():
        type_module = type_index.split(".")[0]
        type_method = type_index.split(".")[1]

        # Update the return type
        spec[type_module][type_method]["ReturnTypeName"] = custom_types[type_index]

if __name__ == "__main__":
    branch = "main"
    if len(sys.argv) > 1:
        branch = sys.argv[1]

    # Load remote file
    res = requests.get(f"https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-spec/{branch}/OldAPISpec.json")
    spec = json.loads(res.content)

    # Load custom types
    load_custom_types(spec)

    generate_spec(spec)
