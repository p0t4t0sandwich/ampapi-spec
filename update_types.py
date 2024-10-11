#!/bin/python3

from dataclasses import dataclass, field
import json
import requests

class AMPAPI():
    """Class for interacting with the AMP API"""
    def __init__(self, baseUri: str) -> None:
        """Initializes the AMP API class
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :returns: None
        """
        self.baseUri = baseUri
        self.sessionId = ""
        self.dataSource = ""

        if not self.baseUri[-1] == "/":
            self.dataSource = self.baseUri + "/API"
        else:
            self.dataSource = self.baseUri + "API"

    def APICall(self, endpoint: str, data: dict = {}) -> dict:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: dict
        """
        headers = {'Accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)

        data_json = json.dumps(data_added)

        res = requests.post(
            url=f"{self.dataSource}/{endpoint}",
            headers=headers,
            data=data_json
        )
        res_json = json.loads(res.content)

        return res_json
    
    def Login(self, username: str, password: str) -> None:
        """Method to login to the AMP API
        :param username: The username to login with
        :type username: str
        :param password: The password to login with
        :type password: str
        :returns: None
        """
        res = self.APICall("Core/Login", {"username": username, "password": password, "token": "", "rememberMe": False})
        self.sessionId = res["sessionID"]

@dataclass
class APIParameter():
    Name: str
    TypeName: str
    Description: str
    Optional: bool
    ParamEnumValues: dict[str, int] = None

@dataclass
class APIMethod():
    ReturnTypeName: str
    IsComplexType: bool
    Parameters: list[APIParameter] = field(default_factory=list)

@dataclass
class TypeField():
    Name: str
    TypeName: str
    Description: str
    Optional: bool = None
    Value: int = None

@dataclass
class TypeDef():
    Description: str
    Fields: list[TypeField]
    SpecialNote: str = None
    SpecialType: str = None
    SerializesAs: str = None

class UpdateTypes():
    APISpec: dict[str, dict[str, APIMethod]] = {}
    TypeSpec: dict[str, TypeDef] = {}

    def _load_api_spec(self) -> None:
        with open("./TypedAPISpec.json") as f:
            json_str: str = f.read()
            for module_name, module in json.loads(json_str).items():
                if module_name not in self.APISpec:
                    self.APISpec[module_name] = {}
                for method_name, method in module.items():
                    self.APISpec[module_name][method_name] = APIMethod(
                        Parameters=[APIParameter(**param) for param in method["Parameters"]],
                        ReturnTypeName=method["ReturnTypeName"],
                        IsComplexType=method["IsComplexType"]
                    )

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

    def print_api_spec(self) -> None:
        for module_name, methods in self.APISpec.items():
            for method_name, method in methods.items():
                print(f"{module_name}.{method_name}")
                print(f"  ReturnTypeName: {method.ReturnTypeName}")
                print(f"  IsComplexType: {method.IsComplexType}")
                for param in method.Parameters:
                    print(f"  Parameter: {param.Name}")
                    print(f"    TypeName: {param.TypeName}")
                    print(f"    Description: {param.Description}")
                    print(f"    Optional: {param.Optional}")
                    if param.ParamEnumValues:
                        print(f"    EnumValues: {param.ParamEnumValues}")

    def convert_type(self, type_name: str) -> str:
        if type_name in type_converter:
            return type_converter[type_name]
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
                        return_val[field.Name] = self.lookup_type(field.TypeName) + "?"
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
        else:
            return self.convert_type(type_name)

    def validate_response_obj(self, response: dict, type_graph: dict | list) -> bool:
        if isinstance(type_graph, list):
            if not all(self.validate_response_obj(item, type_graph[0]) for item in response):
                return False
        if type_graph == "str":
            return isinstance(response, str)
        for key, value in type_graph.items():
            optional = False
            if key[-1] == "?":
                optional = True
                key = key[:-1]
            if key not in response:
                if optional:
                    print(f"Key {key} not found in: [" + ", ".join(response.keys()) + "]")
                continue
            if isinstance(value, dict):
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
        return_type = self.APISpec[module][method].ReturnTypeName

        # Generate return object structure
        type_graph: dict | list = self.lookup_type(return_type)

        # Pretty json
        # print(json.dumps(type_graph, indent=2))

        print(f"Return Type: {return_type}")

        valid = True
        if isinstance(type_graph, list):
            if not all(self.validate_response_obj(item, type_graph[0]) for item in response):
                valid = False
        else:
            for key, value in type_graph.items():
                if key not in response:
                    if key != "str":
                        print(f"Key {key} not found in response")
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

    type_converter = { # C# to Python
        "Int32": "int",
        "String": "str",
        "Boolean": "bool",
        "DateTime": "str",
        "Guid": "str",
        "List": "list",
        "Dictionary": "dict",
        "Object": "dict",
        "Int64": "int",
        "Double": "float",
        "Float": "float"
    }


    module = "Core"
    method = "GetStatus"

    spec = {
        "ADSModule": {
            "GetApplicationEndpoints": {},
            "GetInstances": {}
        }
        # "Core": [
        #     "GetStatus",
        #     "GetUpdates"
        # ]
    }

    for module, methods in spec.items():
        for method in methods:
            print("----------------------------------------")
            print(f"Method: {module}.{method}")
            response = api.APICall(f"{module}/{method}")
            if "Title" in response and "Message" in response and "StackTrace" in response:
                print(f"Error: {response['Title']}")
                print(f"Message: {response['Message']}")
                print(f"StackTrace: {response['StackTrace']}")
                print("----------------------------------------")
                continue
            valid = updater.validate_response(module, method, response)
            print(f"Response is valid: {valid}")
            print("----------------------------------------")
