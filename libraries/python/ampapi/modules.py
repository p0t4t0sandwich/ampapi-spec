from __future__ import annotations

from typing import Final

from .ampapi import AMPAPI, AMPAPIAsync
from .auth import AuthProvider
from .plugins import *

class CommonAPI(AMPAPI):
    Core = Final[Core]
    EmailSenderPlugin = Final[EmailSenderPlugin]
    FileManagerPlugin = Final[FileManagerPlugin]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.Core = Core(self)
        self.EmailSenderPlugin = EmailSenderPlugin(self)
        self.FileManagerPlugin = FileManagerPlugin(self)

class ADS(CommonAPI):
    ADSModule = Final[ADSModule]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.ADSModule = ADSModule(self)

class GenericModule(CommonAPI):
    AnalyticsPlugin = Final[AnalyticsPlugin]
    GenericModule = Final[GenericModule]
    LocalFileBackupPlugin = Final[LocalFileBackupPlugin]
    RCONPlugin = Final[RCONPlugin]
    steamcmdplugin = Final[steamcmdplugin]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPlugin(self)
        self.GenericModule = GenericModule(self)
        self.LocalFileBackupPlugin = LocalFileBackupPlugin(self)
        self.RCONPlugin = RCONPlugin(self)
        self.steamcmdplugin = steamcmdplugin(self)

class Minecraft(CommonAPI):
    AnalyticsPlugin = Final[AnalyticsPlugin]
    LocalFileBackupPlugin = Final[LocalFileBackupPlugin]
    MinecraftModule = Final[MinecraftModule]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPlugin(self)
        self.LocalFileBackupPlugin = LocalFileBackupPlugin(self)
        self.MinecraftModule = MinecraftModule(self)
