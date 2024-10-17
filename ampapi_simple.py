#!/bin/python3

from __future__ import annotations

from json import dumps, loads
from requests import post
from typing import Any, Union

class AMPAPI:
    sessionId: str = ""
    dataSource: str = ""
    username: str = ""
    password: str = ""

    def __init__(self, baseUri: str) -> None:
        if not baseUri[-1] == "/":
            self.dataSource = baseUri + "/API"
        else:
            self.dataSource = baseUri + "API"

    def APICall(self, endpoint: str, data: dict[str, Any] = {}) -> dict[str, Any]:
        headers = {'Accept': 'text/javascript',}
        session = {"SESSIONID": self.sessionId}
        data_added = dict(session, **data)
        data_json = dumps(data_added)

        res = post(
            url=f"{self.dataSource}/{endpoint}",
            headers=headers,
            data=data_json
        )
        res_json = loads(res.content)

        return res_json

    def Login(self, username: str, password: str) -> dict[str, Any]:
        self.username = username
        self.password = password
        res = self.APICall("Core/Login", {"username": username, "password": password, "token": "", "rememberMe": False})
        if "success" in res.keys() and res["success"] == True:
            self.sessionId = res["sessionID"]
        return res

    def ADSModule_GetInstances(self) -> dict[str, Any]:
        return self.APICall("ADSModule/GetInstances")

    def Core_GetAPISpec(self) -> dict[str, Any]:
        return self.APICall("Core/GetAPISpec")

    def Core_GetUpdateInfo(self) -> dict[str, Any]:
        return self.APICall("Core/GetUpdateInfo")

    def InstanceLogin(self, instance_id: str) -> Union[AMPAPI, None]:
        new = AMPAPI(self.dataSource + f"/ADSModule/Servers/{instance_id}")
        loginResult = new.Login(self.username, self.password)
        if loginResult != None and "success" in loginResult.keys() and loginResult["success"] == True:
            return new
        else:
            return None
