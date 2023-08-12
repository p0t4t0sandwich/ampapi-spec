#!/bin/python3

from __future__ import annotations

import os
import sys

import requests
import json

class GenerateSpec:
    def __init__(self, AMP_URL: str, AMP_USERNAME: str, AMP_PASSWORD: str) -> None:
        self.dataSource = AMP_URL + "/API"
        self.username = AMP_USERNAME
        self.password = AMP_PASSWORD
        self.sessionId = ""
        self.type_map = {}

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

    def check_if_new_version(self):
        # Read the current version from the file
        version_file = open("AMPVersion.txt", "r+")
        current_version = version_file.read()

        # Get the latest version from the API
        latest_version = self.Core_GetUpdateInfo()["result"]["Version"]

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

    def parse_method(self, module: str, method_name: str, method: dict) -> str:
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

    def generate_spec(self):
        print("Getting API Spec")
        api_spec = self.Core_GetAPISpec()

        print("Write the API Spec to a file")
        with open("APISpec.json", "w") as outfile:
            json.dump(api_spec["result"], outfile, indent=2)
            outfile.write("\n")
            outfile.close()

        # Wipe friendlySpec.txt
        friendly_spec = open("friendlySpec.txt", "w")

        # Loop through the API Spec and write the friendly names to a file
        for module in api_spec["result"]:
            for method in api_spec["result"][module]:
                friendly_spec.write(self.parse_method(module, method, api_spec["result"][module][method]) + "\n")


if __name__ == "__main__":
    # Create a GenerateSpec object
    spec = GenerateSpec(sys.argv[1], sys.argv[2], sys.argv[3])

    # Login to AMP
    spec.Login()

    # Check if there is a new version of AMP
    if spec.check_if_new_version():
        # If there is a new version, generate the new spec
        spec.generate_spec()
    else:
        print("No new version of AMP")