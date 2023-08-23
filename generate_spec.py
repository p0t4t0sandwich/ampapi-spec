#!/bin/python3

from __future__ import annotations
from typing import TypeVar

import os
import sys

import requests
import json

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

    def ADSModule_GetInstances(self):
        """
        :returns: AMP Type: IEnumerable<IADSInstance>
        :rtype: list
        """
        return self.APICall(endpoint="ADSModule/GetInstances")

    def Core_GetAPISpec(self):
        """
        :returns: AMP Type: Dictionary<String, Dictionary<String, MethodInfoSummary>>
        :rtype: dict[str, dict]
        """
        return self.APICall(endpoint="Core/GetAPISpec")

    def Core_GetUpdateInfo(self):
        """
        :returns: AMP Type: UpdateInfo
        """
        return self.APICall(endpoint="Core/GetUpdateInfo")

AMPAPIHandlerType = TypeVar("AMPAPIHandlerType", bound="AMPAPIHandler")

class AMPAPIHandler(AMPAPI):
    """Class to make handling the AMP API easier, without altering the generated code"""
    def __init__(self, baseUri: str, username: str, password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        """Constructor for AMPAPIHandler
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :param username: The username to log in with
        :type username: str
        :param password: The password to log in with
        :type password: str
        :value password: ""
        :param rememberMeToken: The remember me token to log in with
        :type rememberMeToken: str
        :value rememberMeToken: ""
        :param sessionId: The session ID to log in with
        :type sessionId: str
        :value sessionId: ""
        :returns: None
        """
        super().__init__(baseUri=baseUri)
        if self.baseUri[-1] != "/": self.baseUri = self.baseUri + "/"
        self.username = username
        self.password = password
        self.rememberMeToken = rememberMeToken
        self.sessionId = sessionId

    def APICall(self, endpoint: str, data: dict = {}, retry: bool = False) -> dict:
        """Overridden APICall method to automatically relog if the call fails
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :param retry: Wether the call is a retry or not
        :type retry: bool
        :value retry: False
        :returns: dict with the result of the API call
        :rtype: dict
        """
        try:
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
        except Exception as e:
            # If retry is set to true, raise the exception
            if retry:
                raise e

            # Relog and retry the API call
            loginResult = self.APICall("Core/Login", {
                "username": self.username,
                "password": self.password,
                "token": self.rememberMeToken,
                "rememberMe": False
            })
            if "success" in loginResult.keys() and loginResult["success"]:
                self.APICall(endpoint, data, 1)

    def Login(self) -> dict:
        """Method to make the login process easier
        :returns: dict with the login result
        :rtype: dict
        """
        loginResult = self.APICall(endpoint=f"Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": False
        })
        if "success" in loginResult.keys() and loginResult["success"]:
            self.rememberMeToken = loginResult["rememberMeToken"]
            self.sessionId = loginResult["sessionID"]
        return loginResult

    def InstanceLogin(self, instance_id: str) -> AMPAPIHandlerType | None:
        """Method to build another AMPAPIHandler for the specified instance
        :param instance_id: The instance ID to log into
        :type instance_id: str
        :returns: A new AMPAPIHandler for the specified instance
        :rtype: AMPAPIHandler | None
        """
        loginResult = self.APICall(endpoint=f"ADSModule/Servers/{instance_id}/API/Core/Login", data={
            "username": self.username,
            "password": self.password,
            "token": "",
            "rememberMe": True
        })

        if loginResult != None and "success" in loginResult.keys() and loginResult["success"] == True:
            return AMPAPIHandler(
                baseUri=self.baseUri + f"API/ADSModule/Servers/{instance_id}",
                username=self.username,
                password="",
                rememberMeToken=loginResult["rememberMeToken"],
                sessionId=loginResult["sessionID"]
            )
        else:
            return None

