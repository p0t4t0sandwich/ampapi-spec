from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Generic, TypeVar

T = TypeVar('T')

class ActionResult(Generic[T]):
    """
    Generic response type for calls that return a result and a reason for failure
    :param Reason: Reason for failure
    :type Reason: str
    :param Result: Result of the call
    :type Result: T | None
    :param SupportURL: Support URL
    :type SupportURL: str
    :param SupportTitle: Support title
    :type SupportTitle: str
    :param Status: true if successful, false if not
    :type Status: bool
    """
    Reason: 'str'
    Result: 'T | None'
    SupportURL: 'str'
    SupportTitle: 'str'
    Status: 'bool'

@dataclass
class AMPInstanceBase:
    """
    Base class for an AMP instance
    :param AMPBuild: The AMP build
    :type AMPBuild: str
    :param AMPVersion: The AMP version
    :type AMPVersion: Version
    :param IP: The IP
    :type IP: str
    :param OS: The OS
    :type OS: SupportedOS
    :param ContainerCPUs: The container CPUs
    :type ContainerCPUs: float
    :param ContainerMemoryMB: The container memory in MB
    :type ContainerMemoryMB: int
    :param ContainerMemoryPolicy: The container memory policy
    :type ContainerMemoryPolicy: ContainerMemoryPolicy
    :param ContainerSwapMB: The container swap in MB
    :type ContainerSwapMB: int
    :param CreatedBy: The creator ID
    :type CreatedBy: str
    :param CustomMountBinds: The custom mount binds
    :type CustomMountBinds: dict[str, str]
    :param CustomPorts: The custom ports
    :type CustomPorts: list[PortUsage]
    :param DatastoreId: The datastore ID
    :type DatastoreId: int
    :param DeploymentArgs: The deployment arguments
    :type DeploymentArgs: dict[str, str]
    :param Description: The description
    :type Description: str
    :param DiskUsageMB: The disk usage in MB
    :type DiskUsageMB: int
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    :param ExtraContainerPackages: The extra container packages
    :type ExtraContainerPackages: list[str]
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Group: The group
    :type Group: str
    :param InstanceID: The instance ID
    :type InstanceID: str
    :param InstanceName: The instance name
    :type InstanceName: str
    :param LastReactivationAttempt: The last reactivation attempt
    :type LastReactivationAttempt: str | None
    :param ManagementMode: The management mode
    :type ManagementMode: ManagementModes
    :param MetricsPublishingHMAC: The metrics publishing HMAC
    :type MetricsPublishingHMAC: str
    :param ModuleDisplayName: The module display name
    :type ModuleDisplayName: str
    :param Module: The module
    :type Module: str
    :param OverlayPath: The overlay path
    :type OverlayPath: str
    :param Path: The path
    :type Path: str
    :param PendingSettingChanges: The pending setting changes
    :type PendingSettingChanges: dict[str, str]
    :param Plugins: The plugins
    :type Plugins: list[str]
    :param Port: The port
    :type Port: int
    :param PreviousBuild: The previous build
    :type PreviousBuild: str
    :param PreviousVersion: The previous version
    :type PreviousVersion: Version
    :param ReleaseStream: The release stream
    :type ReleaseStream: AMPReleaseStreams
    :param SpecificDockerImage: The specific Docker image
    :type SpecificDockerImage: str
    :param Tag: The tag
    :type Tag: str
    :param Tags: The tags
    :type Tags: list[str]
    :param TargetID: The target ID
    :type TargetID: str
    :param User: The user
    :type User: str
    :param WelcomeMessage: The welcome message
    :type WelcomeMessage: str
    :param TagsUsedForConfiguration: Whether tags are used for configuration
    :type TagsUsedForConfiguration: bool
    :param DockerBaseReadOnly: Whether the Docker base is read-only
    :type DockerBaseReadOnly: bool
    :param DaemonAutostart: Whether the daemon should autostart
    :type DaemonAutostart: bool
    :param IsHTTPS: Whether the instance is HTTPS
    :type IsHTTPS: bool
    :param IsContainerInstance: Whether the instance is a container
    :type IsContainerInstance: bool
    :param Daemon: Whether the instance is a daemon
    :type Daemon: bool
    :param Suspended: Whether the instance is suspended
    :type Suspended: bool
    :param ExcludeFromFirewall: Whether to exclude from the firewall
    :type ExcludeFromFirewall: bool
    :param ForceDocker: Whether to force Docker
    :type ForceDocker: bool
    :param MatchVersion: Whether to match the version
    :type MatchVersion: bool
    :param AutomaticUPnP: Whether to use automatic UPnP
    :type AutomaticUPnP: bool
    :param UseHostModeNetwork: Whether to use host mode networking
    :type UseHostModeNetwork: bool
    """
    AMPBuild: 'str' = ""
    AMPVersion: 'Version' = None
    IP: 'str' = ""
    OS: 'SupportedOS' = None
    ContainerCPUs: 'float' = 0.0
    ContainerMemoryMB: 'int' = 0
    ContainerMemoryPolicy: 'ContainerMemoryPolicy' = None
    ContainerSwapMB: 'int' = 0
    CreatedBy: 'str' = ""
    CustomMountBinds: 'dict[str, str]' = field(default_factory=dict)
    CustomPorts: 'list[PortUsage]' = field(default_factory=list)
    DatastoreId: 'int' = 0
    DeploymentArgs: 'dict[str, str]' = field(default_factory=dict)
    Description: 'str' = ""
    DiskUsageMB: 'int' = 0
    DisplayImageSource: 'str' = ""
    ExtraContainerPackages: 'list[str]' = field(default_factory=list)
    FriendlyName: 'str' = ""
    Group: 'str' = ""
    InstanceID: 'str' = ""
    InstanceName: 'str' = ""
    LastReactivationAttempt: 'str | None' = None
    ManagementMode: 'ManagementModes' = None
    MetricsPublishingHMAC: 'str' = ""
    ModuleDisplayName: 'str' = ""
    Module: 'str' = ""
    OverlayPath: 'str' = ""
    Path: 'str' = ""
    PendingSettingChanges: 'dict[str, str]' = field(default_factory=dict)
    Plugins: 'list[str]' = field(default_factory=list)
    Port: 'int' = 0
    PreviousBuild: 'str' = ""
    PreviousVersion: 'Version' = None
    ReleaseStream: 'AMPReleaseStreams' = None
    SpecificDockerImage: 'str' = ""
    Tag: 'str' = ""
    Tags: 'list[str]' = field(default_factory=list)
    TargetID: 'str' = ""
    User: 'str' = ""
    WelcomeMessage: 'str' = ""
    TagsUsedForConfiguration: 'bool' = False
    DockerBaseReadOnly: 'bool' = False
    DaemonAutostart: 'bool' = False
    IsHTTPS: 'bool' = False
    IsContainerInstance: 'bool' = False
    Daemon: 'bool' = False
    Suspended: 'bool' = False
    ExcludeFromFirewall: 'bool' = False
    ForceDocker: 'bool' = False
    MatchVersion: 'bool' = False
    AutomaticUPnP: 'bool' = False
    UseHostModeNetwork: 'bool' = False

class AMPReleaseStreams(Enum):
    """
    Represents the AMP release streams
    :param NotSpecified: Not specified
    :type NotSpecified: Int32
    :param LTS: LTS
    :type LTS: Int32
    :param Mainline: Mainline
    :type Mainline: Int32
    :param Preview: Preview
    :type Preview: Int32
    :param Development: Development
    :type Development: Int32
    :param FastTrack: Fast track
    :type FastTrack: Int32
    :param Nightly: Nightly
    :type Nightly: Int32
    :param Bleeding: Bleeding
    :type Bleeding: Int32
    """
    NotSpecified = 0
    LTS = 5
    Mainline = 10
    Preview = 15
    Development = 20
    FastTrack = 100
    Nightly = 1000
    Bleeding = 10000

@dataclass
class APIError:
    """
    An error object
    :param Title: The title of the error
    :type Title: str
    :param Message: The error message
    :type Message: str
    :param StackTrace: The stack trace of the error
    :type StackTrace: str
    """
    Title: 'str' = ""
    Message: 'str' = ""
    StackTrace: 'str' = ""

@dataclass
class APIMethodInfo:
    """
    Information about an API method
    :param Id: The ID
    :type Id: str
    :param Description: The description
    :type Description: str
    :param DisplayFormat: The display format
    :type DisplayFormat: str
    :param Name: The name
    :type Name: str
    :param Consumes: The parameters
    :type Consumes: list[ScheduleTaskParameter]
    """
    Id: 'str' = ""
    Description: 'str' = ""
    DisplayFormat: 'str' = ""
    Name: 'str' = ""
    Consumes: 'list[ScheduleTaskParameter]' = field(default_factory=list)

@dataclass
class ApplicationSpec:
    """
    A specification for an application
    :param Id: The ID
    :type Id: str
    :param Author: The author
    :type Author: str
    :param ContainerReason: The container reason
    :type ContainerReason: str
    :param ContainerSupport: The container support
    :type ContainerSupport: ContainerSupport
    :param DeprecatedReason: The deprecated reason
    :type DeprecatedReason: str
    :param Description: The description
    :type Description: str
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    :param ExtraSetupStepsURI: The extra setup steps URI
    :type ExtraSetupStepsURI: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param ModuleName: The module name
    :type ModuleName: str
    :param Origin: The origin
    :type Origin: str
    :param Settings: The settings
    :type Settings: dict[str, str]
    :param SupportedPlatforms: The supported platforms
    :type SupportedPlatforms: SupportedOS
    :param NoCommercialUsage: Whether commercial usage is allowed
    :type NoCommercialUsage: bool
    :param IsServiceSpec: Whether the spec is a service spec
    :type IsServiceSpec: bool
    """
    Id: 'str' = ""
    Author: 'str' = ""
    ContainerReason: 'str' = ""
    ContainerSupport: 'ContainerSupport' = None
    DeprecatedReason: 'str' = ""
    Description: 'str' = ""
    DisplayImageSource: 'str' = ""
    ExtraSetupStepsURI: 'str' = ""
    FriendlyName: 'str' = ""
    ModuleName: 'str' = ""
    Origin: 'str' = ""
    Settings: 'dict[str, str]' = field(default_factory=dict)
    SupportedPlatforms: 'SupportedOS' = None
    NoCommercialUsage: 'bool' = False
    IsServiceSpec: 'bool' = False

