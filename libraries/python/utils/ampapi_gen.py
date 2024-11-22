#!/bin/python3
"""Python CodeGen implementation"""

from json import loads
from typing import Any

import sys
sys.path.append("../../../")
from validate_types import TypeDef, TypeField

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
    "IPAddress": "str",
    "JSONRawResponse": "dict[str, Any]",
    "JObject": "dict[str, Any]",
    "List": "list",
    "Object": "Any",
    "String": "str",
    "TimeSpan": "str",
    "Uri": "str",
    "Void": "None",

    "Generic": "T",
}


class CodeGen:
    """CodeGen Class"""
    APISpec: dict[str, dict[str, Any]] = {}
    TypeSpec: dict[str, TypeDef] = {}
    ModuleInheritance: dict[str, list[str]] = {}

    def _load_api_spec(self) -> None:
        with open("../../../TypedAPISpec.json", encoding="UTF-8") as file:
            json_str: str = file.read()
            self.APISpec = loads(json_str)

    def _load_type_spec(self) -> None:
        with open("../../../TypeSpec.json", encoding="UTF-8") as file:
            json_str: str = file.read()
            for type_name, type_def in loads(json_str).items():
                self.TypeSpec[type_name] = TypeDef(
                    Description=type_def["Description"],
                    Fields=[TypeField(**field) for field in type_def["Fields"]],
                    SpecialNote=type_def.get("SpecialNote"),
                    SpecialType=type_def.get("SpecialType"),
                    SerializesAs=type_def.get("SerializesAs")
                )

    def _load_module_inheritance(self) -> None:
        with open("../../../ModuleInheritance.json", encoding="UTF-8") as file:
            json_str: str = file.read()
            self.ModuleInheritance = loads(json_str)

    def __init__(self) -> None:
        self._load_api_spec()
        self._load_type_spec()
        self._load_module_inheritance()

    def _convert_type(self, type_name: str, optional: bool = False) -> str:
        converted_type = ""
        if type_name.startswith("List<"):
            inner = type_name.replace("List<", "").replace(">", "")
            t = self._convert_type(inner)
            converted_type = f"list[{t}]"
        elif type_name.startswith("Dictionary<"):
            stripped = type_name[11:-1]
            split = stripped.split(", ", 1)
            left = self._convert_type(split[0])
            right = self._convert_type(split[1])
            converted_type = f"dict[{left}, {right}]"
        elif "Nullable<" in type_name:
            t = type_name.replace("Nullable<", "").replace(">", "")
            if t in cs_to_py:
                t = cs_to_py[t]
            converted_type = f"{t} | None"
        elif "ActionResult<" in type_name:
            t = type_name.replace("ActionResult<", "").replace(">", "")
            if t in cs_to_py:
                t = cs_to_py[t]
            converted_type = f"ActionResult[{t}]"
        else:
            if type_name in cs_to_py:
                converted_type = cs_to_py[type_name]
            else:
                converted_type = type_name

        if optional:
            # converted_type += " | None"
            converted_type = f"Optional[{converted_type}]"

        return converted_type

    def generate_types(self) -> None:
        """Generates API Types"""
        text = ""
        with open("./templates/type_base.txt", encoding="UTF-8") as file:
            text = file.read()

        class_text_template = ""
        with open("./templates/type_class.txt", encoding="UTF-8")as file:
            class_text_template = file.read()

        enum_text_template = ""
        with open("./templates/type_enum.txt", encoding="UTF-8") as file:
            enum_text_template = file.read()

        generic_text_template = ""
        with open("./templates/type_generic.txt", encoding="UTF-8") as file:
            generic_text_template = file.read()

        for type_name, type_def in self.TypeSpec.items():
            class_text = class_text_template
            enum_text = enum_text_template
            generic_text = generic_text_template

            fields = ""
            type_def_description = type_def.Description

            if type_def.SpecialType == "Enum":
                for field in type_def.Fields:
                    if field.Name == "None":
                        field.Name = "None_"
                    field_text = f"    {field.Name} = {field.Value}\n"
                    fields += field_text

                    type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"

                enum_text = enum_text.replace("{TypeFields}", fields)
                enum_text = enum_text.replace("{TypeName}", type_name)
                enum_text = enum_text.replace("{TypeDescription}", type_def_description)

                text += enum_text

            elif type_def.SpecialType == "Generic":
                for field in type_def.Fields:
                    field.TypeName = self._convert_type(field.TypeName, field.Optional)
                    field_text = f"    {field.Name}: '{field.TypeName}'"
                    type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"

                    field_text += "\n"
                    fields += field_text

                generic_text = generic_text.replace("{TypeFields}", fields)
                generic_text = generic_text.replace("{TypeName}", type_name)
                generic_text = generic_text.replace("{TypeDescription}", type_def_description)

                text += generic_text

            else:
                for field in type_def.Fields:
                    field.TypeName = self._convert_type(field.TypeName, field.Optional)

                    field_text = f"    {field.Name}: '{field.TypeName}'"
                    type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"
                    field_text += "\n"

                    fields += field_text

                class_text = class_text.replace("{TypeFields}", fields)
                class_text = class_text.replace("{TypeName}", type_name)
                class_text = class_text.replace("{TypeDescription}", type_def_description)

                text += class_text

        with open("../ampapi/types.py", "w", encoding="UTF-8") as file:
            file.write(text)

    def generate_plugins(self) -> None:
        text = ""
        with open("./templates/plugin_base.txt", encoding="UTF-8") as file:
            text = file.read()

        plugin_class_template = ""
        with open("./templates/plugin_class.txt", encoding="UTF-8") as file:
            plugin_class_template = file.read()

        plugin_method_template = ""
        with open("./templates/plugin_method.txt", encoding="UTF-8") as file:
            plugin_method_template = file.read()

        for plugin_name, method_spec in self.APISpec.items():
            if plugin_name == "CommonCorePlugin":
                continue

            plugin_class = plugin_class_template
            plugin_methods = ""

            for method_name, method_def in method_spec.items():
                method_text = plugin_method_template

                parameter_text = ""
                for param in method_def["Parameters"]:
                    param_text = f"{param['Name']}: '{self._convert_type(param['TypeName'])}'"

                    param_text += ", "
                    parameter_text += param_text

                if parameter_text != "":
                    parameter_text = parameter_text[:-2]

                parameter_args = ""
                for param in method_def["Parameters"]:
                    param_text = f"'{param['Name']}': {param['Name']}"

                    param_text += ", "
                    parameter_args += param_text

                if parameter_args != "":
                    parameter_args = "\n            " + parameter_args[:-2]
                    parameter_args = parameter_args.replace(", ", ",\n            ")
                    parameter_args += "\n        "

                parameter_docs = ""
                for param in method_def["Parameters"]:
                    doc = f"        :param {param['Name']}: {param['Description']}\n"
                    doc += f"        :type {param['Name']}: {self._convert_type(param['TypeName'])}\n"
                    parameter_docs += doc

                if parameter_docs != "":
                    parameter_docs = parameter_docs[:-1]
                parameter_docs = parameter_docs + "\n        "

                method_text = method_text.replace("{MethodParameters}", parameter_text)
                method_text = method_text.replace("{MethodParameterArgs}", parameter_args)
                method_text = method_text.replace("{MethodParameterDocs}", parameter_docs)
                method_text = method_text.replace("{MethodName}", method_name)
                if method_def.get("Description") is None:
                    method_def["Description"] = ""
                method_text = method_text.replace("{MethodDescription}", method_def.get("Description", ""))
                method_text = method_text.replace("{ReturnType}", self._convert_type(method_def["ReturnTypeName"]))

                plugin_methods += method_text

            async_plugin_methods = plugin_methods.replace("def ", "async def ").replace("json_to_obj(", "json_to_obj(await ")

            plugin_class = plugin_class.replace("{PluginMethods}", plugin_methods)
            plugin_class = plugin_class.replace("{AsyncPluginMethods}", async_plugin_methods)
            plugin_class = plugin_class.replace("{PluginName}", plugin_name)
            plugin_class = plugin_class[:-1]
            plugin_class = plugin_class.replace("\n\n\n", "\n")

            text += plugin_class

        with open("../ampapi/plugins.py", "w", encoding="UTF-8") as file:
            file.write(text)

    def generate_modules(self) -> None:
        text = ""
        with open("./templates/module_base.txt", encoding="UTF-8") as file:
            text = file.read()

        module_class_template = ""
        with open("./templates/module_class.txt", encoding="UTF-8") as file:
            module_class_template = file.read()

        common_plugins = []
        for plugin_list in self.ModuleInheritance.values():
            for plugin in plugin_list:
                if plugin == "CommonCorePlugin":
                    continue
                for plugin_list2 in self.ModuleInheritance.values():
                    if plugin not in plugin_list2:
                        break
                else:
                    if plugin not in common_plugins:
                        common_plugins.append(plugin)

        for plugin_list in self.ModuleInheritance.values():
            for plugin in common_plugins:
                if plugin in plugin_list:
                    plugin_list.remove(plugin)
            plugin_list.remove("CommonCorePlugin")

        # Generate CommonAPI
        common_loaded_plugins = ""
        common_plugin_init = ""
        common_async_loaded_plugins = ""
        common_async_plugin_init = ""
        for plugin in common_plugins:
            common_loaded_plugins += f"    {plugin} = Final[{plugin}]\n"
            common_plugin_init += f"        self.{plugin} = {plugin}(self)\n"
            common_async_loaded_plugins += f"    {plugin} = Final[{plugin}Async]\n"
            common_async_plugin_init += f"        self.{plugin} = {plugin}Async(self)\n"
        common_loaded_plugins = common_loaded_plugins[:-1]

        text = text.replace("{LoadedPlugins}", common_loaded_plugins)
        text = text.replace("{PluginInit}", common_plugin_init)
        text = text.replace("{LoadedPluginsAsync}", common_async_loaded_plugins)
        text = text.replace("{PluginInitAsync}", common_async_plugin_init)

        # Generate module classes
        for module_name, plugin_list in self.ModuleInheritance.items():
            module_class = module_class_template

            module_loaded_plugins = ""
            module_plugin_init = ""
            async_module_loaded_plugins = ""
            async_module_plugin_init = ""
            for plugin in plugin_list:
                module_loaded_plugins += f"    {plugin} = Final[{plugin}]\n"
                module_plugin_init += f"        self.{plugin} = {plugin}(self)\n"
                async_module_loaded_plugins += f"    {plugin} = Final[{plugin}Async]\n"
                async_module_plugin_init += f"        self.{plugin} = {plugin}Async(self)\n"

            module_loaded_plugins = module_loaded_plugins[:-1]

            module_class = module_class.replace("{LoadedPlugins}", module_loaded_plugins)
            module_class = module_class.replace("{PluginInit}", module_plugin_init)
            module_class = module_class.replace("{LoadedPluginsAsync}", async_module_loaded_plugins)
            module_class = module_class.replace("{PluginInitAsync}", async_module_plugin_init)
            module_class = module_class.replace("{ModuleName}", module_name)
            module_class = module_class[:-1]

            text += module_class + "\n"

        text = text[:-1]

        with open("../ampapi/modules.py", "w", encoding="UTF-8") as file:
            file.write(text)

    def generate(self) -> None:
        """Generate Code"""
        self.generate_types()
        self.generate_plugins()
        self.generate_modules()

if __name__ == "__main__":
    CodeGen().generate()
