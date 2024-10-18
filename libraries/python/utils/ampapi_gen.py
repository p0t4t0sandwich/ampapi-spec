#!/bin/python3
from json import dumps, loads
from typing import Any

import sys
sys.path.append("../../../")
from validate_types import TypeDef, TypeField

# @dataclass
# class TypeField:
#     Name: str
#     TypeName: str
#     Description: str
#     Optional: bool = None
#     Value: int = None

# @dataclass
# class TypeDef:
#     Description: str
#     Fields: list[TypeField]
#     SpecialNote: str = None
#     SpecialType: str = None
#     SerializesAs: str = None

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
    APISpec: dict[str, dict[str, Any]] = {}
    TypeSpec: dict[str, TypeDef] = {}

    def _load_api_spec(self) -> None:
        with open("../../../TypedAPISpec.json") as f:
            json_str: str = f.read()
            self.APISpec = loads(json_str)

    def _load_type_spec(self) -> None:
        with open("../../../TypeSpec.json") as f:
            json_str: str = f.read()
            for type_name, type_def in loads(json_str).items():
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

    def _convert_type(self, type_name: str) -> str:
        if "List<" in type_name:
            t = type_name.replace("List<", "").replace(">", "")
            if t in cs_to_py:
                t = cs_to_py[t]
            return f"list[{t}]"
        if "Dictionary<" in type_name:
            t = type_name.replace("Dictionary<", "").replace(">", "")
            types = t.split(", ")
            if types[0] in cs_to_py:
                types[0] = cs_to_py[types[0]]
            if types[1] in cs_to_py:
                types[1] = cs_to_py[types[1]]
            return f"dict[{types[0]}, {types[1]}]"
        if "Nullable<" in type_name:
            t = type_name.replace("Nullable<", "").replace(">", "")
            if t in cs_to_py:
                t = cs_to_py[t]
            return f"{t} | None"
        if "ActionResult<" in type_name:
            t = type_name.replace("ActionResult<", "").replace(">", "")
            if t in cs_to_py:
                t = cs_to_py[t]
            return f"ActionResult[{t}]"
        if type_name in cs_to_py:
            return cs_to_py[type_name]
        return type_name

    def generate_types(self) -> None:
        text = ""
        with open("./templates/type_base.txt") as f:
            text = f.read()

        class_text_template = ""
        with open("./templates/type_class.txt") as f:
            class_text_template = f.read()

        enum_text_template = ""
        with open("./templates/type_enum.txt") as f:
            enum_text_template = f.read()

        generic_text_template = ""
        with open("./templates/type_generic.txt") as f:
            generic_text_template = f.read()

        for type_name, type_def in self.TypeSpec.items():
            class_text = class_text_template
            enum_text = enum_text_template
            generic_text = generic_text_template

            fields = ""

            if type_def.SpecialType == "Enum":
                type_def_description = type_def.Description

                for field in type_def.Fields:
                    field_text = f"    {field.Name} = {field.Value}\n"
                    fields += field_text

                    type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"

                enum_text = enum_text.replace("{TypeFields}", fields)
                enum_text = enum_text.replace("{TypeName}", type_name)
                enum_text = enum_text.replace("{TypeDescription}", type_def_description)

                text += enum_text

            elif type_def.SpecialType == "Generic":
                type_def_description = type_def.Description

                for field in type_def.Fields:
                    if field.TypeName in cs_to_py:
                        field_text = f"    {field.Name}: '{cs_to_py[field.TypeName]}'"
                        type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {cs_to_py[field.TypeName]}"
                    else:
                        field_text = f"    {field.Name}: '{field.TypeName}'"
                        type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"

                    if field.Optional:
                        field_text += " | None"

                    field_text += "\n"
                    fields += field_text

                generic_text = generic_text.replace("{TypeFields}", fields)
                generic_text = generic_text.replace("{TypeName}", type_name)
                generic_text = generic_text.replace("{TypeDescription}", type_def_description)

                text += generic_text

            else:
                type_def_description = type_def.Description

                for field in type_def.Fields:
                    if "List<" in field.TypeName:
                        t = field.TypeName.replace("List<", "").replace(">", "")
                        if t in cs_to_py:
                            t = cs_to_py[t]
                        field_text = f"    {field.Name}: 'list[{t}]'"

                        type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: list[{t}]"

                    elif "Dictionary<" in field.TypeName:
                        t = field.TypeName.replace("Dictionary<", "").replace(">", "")
                        types = t.split(", ")
                        if types[0] in cs_to_py:
                            types[0] = cs_to_py[types[0]]
                        if types[1] in cs_to_py:
                            types[1] = cs_to_py[types[1]]
                        field_text = f"    {field.Name}: 'dict[{types[0]}, {types[1]}]'"

                        type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: dict[{types[0]}, {types[1]}]"

                    else:
                        if field.TypeName in cs_to_py:
                            field_text = f"    {field.Name}: '{cs_to_py[field.TypeName]}'"
                            type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {cs_to_py[field.TypeName]}"
                        else:
                            field_text = f"    {field.Name}: '{field.TypeName}'"
                            type_def_description += f"\n    :param {field.Name}: {field.Description}\n    :type {field.Name}: {field.TypeName}"

                    if field.Optional:
                        field_text += " | None"

                    field_text += "\n"
                    fields += field_text

                class_text = class_text.replace("{TypeFields}", fields)
                class_text = class_text.replace("{TypeName}", type_name)
                class_text = class_text.replace("{TypeDescription}", type_def_description)

                text += class_text

        with open(f"../ampapi/types.py", "w") as f:
            f.write(text)

    def generate_plugins(self) -> None:
        text = ""
        with open("./templates/plugin_base.txt") as f:
            text = f.read()

        plugin_class_template = ""
        with open("./templates/plugin_class.txt") as f:
            plugin_class_template = f.read()

        plugin_method_template = ""
        with open("./templates/plugin_method.txt") as f:
            plugin_method_template = f.read()

        for plugin_name, method_spec in self.APISpec.items():
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
                method_text = method_text.replace("{MethodDescription}", method_def.get("Description", ""))
                method_text = method_text.replace("{ReturnType}", self._convert_type(method_def["ReturnTypeName"]))

                plugin_methods += method_text

            plugin_class = plugin_class.replace("{PluginMethods}", plugin_methods)
            plugin_class = plugin_class.replace("{PluginName}", plugin_name)

            text += plugin_class
        
        with open(f"../ampapi/plugins.py", "w") as f:
            f.write(text)

if __name__ == "__main__":
    code_gen = CodeGen()
    code_gen.generate_types()
    code_gen.generate_plugins()