@dataclass
class ApplicationSpecSummary:
    """
    A summary of an application spec
    :param Id: The ID
    :type Id: str
    :param Author: The author
    :type Author: str
    :param ContainerReason: The container reason
    :type ContainerReason: str
    :param ContainerSupport: The container support
    :type ContainerSupport: ContainerSupport
    :param DeprecatedReason: The deprecated reason
    :type DeprecatedReason: str
    :param Description: The description
    :type Description: str
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    :param ExtraSetupStepsURI: The extra setup steps URI
    :type ExtraSetupStepsURI: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Origin: The origin
    :type Origin: str
    :param SupportedPlatforms: The supported platforms
    :type SupportedPlatforms: SupportedOS
    :param NoCommercialUsage: Whether commercial usage is allowed
    :type NoCommercialUsage: bool
    :param IsServiceSpec: Whether the spec is a service spec
    :type IsServiceSpec: bool
    """
    Id: 'str' = ""
    Author: 'str' = ""
    ContainerReason: 'str' = ""
    ContainerSupport: 'ContainerSupport' = None
    DeprecatedReason: 'str' = ""
    Description: 'str' = ""
    DisplayImageSource: 'str' = ""
    ExtraSetupStepsURI: 'str' = ""
    FriendlyName: 'str' = ""
    Origin: 'str' = ""
    SupportedPlatforms: 'SupportedOS' = None
    NoCommercialUsage: 'bool' = False
    IsServiceSpec: 'bool' = False

class ApplicationState(Enum):
    """
    Represents the state of an instance's application
    :param Undefined: Undefined
    :type Undefined: Int32
    :param Stopped: Stopped
    :type Stopped: Int32
    :param PreStart: The server is performing some first-time-start configuration.
    :type PreStart: Int32
    :param Configuring: The server is performing some first-time-start configuration.
    :type Configuring: Int32
    :param Starting: Starting
    :type Starting: Int32
    :param Ready: Ready
    :type Ready: Int32
    :param Restarting: Server is in the middle of stopping, but once shutdown has finished it will automatically restart.
    :type Restarting: Int32
    :param Stopping: Stopping
    :type Stopping: Int32
    :param PreparingForSleep: Preparing for sleep
    :type PreparingForSleep: Int32
    :param Sleeping: The application should be able to be resumed quickly if using this state. Otherwise use Stopped.
    :type Sleeping: Int32
    :param Waiting: The application is waiting for some external service/application to respond/become available.
    :type Waiting: Int32
    :param Installing: Installing
    :type Installing: Int32
    :param Updating: Updating
    :type Updating: Int32
    :param AwaitingUserInput: Used during installation, means that some user input is required to complete setup (authentication etc).
    :type AwaitingUserInput: Int32
    :param Failed: Failed
    :type Failed: Int32
    :param Suspended: Suspended
    :type Suspended: Int32
    :param Maintainence: Maintainence
    :type Maintainence: Int32
    :param Indeterminate: The state is unknown, or doesn't apply (for modules that don't start an external process)
    :type Indeterminate: Int32
    """
    Undefined = -1
    Stopped = 0
    PreStart = 5
    Configuring = 7
    Starting = 10
    Ready = 20
    Restarting = 30
    Stopping = 40
    PreparingForSleep = 45
    Sleeping = 50
    Waiting = 60
    Installing = 70
    Updating = 75
    AwaitingUserInput = 80
    Failed = 100
    Suspended = 200
    Maintainence = 250
    Indeterminate = 999

class Architecture(Enum):
    """
    Represents the architecture
    :param Unknown: Unknown
    :type Unknown: Int32
    :param x86_64: x86_64
    :type x86_64: Int32
    :param aarch64: aarch64
    :type aarch64: Int32
    :param All: All
    :type All: Int32
    """
    Unknown = 0
    x86_64 = 1
    aarch64 = 2
    All = 3

class AuthenticationRequirement(Enum):
    """
    Represents the authentication requirement
    :param None_: None
    :type None_: Int32
    :param Username: Username
    :type Username: Int32
    :param Password: Password
    :type Password: Int32
    :param TOTP: TOTP
    :type TOTP: Int32
    :param Passkeys: Passkeys
    :type Passkeys: Int32
    """
    None_ = 0
    Username = 1
    Password = 2
    TOTP = 4
    Passkeys = 8

class AuthenticationResult(Enum):
    """
    Represents the authentication result
    :param Failure: Failure
    :type Failure: Int32
    :param TokenRejected: Token rejected
    :type TokenRejected: Int32
    :param FullLoginRequired: Full login required
    :type FullLoginRequired: Int32
    :param NoInstanceAccess: No instance access
    :type NoInstanceAccess: Int32
    :param InstanceSuspended: Instance suspended
    :type InstanceSuspended: Int32
    :param Success: Success
    :type Success: Int32
    :param PasswordChangeRequired: Password change required
    :type PasswordChangeRequired: Int32
    :param AccountDisabled: Account disabled
    :type AccountDisabled: Int32
    :param Ignored: Ignored
    :type Ignored: Int32
    :param TwoFactorChallenge: Two-factor challenge
    :type TwoFactorChallenge: Int32
    :param TwoFactorSetupRequired: Two-factor setup required
    :type TwoFactorSetupRequired: Int32
    :param TwoFactorFailed: Two-factor failed
    :type TwoFactorFailed: Int32
    :param PassthruDisabled: Passthru disabled
    :type PassthruDisabled: Int32
    :param PassthruRejected: Passthru rejected
    :type PassthruRejected: Int32
    :param LoginServerUnavailable: Login server unavailable
    :type LoginServerUnavailable: Int32
    """
    Failure = 0
    TokenRejected = 1
    FullLoginRequired = 2
    NoInstanceAccess = 5
    InstanceSuspended = 6
    Success = 10
    PasswordChangeRequired = 20
    AccountDisabled = 25
    Ignored = 30
    TwoFactorChallenge = 40
    TwoFactorSetupRequired = 45
    TwoFactorFailed = 50
    PassthruDisabled = 100
    PassthruRejected = 110
    LoginServerUnavailable = 500

@dataclass
class AuthRoleSummary:
    """
    A summary of an authenticated role
    :param ID: The ID
    :type ID: str
    :param Description: The description
    :type Description: str
    :param Members: The members
    :type Members: list[AuthUserSummary]
    :param Name: The name
    :type Name: str
    :param Permissions: The permissions
    :type Permissions: list[str]
    :param DisableEdits: Whether edits are disabled
    :type DisableEdits: bool
    :param IsCommonRole: Whether the role is common
    :type IsCommonRole: bool
    :param IsDefault: Whether the role is default
    :type IsDefault: bool
    :param Hidden: Whether the role is hidden
    :type Hidden: bool
    :param IsInstanceSpecific: Whether the role is instance specific
    :type IsInstanceSpecific: bool
    """
    ID: 'str' = ""
    Description: 'str' = ""
    Members: 'list[AuthUserSummary]' = field(default_factory=list)
    Name: 'str' = ""
    Permissions: 'list[str]' = field(default_factory=list)
    DisableEdits: 'bool' = False
    IsCommonRole: 'bool' = False
    IsDefault: 'bool' = False
    Hidden: 'bool' = False
    IsInstanceSpecific: 'bool' = False

@dataclass
class AuthUserSummary:
    """
    A summary of an authenticated user
    :param ID: The ID
    :type ID: str
    :param Name: The name
    :type Name: str
    """
    ID: 'str' = ""
    Name: 'str' = ""

@dataclass
class BackupManifest:
    """
    A backup manifest
    :param Id: The ID
    :type Id: str
    :param HashSHA1: The SHA1 hash
    :type HashSHA1: str
    :param Description: The description
    :type Description: str
    :param META: The meta
    :type META: str
    :param ModuleName: The module name
    :type ModuleName: str
    :param Name: The name
    :type Name: str
    :param ParentManifest: The parent manifest
    :type ParentManifest: str | None
    :param RemoteStoreId: The remote store ID
    :type RemoteStoreId: str
    :param SourceOS: The source OS
    :type SourceOS: SupportedOS
    :param Timestamp: The timestamp
    :type Timestamp: str
    :param TotalSizeBytes: The total size in bytes
    :type TotalSizeBytes: int
    :param TakenBy: The user who took the backup
    :type TakenBy: str
    :param Sticky: Whether the backup is sticky
    :type Sticky: bool
    :param StoredLocally: Whether the backup is stored locally
    :type StoredLocally: bool
    :param StoredRemotely: Whether the backup is stored remotely
    :type StoredRemotely: bool
    :param CreatedAutomatically: Whether the backup was created automatically
    :type CreatedAutomatically: bool
    """
    Id: 'str' = ""
    HashSHA1: 'str' = ""
    Description: 'str' = ""
    META: 'str' = ""
    ModuleName: 'str' = ""
    Name: 'str' = ""
    ParentManifest: 'str | None' = None
    RemoteStoreId: 'str' = ""
    SourceOS: 'SupportedOS' = None
    Timestamp: 'str' = ""
    TotalSizeBytes: 'int' = 0
    TakenBy: 'str' = ""
    Sticky: 'bool' = False
    StoredLocally: 'bool' = False
    StoredRemotely: 'bool' = False
    CreatedAutomatically: 'bool' = False

@dataclass
class Branding:
    """
    Branding information
    :param URL: The URL
    :type URL: str
    :param BackgroundURL: The background URL
    :type BackgroundURL: str
    :param BrandingMessage: The branding message
    :type BrandingMessage: str
    :param CompanyName: The company name
    :type CompanyName: str
    :param ForgotPasswordURL: The forgot password URL
    :type ForgotPasswordURL: str
    :param LogoURL: The logo URL
    :type LogoURL: str
    :param PageTitle: The page title
    :type PageTitle: str
    :param ShortBrandingMessage: The short branding message
    :type ShortBrandingMessage: str
    :param SplashFrameURL: The splash frame URL
    :type SplashFrameURL: str
    :param SubmitTicketURL: The submit ticket URL
    :type SubmitTicketURL: str
    :param SupportURL: The support URL
    :type SupportURL: str
    :param SupportText: The support text
    :type SupportText: str
    :param WelcomeMessage: The welcome message
    :type WelcomeMessage: str
    :param DisplayBranding: Whether to display branding
    :type DisplayBranding: bool
    """
    URL: 'str' = ""
    BackgroundURL: 'str' = ""
    BrandingMessage: 'str' = ""
    CompanyName: 'str' = ""
    ForgotPasswordURL: 'str' = ""
    LogoURL: 'str' = ""
    PageTitle: 'str' = ""
    ShortBrandingMessage: 'str' = ""
    SplashFrameURL: 'str' = ""
    SubmitTicketURL: 'str' = ""
    SupportURL: 'str' = ""
    SupportText: 'str' = ""
    WelcomeMessage: 'str' = ""
    DisplayBranding: 'bool' = False