class GenerateSpec:
    def __init__(self, args: list) -> None:
        """Initializes the GenerateSpec class"""

        # APISpec
        self.APISpec = {}

        # ModuleInheritance
        self.ModuleInheritance = {}

        # Get the various API sources
        self.api_handlers: list[AMPAPIHandler] = []
        for i in range(int(len(args)/3)):
            self.api_handlers.append(AMPAPIHandler(
                baseUri=args[i*3],
                username=args[i*3+1],
                password=args[i*3+2]
            ))

        # Login to each API source and check their version
        for i in range(len(self.api_handlers)):
            api_handler = self.api_handlers[i]

            loginResult: dict = api_handler.Login()
            if not ("success" in loginResult.keys() and loginResult["success"]):
                self.api_handlers.pop(i)

    def merge_api_spec(self, api_spec: dict) -> None:
        # Add the API spec to the main APISpec, but only add new modules/methods
            for module in api_spec:
                if not module in self.APISpec.keys():
                    self.APISpec[module] = api_spec[module]
                else:
                    for method in api_spec[module]:
                        if not method in self.APISpec[module].keys():
                            self.APISpec[module][method] = api_spec[module][method]

    def log_game_submodules(self, module: str, api_spec: dict) -> None:
        """Method to log the game submodules
        :param module: The module to log
        :type module: str
        :param api_spec: The API spec to log
        :type api_spec: dict
        :returns: None
        """

        # Loop through the API spec and log the game submodules
        submodules: list[str] = []
        for submodule in api_spec.keys():
            submodules.append(submodule)

        print(f"API Submodules for {module}: {submodules}")
        # Add the submodules to the ModuleInheritance
        self.ModuleInheritance[module] = submodules

    def gen_all_api_spec(self) -> None:
        """Method to generate the spec"""

        # Nuke the ModuleInheritance.json file
        with open("ModuleInheritance.json", "w") as outfile:
            outfile.write("")
            outfile.close()

        catalogued_modules: list[str] = []

        # Loop through the API sources
        for api_handler in self.api_handlers:
            api_spec: dict = api_handler.Core_GetAPISpec()["result"]
            self.merge_api_spec(api_spec)

            # Loop through the Instances
            targets = api_handler.ADSModule_GetInstances()["result"]
            for target in targets:
                for instance in target["AvailableInstances"]:
                    instance_id: str = instance["InstanceID"]
                    instance_name: str = instance["InstanceName"]
                    instance_module: str = instance["Module"]

                    # Check if the instance module has already been catalogued
                    if not instance_module in catalogued_modules:
                        print(f"Generating API Spec for {instance_module}, {instance_name}")
                        instance_api: AMPAPIHandler = api_handler.InstanceLogin(instance_id)

                        # Check if the instance API is valid
                        if instance_api != None:
                            instance_api_spec: dict = instance_api.Core_GetAPISpec()["result"]
                            self.log_game_submodules(instance_module, instance_api_spec)
                            catalogued_modules.append(instance_module)
                            self.merge_api_spec(instance_api_spec)

    def write_spec(self) -> None:
        """Method to write the spec to a file"""
        # Alphabetize the APISpec and all of the methods
        self.APISpec = dict(sorted(self.APISpec.items()))
        for module in self.APISpec:
            self.APISpec[module] = dict(sorted(self.APISpec[module].items()))

        with open("APISpec.json", "w") as outfile:
            json.dump(self.APISpec, outfile, indent=2)
            outfile.write("\n")
            outfile.close()

        # Write the ModuleInheritance.json file
        with open("ModuleInheritance.json", "a") as outfile:
            outfile.write(json.dumps(self.ModuleInheritance, indent=2))
            outfile.write("\n")
            outfile.close()

        # Write the friendly spec to a file
        with open("FriendlySpec.txt", "w") as outfile:
            for module in self.APISpec:
                for method in self.APISpec[module]:
                    outfile.write(self.parse_friendly_method(module, method, self.APISpec[module][method]) + "\n")
            outfile.close()

    def parse_friendly_method(self, module: str, method_name: str, method: dict) -> str:
        """Method to parse the method
        :param module: The module the method is in
        :type module: str
        :param method: The method to parse
        :type method: dict
        :returns: The method in a friendly format
        :rtype: str
        """

        # Get the method parameters
        parameters = ""
        if "Parameters" in method.keys():
            for parameter in method["Parameters"]:
                parameters += f"{parameter['Name']}: {parameter['TypeName']}, "
            parameters = parameters[:-2]

        # Get the method return type
        return_type = method["ReturnTypeName"]

        return f"{module}.{method_name}({parameters}) -> {return_type}"

    def check_if_new_version(self):
        # Read the current version from the file
        version_file = open("AMPVersion.txt", "r+")
        current_version = version_file.read()

        # Get the latest version from the API (Assume the first API source is the latest version)
        latest_version = self.api_handlers[0].Core_GetUpdateInfo()["result"]["Version"]

        # Check if the current version is the same as the latest version
        if current_version != latest_version:
            # If the versions are different, update the version file
            version_file.seek(0)
            version_file.write(latest_version)
            version_file.truncate()
            version_file.close()

            # Set the github actions output
            github_output = os.getenv('GITHUB_OUTPUT')
            go_file = open(github_output, "a")
            go_file.write("AMP_VERSION=" + latest_version)
            go_file.close()

            return True
        else:
            return False

if __name__ == "__main__":
    # Get the arguments
    args = sys.argv[1:]

    # Create the GenerateSpec object
    gs = GenerateSpec(args)

    # Check if there is a new version of AMP
    if gs.check_if_new_version():
        # Generate the API Spec
        gs.gen_all_api_spec()

        # Write the API Spec to a file
        gs.write_spec()
    else:
        print("No new version of AMP")
