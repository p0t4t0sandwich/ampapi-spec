# An API that allows you to communicate with AMP installations from within Python
# Author: p0t4t0sandich

from typing import Any
from ampapi.ampapi import AMPAPI
from ampapi.types import *


class AnalyticsPlugin(AMPAPI):
    def __init__(self, ampapi: AMPAPI) -> None:
        """Initializes the AnalyticsPlugin class
        :param ampapi: The AMPAPI class to clone
        :returns: None
        """
        super().__init__(ampapi.baseUri, ampapi.username, ampapi.password, ampapi.rememberMeToken, ampapi.sessionId)

    def GetAnalyticsSummary(self, PeriodDays: int, StartDate: Any, Filters: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param PeriodDays: {int}  True
        :param StartDate: {Any}  True
        :param Filters: {dict[str, str]}  True
        :returns: Any
        """
        response: dict = self.api_call("AnalyticsPlugin/GetAnalyticsSummary", { 
            "PeriodDays": PeriodDays,
            "StartDate": StartDate,
            "Filters": Filters,
        })
        return Any(**response)

    async def GetAnalyticsSummaryAsync(self, PeriodDays: int, StartDate: Any, Filters: dict[str, str]) -> Any:
        """
        Name Description Optional
        :param PeriodDays: {int}  True
        :param StartDate: {Any}  True
        :param Filters: {dict[str, str]}  True
        :returns: Any
        """
        response: dict = await self.api_call_async("AnalyticsPlugin/GetAnalyticsSummary", { 
            "PeriodDays": PeriodDays,
            "StartDate": StartDate,
            "Filters": Filters,
        })
        return Any(**response)