@dataclass
class BrandingSettings:
    """
    Branding information
    :param URL: The URL
    :type URL: str
    :param BackgroundURL: The background URL
    :type BackgroundURL: str
    :param BrandingMessage: The branding message
    :type BrandingMessage: str
    :param CompanyName: The company name
    :type CompanyName: str
    :param ForgotPasswordURL: The forgot password URL
    :type ForgotPasswordURL: str
    :param LogoURL: The logo URL
    :type LogoURL: str
    :param PageTitle: The page title
    :type PageTitle: str
    :param ShortBrandingMessage: The short branding message
    :type ShortBrandingMessage: str
    :param SplashFrameURL: The splash frame URL
    :type SplashFrameURL: str
    :param SubmitTicketURL: The submit ticket URL
    :type SubmitTicketURL: str
    :param SupportURL: The support URL
    :type SupportURL: str
    :param SupportText: The support text
    :type SupportText: str
    :param WelcomeMessage: The welcome message
    :type WelcomeMessage: str
    :param DisplayBranding: Whether to display branding
    :type DisplayBranding: bool
    """
    URL: 'str' = ""
    BackgroundURL: 'str' = ""
    BrandingMessage: 'str' = ""
    CompanyName: 'str' = ""
    ForgotPasswordURL: 'str' = ""
    LogoURL: 'str' = ""
    PageTitle: 'str' = ""
    ShortBrandingMessage: 'str' = ""
    SplashFrameURL: 'str' = ""
    SubmitTicketURL: 'str' = ""
    SupportURL: 'str' = ""
    SupportText: 'str' = ""
    WelcomeMessage: 'str' = ""
    DisplayBranding: 'bool' = False

@dataclass
class ConsoleEntry:
    """
    Type for Core.GetUpdates#ConsoleEntries
    :param SourceId: The ID of the message's source, eg from a player/user
    :type SourceId: str
    :param Contents: The contents of the console entry
    :type Contents: str
    :param Source: The source of the console entry
    :type Source: str
    :param Timestamp: The timestamp of the console entry
    :type Timestamp: str
    :param Type: The type of the console entry
    :type Type: str
    """
    SourceId: 'str' = ""
    Contents: 'str' = ""
    Source: 'str' = ""
    Timestamp: 'str' = ""
    Type: 'str' = ""

class ContainerMemoryPolicy(Enum):
    """
    Represents the container memory policy
    :param NotSpecified: Not specified
    :type NotSpecified: Int32
    :param Reserve: Reserve
    :type Reserve: Int32
    :param Restrict: Restrict
    :type Restrict: Int32
    """
    NotSpecified = 0
    Reserve = 100
    Restrict = 200

class ContainerSupport(Enum):
    """
    Represents the container support
    :param NoPreference: No preference
    :type NoPreference: Int32
    :param NotSupported: Not supported
    :type NotSupported: Int32
    :param SupportedOnLinux: Supported on Linux
    :type SupportedOnLinux: Int32
    :param SupportedOnWindows: Supported on Windows
    :type SupportedOnWindows: Int32
    :param Supported: Supported
    :type Supported: Int32
    :param RecommendedOnLinux: Recommended on Linux
    :type RecommendedOnLinux: Int32
    :param RecommendedOnWindows: Recommended on Windows
    :type RecommendedOnWindows: Int32
    :param Recommended: Recommended
    :type Recommended: Int32
    :param RequiredOnLinux: Required on Linux
    :type RequiredOnLinux: Int32
    :param RequiredOnWindows: Required on Windows
    :type RequiredOnWindows: Int32
    :param Required: Required
    :type Required: Int32
    """
    NoPreference = 0
    NotSupported = 1
    SupportedOnLinux = 2
    SupportedOnWindows = 4
    Supported = 6
    RecommendedOnLinux = 8
    RecommendedOnWindows = 16
    Recommended = 24
    RequiredOnLinux = 32
    RequiredOnWindows = 64
    Required = 96

@dataclass
class DatastoreSummary:
    """
    A datastore object
    :param Id: The datastore ID
    :type Id: int
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    """
    Id: 'int' = 0
    FriendlyName: 'str' = ""

@dataclass
class DeploymentTemplate:
    """
    A deployment template object
    :param Id: The ID
    :type Id: int
    :param Description: The description
    :type Description: str
    :param Module: The module
    :type Module: str
    :param Name: The name
    :type Name: str
    :param SettingMappings: The setting mappings
    :type SettingMappings: dict[str, str]
    :param Tags: The tags
    :type Tags: list[str]
    :param TemplateBaseApp: The template base app
    :type TemplateBaseApp: str
    :param TemplateInstance: The template instance
    :type TemplateInstance: str | None
    :param TemplateRole: The template role
    :type TemplateRole: str | None
    :param ZipOverlayPath: The zip overlay path
    :type ZipOverlayPath: str
    :param CloneRoleIntoUser: Whether to clone the role into the user
    :type CloneRoleIntoUser: bool
    :param MatchDatastoreTags: Whether to match datastore tags
    :type MatchDatastoreTags: bool
    :param StartOnBoot: Whether to start on boot
    :type StartOnBoot: bool
    """
    Id: 'int' = 0
    Description: 'str' = ""
    Module: 'str' = ""
    Name: 'str' = ""
    SettingMappings: 'dict[str, str]' = field(default_factory=dict)
    Tags: 'list[str]' = field(default_factory=list)
    TemplateBaseApp: 'str' = ""
    TemplateInstance: 'str | None' = None
    TemplateRole: 'str | None' = None
    ZipOverlayPath: 'str' = ""
    CloneRoleIntoUser: 'bool' = False
    MatchDatastoreTags: 'bool' = False
    StartOnBoot: 'bool' = False

@dataclass
class DirectoryListing:
    """
    A file directory object
    :param Created: The creation date
    :type Created: str
    :param Filename: The filename
    :type Filename: str
    :param Modified: The modification date
    :type Modified: str
    :param SizeBytes: The size in bytes
    :type SizeBytes: int
    :param IsDirectory: Whether the file is a directory
    :type IsDirectory: bool
    :param IsVirtualDirectory: Whether the file is a virtual directory
    :type IsVirtualDirectory: bool
    :param IsArchive: Whether the file is an archive
    :type IsArchive: bool
    :param IsDownloadable: Whether the file is downloadable
    :type IsDownloadable: bool
    :param IsEditable: Whether the file is editable
    :type IsEditable: bool
    :param IsExcludedFromBackups: Whether the file is excluded from backups
    :type IsExcludedFromBackups: bool
    """
    Created: 'str' = ""
    Filename: 'str' = ""
    Modified: 'str' = ""
    SizeBytes: 'int' = 0
    IsDirectory: 'bool' = False
    IsVirtualDirectory: 'bool' = False
    IsArchive: 'bool' = False
    IsDownloadable: 'bool' = False
    IsEditable: 'bool' = False
    IsExcludedFromBackups: 'bool' = False

@dataclass
class EndpointInfo:
    """
    An application endpoint object
    :param Uri: The URI of the endpoint
    :type Uri: str
    :param DisplayName: The display name of the endpoint
    :type DisplayName: str
    :param Endpoint: The endpoint address
    :type Endpoint: str
    """
    Uri: 'str' = ""
    DisplayName: 'str' = ""
    Endpoint: 'str' = ""

@dataclass
class FileChunkData:
    """
    A chunk of file data
    :param Base64Data: The base64 data
    :type Base64Data: str
    :param BytesLength: The length of the data in bytes
    :type BytesLength: int
    """
    Base64Data: 'str' = ""
    BytesLength: 'int' = 0

@dataclass
class GlibcInfo:
    """
    Glibc information object
    :param Build: The build number
    :type Build: int
    :param MajorRevision: The major revision number
    :type MajorRevision: int
    :param Major: The major version number
    :type Major: int
    :param MinorRevision: The minor revision number
    :type MinorRevision: int
    :param Minor: The minor version number
    :type Minor: int
    :param Revision: The revision number
    :type Revision: int
    """
    Build: 'int' = 0
    MajorRevision: 'int' = 0
    Major: 'int' = 0
    MinorRevision: 'int' = 0
    Minor: 'int' = 0
    Revision: 'int' = 0

@dataclass
class IADSInstance:
    """
    An ADS instance object
    :param AvailableIPs: Available IPs
    :type AvailableIPs: list[str]
    :param AvailableInstances: Available instances
    :type AvailableInstances: list[InstanceSummary]
    :param Id: The ID
    :type Id: int
    :param URL: The URL
    :type URL: str
    :param Datastores: The datastores
    :type Datastores: list[DatastoreSummary]
    :param Description: The description
    :type Description: str
    :param Fitness: The fitness information object
    :type Fitness: ProvisionFitness
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Host: The host
    :type Host: str
    :param InstanceId: The instance ID
    :type InstanceId: str
    :param Instances: The instances
    :type Instances: list[InstanceSummary]
    :param LastUpdated: The last updated date
    :type LastUpdated: str
    :param Platform: The platform information object
    :type Platform: IPlatformInfo
    :param Port: The port
    :type Port: int
    :param StateReason: The state reason
    :type StateReason: str
    :param State: The state
    :type State: RemoteInstanceState
    :param TagsList: The tags list
    :type TagsList: str
    :param Tags: The tags
    :type Tags: list[str]
    :param IsHTTPS: Whether HTTPS is enabled
    :type IsHTTPS: bool
    :param CanCreate: Whether the instance can be created
    :type CanCreate: bool
    :param CreatesInContainers: Whether the instance creates in containers
    :type CreatesInContainers: bool
    :param Disabled: Whether the instance is disabled
    :type Disabled: bool
    :param IsRemote: Whether the instance is remote
    :type IsRemote: bool
    """
    AvailableIPs: 'list[str]' = field(default_factory=list)
    AvailableInstances: 'list[InstanceSummary]' = field(default_factory=list)
    Id: 'int' = 0
    URL: 'str' = ""
    Datastores: 'list[DatastoreSummary]' = field(default_factory=list)
    Description: 'str' = ""
    Fitness: 'ProvisionFitness' = None
    FriendlyName: 'str' = ""
    Host: 'str' = ""
    InstanceId: 'str' = ""
    Instances: 'list[InstanceSummary]' = field(default_factory=list)
    LastUpdated: 'str' = ""
    Platform: 'IPlatformInfo' = None
    Port: 'int' = 0
    StateReason: 'str' = ""
    State: 'RemoteInstanceState' = None
    TagsList: 'str' = ""
    Tags: 'list[str]' = field(default_factory=list)
    IsHTTPS: 'bool' = False
    CanCreate: 'bool' = False
    CreatesInContainers: 'bool' = False
    Disabled: 'bool' = False
    IsRemote: 'bool' = False

@dataclass
class IAuditLogEntry:
    """
    An audit log entry
    :param Id: The ID
    :type Id: int
    :param Category: The category
    :type Category: str
    :param Message: The message
    :type Message: str
    :param Source: The source
    :type Source: str
    :param Timestamp: The timestamp
    :type Timestamp: str
    :param User: The user
    :type User: str
    """
    Id: 'int' = 0
    Category: 'str' = ""
    Message: 'str' = ""
    Source: 'str' = ""
    Timestamp: 'str' = ""
    User: 'str' = ""

