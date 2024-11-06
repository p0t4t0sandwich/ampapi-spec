#!/bin/python3
from json import dump, dumps, loads
from os import getenv
from sys import argv
from typing import Any

from ampapi_simple import AMPAPI

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
                            module_info = instance_api.Core_GetModuleInfo()
                            # if instance_module == "GenericModule":
                                # instance_module = module_info["AppName"]
                            loaded_plugins = module_info["LoadedPlugins"]

                            self.log_module_plugins(instance_module, instance_api.Core_GetAPISpec(), loaded_plugins)
                            catalogued_modules.append(instance_module)
                            self.apis.append(instance_api)

    def _load_typed_api_spec(self) -> None:
        with open("./TypedAPISpec.json") as f:
            json_str: str = f.read()
            self.TypedAPISpec = loads(json_str)
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

<<<<<<< HEAD
    def __init__(self, args: list) -> None:
        self._load_apis(args)
        self._load_typed_api_spec()
        self._load_api_spec()
=======
        # Write the ModuleInheritance.json file
        with open("ModuleInheritance.json", "a") as outfile:
            outfile.write(json.dumps(self.ModuleInheritance, indent=2))
            outfile.write("\n")
            outfile.close()

        # Write the friendly spec to a file
        with open("FriendlySpec.txt", "w") as outfile:
            old_api_spec_file = open("OldAPISpec.json", "r")
            old_api_spec = json.load(old_api_spec_file)
            old_api_spec_file.close()

            # Non-destructively add new methods to the old API spec
            for module in self.APISpec:
                if not module in old_api_spec.keys():
                    old_api_spec[module] = {}
                for method in self.APISpec[module]:
                    if not method in old_api_spec[module].keys():
                        old_api_spec[module][method] = self.APISpec[module][method]

                    # Now to update any new or removed Parameters
                    else:
                        for parameter in self.APISpec[module][method]["Parameters"]:
                            if not parameter in old_api_spec[module][method]["Parameters"]:
                                old_api_spec[module][method]["Parameters"].append(parameter)
                        for parameter in old_api_spec[module][method]["Parameters"]:
                            if not parameter in self.APISpec[module][method]["Parameters"]:
                                old_api_spec[module][method]["Parameters"].remove(parameter)

            # Alphabetize the old API spec and all of the methods
            old_api_spec = dict(sorted(old_api_spec.items()))

            # Save the old API spec
            with open("OldAPISpec.json", "w") as old_api_spec_file:
                json.dump(old_api_spec, old_api_spec_file, indent=2)
                old_api_spec_file.write("\n")
                old_api_spec_file.close()

            for module in old_api_spec:
                for method in old_api_spec[module]:
                    outfile.write(self.parse_friendly_method(module, method, old_api_spec[module][method]) + "\n")
            outfile.close()

        # Save any new methods to the OldAPISpec.json file
        with open("OldAPISpec.json", "w") as old_api_spec_file:
            for module in self.APISpec:
                for method in self.APISpec[module]:
                    if not module in old_api_spec.keys():
                        old_api_spec[module] = {}
                    if not method in old_api_spec[module].keys():
                        old_api_spec[module][method] = self.APISpec[module][method]

            # Alphabetize the old API spec and all of the methods
            old_api_spec = dict(sorted(old_api_spec.items()))

            # Save the old API spec
            json.dump(old_api_spec, old_api_spec_file, indent=2)

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
>>>>>>> main

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
            try:
                github_output = getenv('GITHUB_OUTPUT')
                go_file = open(github_output, "a")
                go_file.write("AMP_VERSION=" + latest_version)
                go_file.close()
            except:
                pass

#             return True
#         else:
#             return False
        return True

    def log_module_plugins(self, module: str, api_spec: dict[str, dict[str, Any]], loaded_plugins: list[str]) -> None:
        submodules: list[str] = []
        for submodule in api_spec.keys():
            submodules.append(submodule)
        # for plugin in loaded_plugins:
        #     if plugin not in submodules:
        #         submodules.append(plugin)
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

            dump(self.NewAPISpec, outfile, indent=2)
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

            dump(self.TypedAPISpec, outfile, indent=2)
            outfile.write("\n")
            outfile.close()

        # Write the ModuleInheritance.json file
        with open("ModuleInheritance.json", "w") as outfile:
            self.ModuleInheritance = dict(sorted(self.ModuleInheritance.items()))
            for module in self.ModuleInheritance:
                self.ModuleInheritance[module].sort()

            outfile.write(dumps(self.ModuleInheritance, indent=2))
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
    args = argv[1:]

    # Create the GenerateSpec object
    gs = GenerateSpec(args)

    # Check if there is a new version of AMP
    if gs.check_if_new_version():
        gs.update_typed_spec()
        gs.write_spec()
    else:
        print("No new version of AMP")
