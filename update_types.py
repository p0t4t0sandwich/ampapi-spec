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
    _APISpec: dict[str, dict[str, APIMethod]] = {}
    _TypeSpec: dict[str, TypeDef] = {}

    def _load_api_spec(self) -> None:
        with open("./OldAPISpec.json") as f:
            json_str: str = f.read()
            for module_name, module in json.loads(json_str).items():
                if module_name not in self._APISpec:
                    self._APISpec[module_name] = {}
                for method_name, method in module.items():
                    self._APISpec[module_name][method_name] = APIMethod(
                        Parameters=[APIParameter(**param) for param in method["Parameters"]],
                        ReturnTypeName=method["ReturnTypeName"],
                        IsComplexType=method["IsComplexType"]
                    )

    def _load_type_spec(self) -> None:
        with open("./TypeSpec.json") as f:
            json_str: str = f.read()
            for type_name, type_def in json.loads(json_str).items():
                self._TypeSpec[type_name] = TypeDef(
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
        for module_name, methods in self._APISpec.items():
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

if __name__ == "__main__":
    updater = UpdateTypes()
    # api = AMPAPI("http://localhost:8080")
    # api.Login("api_user", "api_user123!")
    # res = api.APICall("Core/GetStatus")
    # print(res)
    