@dataclass
class InlineActionAttribute:
    """
    An inline action object
    :param Argument: The argument
    :type Argument: str
    :param Caption: The caption
    :type Caption: str
    :param Method: The method
    :type Method: str
    :param Module: The module
    :type Module: str
    :param IsClientSide: Whether the action is client-side
    :type IsClientSide: bool
    """
    Argument: 'str' = ""
    Caption: 'str' = ""
    Method: 'str' = ""
    Module: 'str' = ""
    IsClientSide: 'bool' = False

@dataclass
class InstanceDatastore:
    """
    A datastore object
    :param CurrentUsageMB: The current usage in MB
    :type CurrentUsageMB: int
    :param Id: The datastore ID
    :type Id: int
    :param Description: The description
    :type Description: str
    :param Directory: The directory
    :type Directory: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param InstanceLimit: The instance limit
    :type InstanceLimit: int
    :param Priority: The priority
    :type Priority: int
    :param SanitisedName: The sanitised name
    :type SanitisedName: str
    :param SoftLimitMB: The soft limit in MB
    :type SoftLimitMB: int
    :param Tags: The tags
    :type Tags: list[str]
    :param Active: Whether the datastore is active
    :type Active: bool
    :param IsInternal: Whether the datastore is internal
    :type IsInternal: bool
    """
    CurrentUsageMB: 'int' = 0
    Id: 'int' = 0
    Description: 'str' = ""
    Directory: 'str' = ""
    FriendlyName: 'str' = ""
    InstanceLimit: 'int' = 0
    Priority: 'int' = 0
    SanitisedName: 'str' = ""
    SoftLimitMB: 'int' = 0
    Tags: 'list[str]' = field(default_factory=list)
    Active: 'bool' = False
    IsInternal: 'bool' = False

@dataclass
class InstanceStatus:
    """
    An instance status object
    :param InstanceID: The instance ID
    :type InstanceID: str
    :param Running: Whether the instance is running
    :type Running: bool
    """
    InstanceID: 'str' = ""
    Running: 'bool' = False

@dataclass
class InstanceSummary:
    """
    An instance object
    :param AMPVersion: The AMP version
    :type AMPVersion: Version
    :param IP: The IP address
    :type IP: str
    :param ApplicationEndpoints: The application endpoints
    :type ApplicationEndpoints: list[EndpointInfo]
    :param AppState: The application state
    :type AppState: ApplicationState
    :param ContainerCPUs: The container CPUs
    :type ContainerCPUs: float
    :param ContainerMemoryMB: The container memory in MB
    :type ContainerMemoryMB: int
    :param ContainerMemoryPolicy: The container memory policy
    :type ContainerMemoryPolicy: ContainerMemoryPolicy
    :param ContainerSwapMB: The container swap in MB
    :type ContainerSwapMB: int
    :param DeploymentArgs: The deployment arguments
    :type DeploymentArgs: dict[str, str]
    :param Description: The description
    :type Description: str
    :param DiskUsageMB: The disk usage in MB
    :type DiskUsageMB: int
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param InstanceID: The instance ID
    :type InstanceID: str
    :param InstanceName: The instance name
    :type InstanceName: str
    :param WelcomeMessage: The instance's welcome message
    :type WelcomeMessage: str
    :param ManagementMode: The management mode
    :type ManagementMode: ManagementModes
    :param Metrics: The metrics
    :type Metrics: dict[str, MetricInfo]
    :param ModuleDisplayName: The module display name
    :type ModuleDisplayName: str
    :param Module: The module
    :type Module: str
    :param Port: The port
    :type Port: int
    :param ReleaseStream: The release stream
    :type ReleaseStream: AMPReleaseStreams
    :param SpecificDockerImage: The specific Docker image
    :type SpecificDockerImage: str
    :param Tags: The tags
    :type Tags: list[str]
    :param TargetID: The target ID
    :type TargetID: str
    :param IsHTTPS: Whether HTTPS is enabled
    :type IsHTTPS: bool
    :param UseHostModeNetwork: Whether the container uses host mode network
    :type UseHostModeNetwork: bool
    :param DaemonAutostart: Whether the instance daemon autostarts
    :type DaemonAutostart: bool
    :param IsContainerInstance: Whether the instance is a container instance
    :type IsContainerInstance: bool
    :param Daemon: Whether the instance is a daemon
    :type Daemon: bool
    :param ExcludeFromFirewall: Whether the instance is excluded from the firewall
    :type ExcludeFromFirewall: bool
    :param Running: Whether the instance is running
    :type Running: bool
    :param Suspended: Whether the instance is suspended
    :type Suspended: bool
    """
    AMPVersion: 'Version' = None
    IP: 'str' = ""
    ApplicationEndpoints: 'list[EndpointInfo]' = field(default_factory=list)
    AppState: 'ApplicationState' = None
    ContainerCPUs: 'float' = 0.0
    ContainerMemoryMB: 'int' = 0
    ContainerMemoryPolicy: 'ContainerMemoryPolicy' = None
    ContainerSwapMB: 'int' = 0
    DeploymentArgs: 'dict[str, str]' = field(default_factory=dict)
    Description: 'str' = ""
    DiskUsageMB: 'int' = 0
    DisplayImageSource: 'str' = ""
    FriendlyName: 'str' = ""
    InstanceID: 'str' = ""
    InstanceName: 'str' = ""
    WelcomeMessage: 'str' = ""
    ManagementMode: 'ManagementModes' = None
    Metrics: 'dict[str, MetricInfo]' = field(default_factory=dict)
    ModuleDisplayName: 'str' = ""
    Module: 'str' = ""
    Port: 'int' = 0
    ReleaseStream: 'AMPReleaseStreams' = None
    SpecificDockerImage: 'str' = ""
    Tags: 'list[str]' = field(default_factory=list)
    TargetID: 'str' = ""
    IsHTTPS: 'bool' = False
    UseHostModeNetwork: 'bool' = False
    DaemonAutostart: 'bool' = False
    IsContainerInstance: 'bool' = False
    Daemon: 'bool' = False
    ExcludeFromFirewall: 'bool' = False
    Running: 'bool' = False
    Suspended: 'bool' = False

@dataclass
class IPermissionsTreeNode:
    """
    A permissions tree node
    :param Children: The children
    :type Children: list[IPermissionsTreeNode]
    :param Description: The description
    :type Description: str
    :param DisplayName: The display name
    :type DisplayName: str
    :param Name: The name
    :type Name: str
    :param Node: The node
    :type Node: str
    """
    Children: 'list[IPermissionsTreeNode]' = field(default_factory=list)
    Description: 'str' = ""
    DisplayName: 'str' = ""
    Name: 'str' = ""
    Node: 'str' = ""

@dataclass
class IPlatformInfo:
    """
    Platform information object
    :param CPUInfo: The CPU information object
    :type CPUInfo: ProcessorInfo
    :param OS: The OS
    :type OS: SupportedOS
    :param InstalledRAMMB: The installed RAM in MB
    :type InstalledRAMMB: int
    :param PlatformName: The platform name
    :type PlatformName: str
    :param SystemType: The system type
    :type SystemType: Architecture
    :param Virtualization: The virtualization type
    :type Virtualization: VirtualizationType
    :param DockerNetworkIsHostMode: Whether the Docker network is in host mode
    :type DockerNetworkIsHostMode: bool
    """
    CPUInfo: 'ProcessorInfo' = None
    OS: 'SupportedOS' = None
    InstalledRAMMB: 'int' = 0
    PlatformName: 'str' = ""
    SystemType: 'Architecture' = None
    Virtualization: 'VirtualizationType' = None
    DockerNetworkIsHostMode: 'bool' = False

@dataclass
class LicenceInfo:
    """
    A struct to represent the object returned by Core#ActivateAMPLicence(Guid, Boolean)
    :param Expires: The expiry date
    :type Expires: str
    :param GradeName: The grade name
    :type GradeName: str
    :param Grade: The grade
    :type Grade: str
    :param LicenceKey: The licence key
    :type LicenceKey: str
    :param ProductName: The product name
    :type ProductName: str
    :param Product: The product
    :type Product: str
    :param Usage: The usage
    :type Usage: int
    """
    Expires: 'str' = ""
    GradeName: 'str' = ""
    Grade: 'str' = ""
    LicenceKey: 'str' = ""
    ProductName: 'str' = ""
    Product: 'str' = ""
    Usage: 'int' = 0

@dataclass
class ListeningPortSummary:
    """
    A listening port object
    :param Name: The name
    :type Name: str
    :param Port: The port
    :type Port: int
    :param Protocol: The protocol
    :type Protocol: PortProtocol
    :param IsDelayedOpen: Whether the port is delayed open
    :type IsDelayedOpen: bool
    :param Listening: Whether the port is listening
    :type Listening: bool
    :param Required: Whether the port is required
    :type Required: bool
    """
    Name: 'str' = ""
    Port: 'int' = 0
    Protocol: 'PortProtocol' = None
    IsDelayedOpen: 'bool' = False
    Listening: 'bool' = False
    Required: 'bool' = False

