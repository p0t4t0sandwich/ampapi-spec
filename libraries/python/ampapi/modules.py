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

class CommonAPIAsync(AMPAPIAsync):
    Core = Final[CoreAsync]
    EmailSenderPlugin = Final[EmailSenderPluginAsync]
    FileManagerPlugin = Final[FileManagerPluginAsync]

    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.Core = CoreAsync(self)
        self.EmailSenderPlugin = EmailSenderPluginAsync(self)
        self.FileManagerPlugin = FileManagerPluginAsync(self)

class ADS(CommonAPI):
    ADSModule = Final[ADSModule]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.ADSModule = ADSModule(self)

class ADSAsync(CommonAPIAsync):
    ADSModule = Final[ADSModuleAsync]

    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.ADSModule = ADSModuleAsync(self)

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

class GenericModuleAsync(CommonAPIAsync):
    AnalyticsPlugin = Final[AnalyticsPluginAsync]
    GenericModule = Final[GenericModuleAsync]
    LocalFileBackupPlugin = Final[LocalFileBackupPluginAsync]
    RCONPlugin = Final[RCONPluginAsync]
    steamcmdplugin = Final[steamcmdpluginAsync]

    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPluginAsync(self)
        self.GenericModule = GenericModuleAsync(self)
        self.LocalFileBackupPlugin = LocalFileBackupPluginAsync(self)
        self.RCONPlugin = RCONPluginAsync(self)
        self.steamcmdplugin = steamcmdpluginAsync(self)

class Minecraft(CommonAPI):
    AnalyticsPlugin = Final[AnalyticsPlugin]
    LocalFileBackupPlugin = Final[LocalFileBackupPlugin]
    MinecraftModule = Final[MinecraftModule]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPlugin(self)
        self.LocalFileBackupPlugin = LocalFileBackupPlugin(self)
        self.MinecraftModule = MinecraftModule(self)

class MinecraftAsync(CommonAPIAsync):
    AnalyticsPlugin = Final[AnalyticsPluginAsync]
    LocalFileBackupPlugin = Final[LocalFileBackupPluginAsync]
    MinecraftModule = Final[MinecraftModuleAsync]

    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPluginAsync(self)
        self.LocalFileBackupPlugin = LocalFileBackupPluginAsync(self)
        self.MinecraftModule = MinecraftModuleAsync(self)

class Rust(CommonAPI):
    AnalyticsPlugin = Final[AnalyticsPlugin]
    LocalFileBackupPlugin = Final[LocalFileBackupPlugin]
    RCONPlugin = Final[RCONPlugin]
    RustModule = Final[RustModule]
    steamcmdplugin = Final[steamcmdplugin]
    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPlugin(self)
        self.LocalFileBackupPlugin = LocalFileBackupPlugin(self)
        self.RCONPlugin = RCONPlugin(self)
        self.RustModule = RustModule(self)
        self.steamcmdplugin = steamcmdplugin(self)

class RustAsync(CommonAPIAsync):
    AnalyticsPlugin = Final[AnalyticsPluginAsync]
    LocalFileBackupPlugin = Final[LocalFileBackupPluginAsync]
    RCONPlugin = Final[RCONPluginAsync]
    RustModule = Final[RustModuleAsync]
    steamcmdplugin = Final[steamcmdpluginAsync]

    def __init__(self, auth: AuthProvider):
        super().__init__(auth)
        self.AnalyticsPlugin = AnalyticsPluginAsync(self)
        self.LocalFileBackupPlugin = LocalFileBackupPluginAsync(self)
        self.RCONPlugin = RCONPluginAsync(self)
        self.RustModule = RustModuleAsync(self)
        self.steamcmdplugin = steamcmdpluginAsync(self)
