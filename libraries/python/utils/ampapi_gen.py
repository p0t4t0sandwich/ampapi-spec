#!/bin/python3
from __future__ import annotations

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
    "JSONRawResponse": "Any",
    "List": "list",
    "Object": "Any",
    "String": "str",
    "TimeSpan": "str",
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
            f.close()

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

    def generate_types(self) -> None:
        text = ""
        with open("./templates/type_base.txt") as f:
            text = f.read()
            f.close()

        class_text_template = ""
        with open("./templates/type_class.txt") as f:
            class_text_template = f.read()
            f.close()

        enum_text_template = ""
        with open("./templates/type_enum.txt") as f:
            enum_text_template = f.read()
            f.close()

        generic_text_template = ""
        with open("./templates/type_generic.txt") as f:
            generic_text_template = f.read()
            f.close()

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
            f.close()

if __name__ == "__main__":
    code_gen = CodeGen()
    code_gen.generate_types()