@dataclass
class LocalAMPInstance:
    """
    A local AMP instance object
    :param AMPBuild: The AMP build
    :type AMPBuild: str
    :param AMPVersion: The AMP version
    :type AMPVersion: Version
    :param IP: The IP
    :type IP: str
    :param OS: The OS
    :type OS: SupportedOS
    :param ContainerCPUs: The container CPUs
    :type ContainerCPUs: float
    :param ContainerMemoryMB: The container memory in MB
    :type ContainerMemoryMB: int
    :param ContainerMemoryPolicy: The container memory policy
    :type ContainerMemoryPolicy: ContainerMemoryPolicy
    :param ContainerSwapMB: The container swap in MB
    :type ContainerSwapMB: int
    :param CreatedBy: The creator ID
    :type CreatedBy: str
    :param CustomMountBinds: The custom mount binds
    :type CustomMountBinds: dict[str, str]
    :param CustomPorts: The custom ports
    :type CustomPorts: list[PortUsage]
    :param DatastoreId: The datastore ID
    :type DatastoreId: int
    :param DeploymentArgs: The deployment arguments
    :type DeploymentArgs: dict[str, str]
    :param Description: The description
    :type Description: str
    :param DiskUsageMB: The disk usage in MB
    :type DiskUsageMB: int
    :param DisplayImageSource: The display image source
    :type DisplayImageSource: str
    :param ExtraContainerPackages: The extra container packages
    :type ExtraContainerPackages: list[str]
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param Group: The group
    :type Group: str
    :param InstanceID: The instance ID
    :type InstanceID: str
    :param InstanceName: The instance name
    :type InstanceName: str
    :param LastReactivationAttempt: The last reactivation attempt
    :type LastReactivationAttempt: str | None
    :param ManagementMode: The management mode
    :type ManagementMode: ManagementModes
    :param MetricsPublishingHMAC: The metrics publishing HMAC
    :type MetricsPublishingHMAC: str
    :param ModuleDisplayName: The module display name
    :type ModuleDisplayName: str
    :param Module: The module
    :type Module: str
    :param OverlayURL: The overlay URL
    :type OverlayURL: str
    :param OverlayPath: The overlay path
    :type OverlayPath: str
    :param Path: The path
    :type Path: str
    :param PendingSettingChanges: The pending setting changes
    :type PendingSettingChanges: dict[str, str]
    :param Plugins: The plugins
    :type Plugins: list[str]
    :param Port: The port
    :type Port: int
    :param PreviousBuild: The previous build
    :type PreviousBuild: str
    :param PreviousVersion: The previous version
    :type PreviousVersion: Version
    :param ReleaseStream: The release stream
    :type ReleaseStream: AMPReleaseStreams
    :param SpecificDockerImage: The specific Docker image
    :type SpecificDockerImage: str
    :param Tag: The tag
    :type Tag: str
    :param Tags: The tags
    :type Tags: list[str]
    :param TargetID: The target ID
    :type TargetID: str
    :param User: The user
    :type User: str
    :param WelcomeMessage: The welcome message
    :type WelcomeMessage: str
    :param TagsUsedForConfiguration: Whether tags are used for configuration
    :type TagsUsedForConfiguration: bool
    :param DockerBaseReadOnly: Whether the Docker base is read-only
    :type DockerBaseReadOnly: bool
    :param DaemonAutostart: Whether the daemon should autostart
    :type DaemonAutostart: bool
    :param HasOverlayApplied: Whether the instance has an overlay applied
    :type HasOverlayApplied: bool
    :param IsHTTPS: Whether the instance is HTTPS
    :type IsHTTPS: bool
    :param IsContainerInstance: Whether the instance is a container
    :type IsContainerInstance: bool
    :param IsDaemonUserManaged: Whether the instance is a daemon user managed
    :type IsDaemonUserManaged: bool
    :param Daemon: Whether the instance is a daemon
    :type Daemon: bool
    :param IsSharedInstance: Whether the instance is a shared instance
    :type IsSharedInstance: bool
    :param Suspended: Whether the instance is suspended
    :type Suspended: bool
    :param ExcludeFromFirewall: Whether to exclude from the firewall
    :type ExcludeFromFirewall: bool
    :param ForceDocker: Whether to force Docker
    :type ForceDocker: bool
    :param MatchVersion: Whether to match the version
    :type MatchVersion: bool
    :param AutomaticUPnP: Whether to use automatic UPnP
    :type AutomaticUPnP: bool
    :param UseHostModeNetwork: Whether to use host mode networking
    :type UseHostModeNetwork: bool
    """
    AMPBuild: 'str' = ""
    AMPVersion: 'Version' = None
    IP: 'str' = ""
    OS: 'SupportedOS' = None
    ContainerCPUs: 'float' = 0.0
    ContainerMemoryMB: 'int' = 0
    ContainerMemoryPolicy: 'ContainerMemoryPolicy' = None
    ContainerSwapMB: 'int' = 0
    CreatedBy: 'str' = ""
    CustomMountBinds: 'dict[str, str]' = field(default_factory=dict)
    CustomPorts: 'list[PortUsage]' = field(default_factory=list)
    DatastoreId: 'int' = 0
    DeploymentArgs: 'dict[str, str]' = field(default_factory=dict)
    Description: 'str' = ""
    DiskUsageMB: 'int' = 0
    DisplayImageSource: 'str' = ""
    ExtraContainerPackages: 'list[str]' = field(default_factory=list)
    FriendlyName: 'str' = ""
    Group: 'str' = ""
    InstanceID: 'str' = ""
    InstanceName: 'str' = ""
    LastReactivationAttempt: 'str | None' = None
    ManagementMode: 'ManagementModes' = None
    MetricsPublishingHMAC: 'str' = ""
    ModuleDisplayName: 'str' = ""
    Module: 'str' = ""
    OverlayURL: 'str' = ""
    OverlayPath: 'str' = ""
    Path: 'str' = ""
    PendingSettingChanges: 'dict[str, str]' = field(default_factory=dict)
    Plugins: 'list[str]' = field(default_factory=list)
    Port: 'int' = 0
    PreviousBuild: 'str' = ""
    PreviousVersion: 'Version' = None
    ReleaseStream: 'AMPReleaseStreams' = None
    SpecificDockerImage: 'str' = ""
    Tag: 'str' = ""
    Tags: 'list[str]' = field(default_factory=list)
    TargetID: 'str' = ""
    User: 'str' = ""
    WelcomeMessage: 'str' = ""
    TagsUsedForConfiguration: 'bool' = False
    DockerBaseReadOnly: 'bool' = False
    DaemonAutostart: 'bool' = False
    HasOverlayApplied: 'bool' = False
    IsHTTPS: 'bool' = False
    IsContainerInstance: 'bool' = False
    IsDaemonUserManaged: 'bool' = False
    Daemon: 'bool' = False
    IsSharedInstance: 'bool' = False
    Suspended: 'bool' = False
    ExcludeFromFirewall: 'bool' = False
    ForceDocker: 'bool' = False
    MatchVersion: 'bool' = False
    AutomaticUPnP: 'bool' = False
    UseHostModeNetwork: 'bool' = False

@dataclass
class LoginResponse:
    """
    Type for the result of Core.Login
    :param permissions: The permissions
    :type permissions: list[str]
    :param rememberMeToken: The remember me token
    :type rememberMeToken: str
    :param resultReason: The result reason
    :type resultReason: str
    :param result: The result
    :type result: AuthenticationResult
    :param sessionID: The session ID
    :type sessionID: str
    :param userInfo: The user info
    :type userInfo: UserInfoSummary
    :param success: Whether the login was successful
    :type success: bool
    """
    permissions: 'list[str]' = field(default_factory=list)
    rememberMeToken: 'str' = ""
    resultReason: 'str' = ""
    result: 'AuthenticationResult' = None
    sessionID: 'str' = ""
    userInfo: 'UserInfoSummary' = None
    success: 'bool' = False

class ManagementModes(Enum):
    """
    Represents the management modes
    :param Standalone: Standalone
    :type Standalone: Int32
    :param ViaADS: Via ADS
    :type ViaADS: Int32
    """
    Standalone = 0
    ViaADS = 10

@dataclass
class MethodInfoSummary:
    """
    A summary of a method
    :param Description: The description
    :type Description: str
    :param Parameters: The parameters
    :type Parameters: list[MethodParameterSummary]
    :param ReturnTypeName: The return type name
    :type ReturnTypeName: str
    :param Returns: The methods return value (deprecated)
    :type Returns: str | None
    :param IsComplexType: Whether the method is a complex type
    :type IsComplexType: bool
    """
    Description: 'str' = ""
    Parameters: 'list[MethodParameterSummary]' = field(default_factory=list)
    ReturnTypeName: 'str' = ""
    Returns: 'str | None' = None
    IsComplexType: 'bool' = False

@dataclass
class MethodParameterSummary:
    """
    A summary of a method parameter
    :param Description: The description
    :type Description: str
    :param Name: The name
    :type Name: str
    :param ParamEnumValues: The parameter enum values
    :type ParamEnumValues: dict[str, Any] | None
    :param TypeName: The type name
    :type TypeName: str
    :param Optional: Whether the parameter is optional
    :type Optional: bool
    """
    Description: 'str' = ""
    Name: 'str' = ""
    ParamEnumValues: 'dict[str, Any] | None' = field(default_factory=dict)
    TypeName: 'str' = ""
    Optional: 'bool' = False

@dataclass
class MetricInfo:
    """
    A metric info object
    :param Color: The color
    :type Color: str
    :param MaxValue: The maximum value
    :type MaxValue: int
    :param Percent: The percentage
    :type Percent: int
    :param RawValue: The raw value
    :type RawValue: int
    :param Color2: The second color
    :type Color2: str
    :param ShortName: The short name
    :type ShortName: str
    :param Color3: The third color
    :type Color3: str
    :param Units: The units
    :type Units: str
    """
    Color: 'str' = ""
    MaxValue: 'int' = 0
    Percent: 'int' = 0
    RawValue: 'int' = 0
    Color2: 'str' = ""
    ShortName: 'str' = ""
    Color3: 'str' = ""
    Units: 'str' = ""

@dataclass
class ModuleInfo:
    """
    A struct to represent the object returned by the Core.GetModuleInfo() method
    :param AMPBuild: The AMP build
    :type AMPBuild: str
    :param AMPVersion: The AMP version
    :type AMPVersion: str
    :param APIVersion: The API version
    :type APIVersion: str
    :param AppName: The application name
    :type AppName: str
    :param Author: The author of the module
    :type Author: str
    :param BasePort: The base port
    :type BasePort: int
    :param Branding: The branding object
    :type Branding: BrandingSettings
    :param BuildSpec: The build spec
    :type BuildSpec: str
    :param DisplayBaseURI: The display base URI
    :type DisplayBaseURI: str
    :param EndpointURI: The endpoint URI
    :type EndpointURI: str
    :param FeatureSet: The feature set
    :type FeatureSet: list[str]
    :param FriendlyName: The friendly name
    :type FriendlyName: str
    :param InstanceId: The instance ID
    :type InstanceId: str
    :param InstanceName: The instance name
    :type InstanceName: str
    :param LoadedPlugins: The loaded plugins
    :type LoadedPlugins: list[str]
    :param ModuleName: The module name
    :type ModuleName: str
    :param Name: The name of the module
    :type Name: str
    :param PrimaryEndpoint: The primary endpoint
    :type PrimaryEndpoint: str
    :param Timestamp: The timestamp
    :type Timestamp: str
    :param ToolsVersion: The tools version
    :type ToolsVersion: str
    :param VersionCodename: The version codename
    :type VersionCodename: str
    :param Analytics: Whether analytics are enabled
    :type Analytics: bool
    :param AllowRememberMe: Whether remember me is allowed
    :type AllowRememberMe: bool
    :param IsRemoteInstance: Whether the instance is remote
    :type IsRemoteInstance: bool
    :param RequiresFullLoad: Whether the module requires a full load
    :type RequiresFullLoad: bool
    :param SupportsSleep: Whether the module supports sleep mode
    :type SupportsSleep: bool
    """
    AMPBuild: 'str' = ""
    AMPVersion: 'str' = ""
    APIVersion: 'str' = ""
    AppName: 'str' = ""
    Author: 'str' = ""
    BasePort: 'int' = 0
    Branding: 'BrandingSettings' = None
    BuildSpec: 'str' = ""
    DisplayBaseURI: 'str' = ""
    EndpointURI: 'str' = ""
    FeatureSet: 'list[str]' = field(default_factory=list)
    FriendlyName: 'str' = ""
    InstanceId: 'str' = ""
    InstanceName: 'str' = ""
    LoadedPlugins: 'list[str]' = field(default_factory=list)
    ModuleName: 'str' = ""
    Name: 'str' = ""
    PrimaryEndpoint: 'str' = ""
    Timestamp: 'str' = ""
    ToolsVersion: 'str' = ""
    VersionCodename: 'str' = ""
    Analytics: 'bool' = False
    AllowRememberMe: 'bool' = False
    IsRemoteInstance: 'bool' = False
    RequiresFullLoad: 'bool' = False
    SupportsSleep: 'bool' = False

