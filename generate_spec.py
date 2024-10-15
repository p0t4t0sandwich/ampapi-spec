#!/bin/python3

from __future__ import annotations

import os
import sys
import json
from typing import Any

from ampapi import AMPAPI

class GenerateSpec:
    NewAPISpec: dict[str, dict[str, Any]] = {}
    TypedAPISpec: dict[str, dict[str, Any]] = {}
    ModuleInheritance: dict[str, list[str]] = {}
    apis: list[AMPAPI] = []

    def _load_apis(self, args: list[str]) -> None:
        catalogued_modules: list[str] = []

        for i in range(int(len(args)/3)):
            api = AMPAPI(args[i*3])
            loginResult: dict[str, Any] = api.Login(args[i*3+1], args[i*3+2])
            if "success" in loginResult.keys() and loginResult["success"]:
                self.apis.append(api)

            targets = api.ADSModule_GetInstances()
            for target in targets:
                for instance in target["AvailableInstances"]:
                    instance_id: str = instance["InstanceID"]
                    instance_name: str = instance["InstanceName"]
                    instance_module: str = instance["Module"]

                    if not instance_module in catalogued_modules:
                        print(f"Generating API Spec for {instance_module}, {instance_name}")
                        instance_api: AMPAPI = api.InstanceLogin(instance_id)

                        if instance_api != None:
                            self.log_module_plugins(instance_module, instance_api.Core_GetAPISpec())
                            catalogued_modules.append(instance_module)
                            self.apis.append(instance_api)

    def _load_typed_api_spec(self) -> None:
        with open("./TypedAPISpec.json") as f:
            json_str: str = f.read()
            self.TypedAPISpec = json.loads(json_str)
            f.close()

    def _load_api_spec(self) -> None:
        for api in self.apis:
            api_spec: dict[str, dict[str, Any]] = api.Core_GetAPISpec()
            for module_name, module in api_spec.items():
                if module_name not in self.NewAPISpec:
                    self.NewAPISpec[module_name] = {}
                for method_name, method in module.items():
                    if method_name not in self.NewAPISpec[module_name]:
                        self.NewAPISpec[module_name][method_name] = method

    def __init__(self, args: list) -> None:
        self._load_apis(args)
        self._load_typed_api_spec()
        self._load_api_spec()

    def check_if_new_version(self):
        # Read the current version from the file
        version_file = open("AMPVersion.txt", "r+")
        current_version = version_file.read()

        # Get the latest version from the API (Assume the first API source is the latest version)
        latest_version = self.apis[0].Core_GetUpdateInfo()["Version"]

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

#             return True
#         else:
#             return False
        return True

    def log_module_plugins(self, module: str, api_spec: dict[str, dict[str, Any]]) -> None:
        submodules: list[str] = []
        for submodule in api_spec.keys():
            submodules.append(submodule)
        submodules.sort()
        print(f"API Submodules for {module}: {submodules}")
        self.ModuleInheritance[module] = submodules

    def update_typed_spec(self) -> None:
        """
        Merge the new API spec with the typed API spec
        Remove any methods that are not in the new API spec
        Add any new methods to the typed API spec
        Remove any parameters that are not in the new API spec
        Add any new parameters to the typed API spec
        """
        for module in self.NewAPISpec:
            if module not in self.TypedAPISpec:
                self.TypedAPISpec[module] = self.NewAPISpec[module]
            else:
                for method in self.NewAPISpec[module]:
                    if method not in self.TypedAPISpec[module]:
                        self.TypedAPISpec[module][method] = self.NewAPISpec[module][method]
                    else:
                        for parameter in self.NewAPISpec[module][method]["Parameters"]:
                            found = False
                            for typed_param in self.TypedAPISpec[module][method]["Parameters"]:
                                if parameter["Name"] == typed_param["Name"]:
                                    found = True
                                    break
                            if not found:
                                self.TypedAPISpec[module][method]["Parameters"].append(parameter)

        for module in self.TypedAPISpec:
            for method in list(self.TypedAPISpec[module]):
                if method not in self.NewAPISpec[module]:
                    self.TypedAPISpec[module].pop(method)
                else:
                    for parameter in self.TypedAPISpec[module][method]["Parameters"]:
                        found = False
                        for new_param in self.NewAPISpec[module][method]["Parameters"]:
                            if parameter["Name"] == new_param["Name"]:
                                found = True
                                break
                        if not found:
                            self.TypedAPISpec[module][method]["Parameters"].remove(parameter)

    def write_spec(self) -> None:
        with open("APISpec.json", "w") as outfile:
            self.NewAPISpec = dict(sorted(self.NewAPISpec.items()))
            for module in self.NewAPISpec:
                self.NewAPISpec[module] = dict(sorted(self.NewAPISpec[module].items()))
                for method in self.NewAPISpec[module]:
                    sorted_params = []
                    for param in self.NewAPISpec[module][method]["Parameters"]:
                        sorted_params.append(dict(sorted(param.items())))
                    self.NewAPISpec[module][method]["Parameters"] = sorted_params

            json.dump(self.NewAPISpec, outfile, indent=2)
            outfile.write("\n")
            outfile.close()

        with open("TypedAPISpec.json", "w") as outfile:
            # Alphabetize the dictionary
            self.TypedAPISpec = dict(sorted(self.TypedAPISpec.items()))
            for module in self.TypedAPISpec:
                self.TypedAPISpec[module] = dict(sorted(self.TypedAPISpec[module].items()))
                for method in self.TypedAPISpec[module]:
                    sorted_params = []
                    for param in self.TypedAPISpec[module][method]["Parameters"]:
                        sorted_params.append(dict(sorted(param.items())))
                    self.TypedAPISpec[module][method]["Parameters"] = sorted_params

            json.dump(self.TypedAPISpec, outfile, indent=2)
            outfile.write("\n")
            outfile.close()

        # Write the ModuleInheritance.json file
        with open("ModuleInheritance.json", "w") as outfile:
            self.ModuleInheritance = dict(sorted(self.ModuleInheritance.items()))
            for module in self.ModuleInheritance:
                self.ModuleInheritance[module].sort()

            outfile.write(json.dumps(self.ModuleInheritance, indent=2))
            outfile.write("\n")
            outfile.close()

        # Write the friendly spec to a file
        with open("FriendlySpec.txt", "w") as outfile:
            for module in self.TypedAPISpec:
                for method in self.TypedAPISpec[module]:
                    parameters = ""
                    for parameter in self.TypedAPISpec[module][method]["Parameters"]:
                        parameters += f"{parameter['Name']}: {parameter['TypeName']}, "
                    parameters = parameters[:-2]

                    return_type = self.TypedAPISpec[module][method]["ReturnTypeName"]
                    outfile.write(f"{module}.{method}({parameters}) -> {return_type}\n")
            outfile.close()

if __name__ == "__main__":
    # Get the arguments
    args = sys.argv[1:]

    # Create the GenerateSpec object
    gs = GenerateSpec(args)

    # Check if there is a new version of AMP
    if gs.check_if_new_version():
        gs.update_typed_spec()
        gs.write_spec()
    else:
        print("No new version of AMP")
