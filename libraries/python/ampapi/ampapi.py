# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from __future__ import annotations
from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar
import time

import requests
import json

from aiohttp import ClientSession
from ampapi.types import LoginResult


class AMPAPI():
    """Class for interacting with the AMP API"""
    def __init__(self, baseUri: str, username: str = "", password: str = "", rememberMeToken: str = "", sessionId: str = "") -> None:
        """Initializes the AMP API class
        :param baseUri: The base URI of the AMP instance
        :type baseUri: str
        :returns: None
        """
        self.baseUri: str = baseUri

        # Check if the baseUri ends with a slash
        if not self.baseUri[-1] == "/":
            self.baseUri += "/"
        self.dataSource: str = self.baseUri + "API/"

        self.username: str = username
        self.password: str = password
        self.rememberMeToken: str = rememberMeToken
        self.sessionId: str = sessionId

        self.lastAPICall: int = round(time.time())
        self.relogInterval: int = 60*5

        self.headers: dict = {
            'Content-Type': 'application/json',
            'Accept': 'text/javascript',
            'User-Agent': 'ampapi-py/1.3.6'
        }

    def api_call(self, endpoint: str, data: dict = {}) -> dict:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: dict
        """
        # Check the last API call time, and if it's been more than the relog interval, relog.
        if round(time.time()) - self.lastAPICall > self.relogInterval:
            self.lastAPICall = round(time.time())
            self.Login()
        else:
            self.lastAPICall = round(time.time())
        session = {"SESSIONID": self.sessionId}

        data_added = dict(session, **data)
        data_json = json.dumps(data_added)

        res = requests.post(
            url=f"{self.dataSource}{endpoint}",
            headers=self.headers,
            data=data_json
        )

        response = json.loads(res.content)

        # Raise an exception if the API call failed
        if isinstance(response, dict) and "Title" in response.keys() and "Message" in response.keys() and "StackTrace" in response.keys():
            raise Exception(f"{response['Title']}: {response['Message']}\n{response['StackTrace']}")

        return response

    async def api_call_async(self, endpoint: str, data: dict = {}) -> dict:
        """Method to make AMP API calls
        :param endpoint: The endpoint to call
        :type endpoint: str
        :param data: The data to send to the endpoint
        :type data: dict
        :value data: {}
        :returns: dict with the result of the API call
        :rtype: dict
        """
        # Check the last API call time, and if it's been more than the relog interval, relog.
        now: int = round(time.time())
        if now - self.lastAPICall > self.relogInterval:
            self.lastAPICall = now
            await self.LoginAsync()
        else:
            self.lastAPICall = now
        session = {"SESSIONID": self.sessionId}

        data_added = dict(session, **data)
        data_json = json.dumps(data_added)

        response: dict = {}
        async with ClientSession() as session:
            async with session.post(url=f'{self.dataSource}{endpoint}', headers=self.headers, data=data_json) as post:
                response = await post.json()
                post.close()

        # Raise an exception if the API call failed
        if isinstance(response, dict) and "Title" in response.keys() and "Message" in response.keys() and "StackTrace" in response.keys():
            raise Exception(f"{response['Title']}: {response['Message']}\n{response['StackTrace']}")

        return response

    def Login(self) -> LoginResult:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        data: dict = {
            "username": self.username,
            "password": self.password,
            "token": self.rememberMeToken,
            "rememberMe": True,
        }

        # If remember me token is empty, use the password.
        if self.rememberMeToken == "":
            data["password"] = self.password

        loginResult: LoginResult = LoginResult(**(self.api_call("Core/Login", data)))

        if loginResult.success == True:
            self.rememberMeToken = loginResult.rememberMeToken
            self.sessionId = loginResult.sessionID

        return loginResult

    async def LoginAsync(self) -> LoginResult:
        """
        Simplified login function
        :returns: dict with the result of the login
        """
        data: dict = {
            "username": self.username,
            "password": self.password,
            "token": self.rememberMeToken,
            "rememberMe": True,
        }

        # If remember me token is empty, use the password.
        if self.rememberMeToken == "":
            data["password"] = self.password

        loginResult: LoginResult = LoginResult(**(self.api_call("Core/Login", data)))

        if loginResult.success == True:
            self.rememberMeToken = loginResult.rememberMeToken
            self.sessionId = loginResult.sessionID

        return loginResult