@dataclass
class OPEntry:
    """
    An OP entry
    :param UUID: The UUID
    :type UUID: str
    :param Level: The level
    :type Level: int
    :param Name: The name
    :type Name: str
    """
    UUID: 'str' = ""
    Level: 'int' = 0
    Name: 'str' = ""

class PortProtocol(Enum):
    """
    Represents the port protocol
    :param TCP: TCP
    :type TCP: Int32
    :param UDP: UDP
    :type UDP: Int32
    :param Both: Both
    :type Both: Int32
    """
    TCP = 0
    UDP = 1
    Both = 2

@dataclass
class PortSummary:
    """
    A port object
    :param Name: The name
    :type Name: str
    :param Port: The port
    :type Port: int
    :param Protocol: The protocol
    :type Protocol: PortProtocol
    :param IsDelayedOpen: Whether the port is delayed open
    :type IsDelayedOpen: bool
    :param Required: Whether the port is required
    :type Required: bool
    """
    Name: 'str' = ""
    Port: 'int' = 0
    Protocol: 'PortProtocol' = None
    IsDelayedOpen: 'bool' = False
    Required: 'bool' = False

@dataclass
class PortUsage:
    """
    A port usage object
    :param Description: The description
    :type Description: str
    :param PortNumber: The port number
    :type PortNumber: int
    :param Protocol: The protocol
    :type Protocol: PortProtocol
    :param ProvisionNodeName: The provision node name
    :type ProvisionNodeName: str
    :param Range: The range
    :type Range: int
    :param IsUserDefined: Whether the port is user-defined
    :type IsUserDefined: bool
    :param Verified: Whether the port is verified
    :type Verified: bool
    """
    Description: 'str' = ""
    PortNumber: 'int' = 0
    Protocol: 'PortProtocol' = None
    ProvisionNodeName: 'str' = ""
    Range: 'int' = 0
    IsUserDefined: 'bool' = False
    Verified: 'bool' = False

class PostCreateAppActions(Enum):
    """
    Represents the post create app actions
    :param DoNothing: Do nothing
    :type DoNothing: Int32
    :param UpdateOnce: Update once
    :type UpdateOnce: Int32
    :param UpdateAlways: Update always
    :type UpdateAlways: Int32
    :param UpdateAndStartOnce: Update and start once
    :type UpdateAndStartOnce: Int32
    :param UpdateAndStartAlways: Update and start always
    :type UpdateAndStartAlways: Int32
    :param StartAlways: Start always
    :type StartAlways: Int32
    """
    DoNothing = 0
    UpdateOnce = 1
    UpdateAlways = 2
    UpdateAndStartOnce = 3
    UpdateAndStartAlways = 4
    StartAlways = 5

@dataclass
class ProcessorInfo:
    """
    CPU information object
    :param ModelName: CPU model name
    :type ModelName: str
    :param Vendor: CPU vendor
    :type Vendor: str
    :param Cores: Number of CPU cores
    :type Cores: int
    :param Sockets: Number of CPU sockets
    :type Sockets: int
    :param Threads: Number of CPU threads
    :type Threads: int
    :param TotalCores: Total number of CPU cores
    :type TotalCores: int
    :param TotalThreads: Total number of CPU threads
    :type TotalThreads: int
    """
    ModelName: 'str' = ""
    Vendor: 'str' = ""
    Cores: 'int' = 0
    Sockets: 'int' = 0
    Threads: 'int' = 0
    TotalCores: 'int' = 0
    TotalThreads: 'int' = 0

@dataclass
class ProvisionFitness:
    """
    Fitness information object
    :param Available: Availability
    :type Available: bool
    :param CPUServiceRatio: CPU service ratio
    :type CPUServiceRatio: float
    :param Score: Fitness score
    :type Score: float
    :param LoadAvg: Load average
    :type LoadAvg: float
    :param RemainingInstanceSlots: Remaining instance slots
    :type RemainingInstanceSlots: int
    :param TotalServices: Service count
    :type TotalServices: int
    :param ThreadQueueLength: Thread queue length
    :type ThreadQueueLength: int
    :param FreeRAMMB: Unallocated RAM in MB
    :type FreeRAMMB: int
    :param FreeDiskMB: Unallocated disk space in MB
    :type FreeDiskMB: int
    """
    Available: 'bool' = False
    CPUServiceRatio: 'float' = 0.0
    Score: 'float' = 0.0
    LoadAvg: 'float' = 0.0
    RemainingInstanceSlots: 'int' = 0
    TotalServices: 'int' = 0
    ThreadQueueLength: 'int' = 0
    FreeRAMMB: 'int' = 0
    FreeDiskMB: 'int' = 0

@dataclass
class ProvisionSettingInfo:
    """
    A provision setting object
    :param CustomFieldType: The custom field type
    :type CustomFieldType: str
    :param DefaultValue: The default value
    :type DefaultValue: Any
    :param Description: The description
    :type Description: str
    :param EndpointFormat: The endpoint format
    :type EndpointFormat: str
    :param EndpointName: The endpoint name
    :type EndpointName: str
    :param Node: The node
    :type Node: str
    :param RelatedSetting: The related setting
    :type RelatedSetting: str
    :param Type: The type
    :type Type: str
    :param ValueRange: The value range
    :type ValueRange: int
    """
    CustomFieldType: 'str' = ""
    DefaultValue: 'Any' = None
    Description: 'str' = ""
    EndpointFormat: 'str' = ""
    EndpointName: 'str' = ""
    Node: 'str' = ""
    RelatedSetting: 'str' = ""
    Type: 'str' = ""
    ValueRange: 'int' = 0

@dataclass
class PushedMessage:
    """
    Type for API.Core.GetUpdates#Messages[i] (along with WS keep alive)
    :param AgeMinutes: The age of the message in minutes
    :type AgeMinutes: int
    :param Id: The message ID
    :type Id: str
    :param Message: The message
    :type Message: str
    :param Source: The source of the message
    :type Source: str
    :param Expired: Whether the message has expired
    :type Expired: bool
    """
    AgeMinutes: 'int' = 0
    Id: 'str' = ""
    Message: 'str' = ""
    Source: 'str' = ""
    Expired: 'bool' = False

class RemoteInstanceState(Enum):
    """
    Represents the state of a remote instance
    :param Pending: Pending
    :type Pending: Int32
    :param Connecting: Connecting
    :type Connecting: Int32
    :param Offline: Offline
    :type Offline: Int32
    :param Unavailable: Unavailable
    :type Unavailable: Int32
    :param AuthFailure: Authentication failure
    :type AuthFailure: Int32
    :param Online: Online
    :type Online: Int32
    :param Disabled: Disabled
    :type Disabled: Int32
    :param UpdateInProgress: Update in progress
    :type UpdateInProgress: Int32
    """
    Pending = 0
    Connecting = 5
    Offline = 10
    Unavailable = 15
    AuthFailure = 16
    Online = 20
    Disabled = 30
    UpdateInProgress = 100

@dataclass
class RemoteTargetInfo:
    """
    Information about a remote target, returned by ADSModule#GetTargetInfo()
    :param IPAddressList: The IP address list
    :type IPAddressList: list[str]
    :param Datastores: The datastores
    :type Datastores: list[DatastoreSummary]
    :param PlatformInfo: The remote target's platform info
    :type PlatformInfo: IPlatformInfo
    :param DeploysInContainers: Whether the target deploys in containers
    :type DeploysInContainers: bool
    """
    IPAddressList: 'list[str]' = field(default_factory=list)
    Datastores: 'list[DatastoreSummary]' = field(default_factory=list)
    PlatformInfo: 'IPlatformInfo' = None
    DeploysInContainers: 'bool' = False

@dataclass
class RunningTask:
    """
    A running task object
    :param Description: The description
    :type Description: str
    :param EndTime: The end time
    :type EndTime: str | None
    :param LastUpdatePushed: The last update pushed
    :type LastUpdatePushed: str
    :param Name: The name
    :type Name: str
    :param Origin: The origin
    :type Origin: str
    :param ParentTaskId: The parent task ID
    :type ParentTaskId: str | None
    :param ProgressPercent: The progress percentage
    :type ProgressPercent: int
    :param RemoteInstanceId: The remote instance ID
    :type RemoteInstanceId: str | None
    :param Speed: The speed
    :type Speed: str
    :param StartTime: The start time
    :type StartTime: str
    :param StateMessage: The state message
    :type StateMessage: str
    :param State: The state
    :type State: TaskState
    :param Id: The task ID
    :type Id: str
    :param FastDismiss: Whether the task can be dismissed quickly
    :type FastDismiss: bool
    :param IsCancellable: Whether the task is cancellable
    :type IsCancellable: bool
    :param HideFromUI: Whether the task is hidden from the UI
    :type HideFromUI: bool
    :param IsIndeterminate: Whether the task is indeterminate
    :type IsIndeterminate: bool
    :param IsPrimaryTask: Whether the task is primary
    :type IsPrimaryTask: bool
    :param DontPropagate: Whether the task should not propagate
    :type DontPropagate: bool
    """
    Description: 'str' = ""
    EndTime: 'str | None' = None
    LastUpdatePushed: 'str' = ""
    Name: 'str' = ""
    Origin: 'str' = ""
    ParentTaskId: 'str | None' = None
    ProgressPercent: 'int' = 0
    RemoteInstanceId: 'str | None' = None
    Speed: 'str' = ""
    StartTime: 'str' = ""
    StateMessage: 'str' = ""
    State: 'TaskState' = None
    Id: 'str' = ""
    FastDismiss: 'bool' = False
    IsCancellable: 'bool' = False
    HideFromUI: 'bool' = False
    IsIndeterminate: 'bool' = False
    IsPrimaryTask: 'bool' = False
    DontPropagate: 'bool' = False

class ScheduleEnabledState(Enum):
    """
    Represents the schedule enabled state
    :param Disabled: Disabled
    :type Disabled: Int32
    :param Enabled: Enabled
    :type Enabled: Int32
    :param RunOnce: Run once
    :type RunOnce: Int32
    :param DeleteOnRun: Delete on run
    :type DeleteOnRun: Int32
    """
    Disabled = 0
    Enabled = 1
    RunOnce = 2
    DeleteOnRun = 4

@dataclass
class ScheduleEntryDefinition:
    """
    A schedule entry definition
    :param Id: The ID
    :type Id: str
    :param CreatedBy: The creator
    :type CreatedBy: str | None
    :param EnabledState: The enabled state
    :type EnabledState: ScheduleEnabledState
    :param ErrorBehaviour: The error behaviour
    :type ErrorBehaviour: ScheduleErrorBehaviour
    :param LastErrorReason: The last error reason
    :type LastErrorReason: str
    :param Order: The order
    :type Order: int
    :param ParameterMapping: The parameter mapping
    :type ParameterMapping: dict[str, str]
    :param TaskMethodName: The task method name
    :type TaskMethodName: str
    :param Locked: Whether the entry is locked
    :type Locked: bool
    :param LastExecuteError: Whether the last execution had an error
    :type LastExecuteError: bool
    :param WaitForComplete: Whether to wait for completion
    :type WaitForComplete: bool
    """
    Id: 'str' = ""
    CreatedBy: 'str | None' = None
    EnabledState: 'ScheduleEnabledState' = None
    ErrorBehaviour: 'ScheduleErrorBehaviour' = None
    LastErrorReason: 'str' = ""
    Order: 'int' = 0
    ParameterMapping: 'dict[str, str]' = field(default_factory=dict)
    TaskMethodName: 'str' = ""
    Locked: 'bool' = False
    LastExecuteError: 'bool' = False
    WaitForComplete: 'bool' = False

class ScheduleErrorBehaviour(Enum):
    """
    Represents the schedule error behaviour
    :param Normal: Normal
    :type Normal: Int32
    :param ContinueSilently: Continue silently
    :type ContinueSilently: Int32
    """
    Normal = 0
    ContinueSilently = 1

@dataclass
class ScheduleInfo:
    """
    Information about a schedule
    :param AvailableMethods: The available methods
    :type AvailableMethods: list[APIMethodInfo]
    :param AvailableTriggers: The available triggers
    :type AvailableTriggers: list[TriggerInfo]
    :param PopulatedTriggers: The populated triggers
    :type PopulatedTriggers: list[TriggerInfo]
    """
    AvailableMethods: 'list[APIMethodInfo]' = field(default_factory=list)
    AvailableTriggers: 'list[TriggerInfo]' = field(default_factory=list)
    PopulatedTriggers: 'list[TriggerInfo]' = field(default_factory=list)

@dataclass
class ScheduleTaskParameter:
    """
    A parameter for a scheduled task
    :param Description: The description
    :type Description: str
    :param DisplayName: The display name
    :type DisplayName: str
    :param EnumValues: The enum values
    :type EnumValues: dict[str, str] | None
    :param InputType: The input type
    :type InputType: str
    :param Name: The name
    :type Name: str
    :param SelectionSource: The selection source
    :type SelectionSource: StringSelectionSourceAttribute
    :param ValueType: The value type
    :type ValueType: str
    """
    Description: 'str' = ""
    DisplayName: 'str' = ""
    EnumValues: 'dict[str, str] | None' = field(default_factory=dict)
    InputType: 'str' = ""
    Name: 'str' = ""
    SelectionSource: 'StringSelectionSourceAttribute' = None
    ValueType: 'str' = ""

@dataclass
class ScheduleTrigger:
    """
    A time interval trigger
    :param Id: The ID
    :type Id: str
    :param Description: The description
    :type Description: str
    :param EnabledState: The enabled state
    :type EnabledState: ScheduleEnabledState
    :param LastExecuted: The last executed
    :type LastExecuted: str | None
    :param Name: The name
    :type Name: str
    :param Order: The order
    :type Order: int
    """
    Id: 'str' = ""
    Description: 'str' = ""
    EnabledState: 'ScheduleEnabledState' = None
    LastExecuted: 'str | None' = None
    Name: 'str' = ""
    Order: 'int' = 0

@dataclass
class SecurityCheckResult:
    """
    A security check result
    :param Description: The description
    :type Description: str
    :param Resolution: The resolution
    :type Resolution: str
    :param Severity: The severity
    :type Severity: int
    :param Title: The title
    :type Title: str
    :param Hidden: Whether the check is hidden
    :type Hidden: bool
    :param Pass: Whether the check passed
    :type Pass: bool
    """
    Description: 'str' = ""
    Resolution: 'str' = ""
    Severity: 'int' = 0
    Title: 'str' = ""
    Hidden: 'bool' = False
    Pass: 'bool' = False

@dataclass
class SettingSpec:
    """
    A setting specification object
    :param Actions: The actions
    :type Actions: list[InlineActionAttribute]
    :param Attributes: The attributes
    :type Attributes: Any
    :param Category: The category
    :type Category: str
    :param CurrentValue: The current value
    :type CurrentValue: Any
    :param Description: The description
    :type Description: str
    :param EnumValues: The enum values
    :type EnumValues: dict[str, str] | None
    :param InputType: The input type
    :type InputType: str
    :param Keywords: The keywords
    :type Keywords: str
    :param MaxLength: The max length
    :type MaxLength: int
    :param MaxValue: The max value
    :type MaxValue: float | None
    :param Meta: The meta
    :type Meta: str
    :param MinValue: The min value
    :type MinValue: float | None
    :param Name: The name
    :type Name: str
    :param Node: The node
    :type Node: str
    :param Order: The order
    :type Order: int
    :param Placeholder: The placeholder
    :type Placeholder: str
    :param SelectionSource: The selection source
    :type SelectionSource: StringSelectionSourceAttribute
    :param Subcategory: The subcategory
    :type Subcategory: str
    :param Suffix: The suffix
    :type Suffix: str
    :param Tag: The tag
    :type Tag: str
    :param ValType: The value type
    :type ValType: str
    :param EnumValuesAreDeferred: Whether the enum values are deferred
    :type EnumValuesAreDeferred: bool
    :param ReadOnlyProvision: Whether the provision is read-only
    :type ReadOnlyProvision: bool
    :param IsProvisionSpec: Whether the setting is a provision spec
    :type IsProvisionSpec: bool
    :param AlwaysAllowRead: Whether the setting is always allowed to be read
    :type AlwaysAllowRead: bool
    :param ReadOnly: Whether the setting is read-only
    :type ReadOnly: bool
    :param Required: Whether the setting is required
    :type Required: bool
    :param RequiresRestart: Whether the setting requires a restart
    :type RequiresRestart: bool
    """
    Actions: 'list[InlineActionAttribute]' = field(default_factory=list)
    Attributes: 'Any' = None
    Category: 'str' = ""
    CurrentValue: 'Any' = None
    Description: 'str' = ""
    EnumValues: 'dict[str, str] | None' = field(default_factory=dict)
    InputType: 'str' = ""
    Keywords: 'str' = ""
    MaxLength: 'int' = 0
    MaxValue: 'float | None' = None
    Meta: 'str' = ""
    MinValue: 'float | None' = None
    Name: 'str' = ""
    Node: 'str' = ""
    Order: 'int' = 0
    Placeholder: 'str' = ""
    SelectionSource: 'StringSelectionSourceAttribute' = None
    Subcategory: 'str' = ""
    Suffix: 'str' = ""
    Tag: 'str' = ""
    ValType: 'str' = ""
    EnumValuesAreDeferred: 'bool' = False
    ReadOnlyProvision: 'bool' = False
    IsProvisionSpec: 'bool' = False
    AlwaysAllowRead: 'bool' = False
    ReadOnly: 'bool' = False
    Required: 'bool' = False
    RequiresRestart: 'bool' = False

@dataclass
class SimpleUser:
    """
    A simple user object
    :param Id: The ID
    :type Id: str
    :param IPAddress: The IP address
    :type IPAddress: str
    :param UID: The UID
    :type UID: str
    :param JoinTime: The join time
    :type JoinTime: str
    :param Name: The name
    :type Name: str
    :param Port: The port
    :type Port: int
    :param SessionID: The session ID
    :type SessionID: str
    :param Tags: The tags
    :type Tags: list[str]
    :param TimeLoggedIn: The time logged in
    :type TimeLoggedIn: str
    :param UserSessionId: The user session ID
    :type UserSessionId: str
    """
    Id: 'str' = ""
    IPAddress: 'str' = ""
    UID: 'str' = ""
    JoinTime: 'str' = ""
    Name: 'str' = ""
    Port: 'int' = 0
    SessionID: 'str' = ""
    Tags: 'list[str]' = field(default_factory=list)
    TimeLoggedIn: 'str' = ""
    UserSessionId: 'str' = ""

@dataclass
class StatusResponse:
    """
    Type for the result of Core.GetStatus
    :param Metrics: The metrics
    :type Metrics: dict[str, MetricInfo]
    :param State: The state of the instance
    :type State: ApplicationState
    :param Uptime: The uptime of the instance
    :type Uptime: str
    """
    Metrics: 'dict[str, MetricInfo]' = field(default_factory=dict)
    State: 'ApplicationState' = None
    Uptime: 'str' = ""

@dataclass
class StringSelectionSourceAttribute:
    """
    A string selection source object
    :param Deferred: Whether the selection source is deferred
    :type Deferred: bool
    :param MustValidate: Whether the selection source must validate
    :type MustValidate: bool
    """
    Deferred: 'bool' = False
    MustValidate: 'bool' = False

class SupportedOS(Enum):
    """
    Represents the supported OS
    :param None_: None
    :type None_: Int32
    :param Windows: Windows
    :type Windows: Int32
    :param Linux: Linux
    :type Linux: Int32
    :param MacOS: MacOS
    :type MacOS: Int32
    :param BSD: BSD
    :type BSD: Int32
    :param Other: Other
    :type Other: Int32
    :param All: All
    :type All: Int32
    """
    None_ = 0
    Windows = 1
    Linux = 2
    MacOS = 4
    BSD = 8
    Other = 16
    All = 31

class TaskState(Enum):
    """
    Represents the state of a task
    :param Running: Running
    :type Running: Int32
    :param Waiting: Waiting
    :type Waiting: Int32
    :param Queued: Queued
    :type Queued: Int32
    :param Failed: Failed
    :type Failed: Int32
    :param Finished: Finished
    :type Finished: Int32
    :param PendingCancellation: Pending cancellation
    :type PendingCancellation: Int32
    :param Cancelled: Cancelled
    :type Cancelled: Int32
    :param Acknowledged: Acknowledged
    :type Acknowledged: Int32
    :param UserActionRequired: User action required
    :type UserActionRequired: Int32
    :param TimedOut: Timed out
    :type TimedOut: Int32
    """
    Running = 0
    Waiting = 1
    Queued = 2
    Failed = 3
    Finished = 4
    PendingCancellation = 5
    Cancelled = 6
    Acknowledged = 7
    UserActionRequired = 100
    TimedOut = 254

@dataclass
class TimeIntervalTrigger:
    """
    A time interval trigger
    :param Id: The ID
    :type Id: str
    :param Description: The description
    :type Description: str
    :param EnabledState: The enabled state
    :type EnabledState: ScheduleEnabledState
    :param LastExecuted: The last executed
    :type LastExecuted: str | None
    :param MatchDaysOfMonth: The match days of month
    :type MatchDaysOfMonth: list[int]
    :param MatchDays: The match days
    :type MatchDays: list[int]
    :param MatchHours: The match hours
    :type MatchHours: list[int]
    :param MatchMinutes: The match minutes
    :type MatchMinutes: list[int]
    :param MatchMonths: The match months
    :type MatchMonths: list[int]
    :param Name: The name
    :type Name: str
    :param Order: The order
    :type Order: int
    """
    Id: 'str' = ""
    Description: 'str' = ""
    EnabledState: 'ScheduleEnabledState' = None
    LastExecuted: 'str | None' = None
    MatchDaysOfMonth: 'list[int]' = field(default_factory=list)
    MatchDays: 'list[int]' = field(default_factory=list)
    MatchHours: 'list[int]' = field(default_factory=list)
    MatchMinutes: 'list[int]' = field(default_factory=list)
    MatchMonths: 'list[int]' = field(default_factory=list)
    Name: 'str' = ""
    Order: 'int' = 0

@dataclass
class TriggerInfo:
    """
    Information about a trigger
    :param Id: The ID
    :type Id: str
    :param Description: The description
    :type Description: str
    :param Emits: The emits
    :type Emits: list[str]
    :param EnabledState: The enabled state
    :type EnabledState: ScheduleEnabledState
    :param Tasks: The tasks
    :type Tasks: list[ScheduleEntryDefinition]
    :param TriggerType: The trigger type
    :type TriggerType: str
    :param Type: The type
    :type Type: str
    """
    Id: 'str' = ""
    Description: 'str' = ""
    Emits: 'list[str]' = field(default_factory=list)
    EnabledState: 'ScheduleEnabledState' = None
    Tasks: 'list[ScheduleEntryDefinition]' = field(default_factory=list)
    TriggerType: 'str' = ""
    Type: 'str' = ""

@dataclass
class TwoFactorSetupInfo:
    """
    Information about two-factor setup
    :param Url: The URL
    :type Url: str
    :param ManualKey: The manual key
    :type ManualKey: str
    """
    Url: 'str' = ""
    ManualKey: 'str' = ""

@dataclass
class UpdateInfo:
    """
    A struct to represent the object returned by the Core.GetUpdateInfo() method
    :param ReleaseNotesURL: The URL to the release notes
    :type ReleaseNotesURL: str
    :param Build: The build of the update
    :type Build: str
    :param ToolsVersion: The version of the tools
    :type ToolsVersion: str
    :param Version: The version of the update
    :type Version: str
    :param UpdateAvailable: Whether an update is available
    :type UpdateAvailable: bool
    :param PatchOnly: Whether the update is a patch
    :type PatchOnly: bool
    """
    ReleaseNotesURL: 'str' = ""
    Build: 'str' = ""
    ToolsVersion: 'str' = ""
    Version: 'str' = ""
    UpdateAvailable: 'bool' = False
    PatchOnly: 'bool' = False

@dataclass
class UpdateResponse:
    """
    Response type for Core.GetUpdates
    :param ConsoleEntries: The console entries of the server
    :type ConsoleEntries: list[ConsoleEntry]
    :param Messages: The messages of the server
    :type Messages: list[PushedMessage]
    :param Ports: The ports of the server
    :type Ports: list[ListeningPortSummary]
    :param Status: The status of the server
    :type Status: StatusResponse
    :param Tasks: The tasks of the server
    :type Tasks: list[RunningTask]
    """
    ConsoleEntries: 'list[ConsoleEntry]' = field(default_factory=list)
    Messages: 'list[PushedMessage]' = field(default_factory=list)
    Ports: 'list[ListeningPortSummary]' = field(default_factory=list)
    Status: 'StatusResponse' = None
    Tasks: 'list[RunningTask]' = field(default_factory=list)

@dataclass
class UserAccessData:
    """
    User access data
    :param OPList: The OP list
    :type OPList: list[OPEntry]
    :param Whitelist: The whitelist
    :type Whitelist: list[WhitelistEntry]
    """
    OPList: 'list[OPEntry]' = field(default_factory=list)
    Whitelist: 'list[WhitelistEntry]' = field(default_factory=list)

@dataclass
class UserInfo:
    """
    Information about a user
    :param ID: The ID
    :type ID: str
    :param AvatarBase64: The avatar base64
    :type AvatarBase64: str
    :param EmailAddress: The email address
    :type EmailAddress: str
    :param GravatarHash: The gravatar hash
    :type GravatarHash: str
    :param LastLogin: The last login
    :type LastLogin: str
    :param Name: The name
    :type Name: str
    :param Permissions: The permissions
    :type Permissions: list[str]
    :param Roles: The roles
    :type Roles: list[str]
    :param CannotChangePassword: Whether the password cannot be changed
    :type CannotChangePassword: bool
    :param PasswordExpires: Whether the password expires
    :type PasswordExpires: bool
    :param MustChangePassword: Whether the password must be changed
    :type MustChangePassword: bool
    :param IsSuperUser: Whether the user is a super user
    :type IsSuperUser: bool
    :param IsLDAPUser: Whether the user is an LDAP user
    :type IsLDAPUser: bool
    :param Disabled: Whether the user is disabled
    :type Disabled: bool
    :param IsTwoFactorEnabled: Whether two-factor is enabled
    :type IsTwoFactorEnabled: bool
    """
    ID: 'str' = ""
    AvatarBase64: 'str' = ""
    EmailAddress: 'str' = ""
    GravatarHash: 'str' = ""
    LastLogin: 'str' = ""
    Name: 'str' = ""
    Permissions: 'list[str]' = field(default_factory=list)
    Roles: 'list[str]' = field(default_factory=list)
    CannotChangePassword: 'bool' = False
    PasswordExpires: 'bool' = False
    MustChangePassword: 'bool' = False
    IsSuperUser: 'bool' = False
    IsLDAPUser: 'bool' = False
    Disabled: 'bool' = False
    IsTwoFactorEnabled: 'bool' = False

@dataclass
class UserInfoSummary:
    """
    Information about the user
    :param GravatarHash: The Gravatar hash
    :type GravatarHash: str
    :param AvatarBase64: The avatar base64
    :type AvatarBase64: str
    :param EmailAddress: The email address
    :type EmailAddress: str
    :param LastLogin: The last login
    :type LastLogin: str
    :param ID: The user ID
    :type ID: str
    :param Username: The username
    :type Username: str
    :param IsTwoFactorEnabled: Whether 2FA is enabled
    :type IsTwoFactorEnabled: bool
    :param IsLDAPUser: Whether the user is an LDAP user
    :type IsLDAPUser: bool
    :param Disabled: Whether the user is disabled
    :type Disabled: bool
    """
    GravatarHash: 'str' = ""
    AvatarBase64: 'str' = ""
    EmailAddress: 'str' = ""
    LastLogin: 'str' = ""
    ID: 'str' = ""
    Username: 'str' = ""
    IsTwoFactorEnabled: 'bool' = False
    IsLDAPUser: 'bool' = False
    Disabled: 'bool' = False

@dataclass
class Version:
    """
    AMP version information
    :param Build: The build number
    :type Build: int
    :param MajorRevision: The major revision number
    :type MajorRevision: int
    :param Major: The major version number
    :type Major: int
    :param MinorRevision: The minor revision number
    :type MinorRevision: int
    :param Minor: The minor version number
    :type Minor: int
    :param Revision: The revision number
    :type Revision: int
    """
    Build: 'int' = 0
    MajorRevision: 'int' = 0
    Major: 'int' = 0
    MinorRevision: 'int' = 0
    Minor: 'int' = 0
    Revision: 'int' = 0

class VirtualizationType(Enum):
    """
    Represents the virtualization type
    :param None_: None/Bare Metal
    :type None_: Int32
    :param VMware: VMware
    :type VMware: Int32
    :param VMwareESX: VMware ESX
    :type VMwareESX: Int32
    :param VirtualBox: VirtualBox
    :type VirtualBox: Int32
    :param Xen: Xen
    :type Xen: Int32
    :param QEMU_KVM: QEMU KVM
    :type QEMU_KVM: Int32
    :param OpenVZ: OpenVZ
    :type OpenVZ: Int32
    :param HyperV: HyperV
    :type HyperV: Int32
    :param Docker: Docker
    :type Docker: Int32
    :param LXC: LXC
    :type LXC: Int32
    :param WSL: Windows Subsystem for Linux
    :type WSL: Int32
    :param ProxmoxVM: ProxmoxVM
    :type ProxmoxVM: Int32
    :param ProxmoxLXC: Proxmox LXC Container
    :type ProxmoxLXC: Int32
    """
    None_ = 0
    VMware = 1
    VMwareESX = 2
    VirtualBox = 3
    Xen = 4
    QEMU_KVM = 5
    OpenVZ = 6
    HyperV = 7
    Docker = 8
    LXC = 9
    WSL = 10
    ProxmoxVM = 11
    ProxmoxLXC = 12

@dataclass
class WebauthnCredentialSummary:
    """
    A summary of a WebAuthn credential
    :param ID: The ID
    :type ID: int
    :param CreatedUTC: The created time
    :type CreatedUTC: str
    :param Description: The description
    :type Description: str
    :param LastUsedUTC: The last used time
    :type LastUsedUTC: str
    """
    ID: 'int' = 0
    CreatedUTC: 'str' = ""
    Description: 'str' = ""
    LastUsedUTC: 'str' = ""

@dataclass
class WebauthnLoginInfo:
    """
    Information about a WebAuthn login
    :param Ids: The IDs
    :type Ids: list[str]
    :param Challenge: The challenge
    :type Challenge: str
    """
    Ids: 'list[str]' = field(default_factory=list)
    Challenge: 'str' = ""

@dataclass
class WebSessionSummary:
    """
    A summary of a web session
    :param LastActivity: The last activity
    :type LastActivity: str
    :param SessionID: The session ID
    :type SessionID: str
    :param SessionType: The session type
    :type SessionType: str
    :param Source: The source
    :type Source: str
    :param StartTime: The start time
    :type StartTime: str
    :param Username: The username
    :type Username: str
    """
    LastActivity: 'str' = ""
    SessionID: 'str' = ""
    SessionType: 'str' = ""
    Source: 'str' = ""
    StartTime: 'str' = ""
    Username: 'str' = ""

@dataclass
class WhitelistEntry:
    """
    A whitelist entry
    :param UUID: The UUID
    :type UUID: str
    :param Name: The name
    :type Name: str
    """
    UUID: 'str' = ""
    Name: 'str' = ""

