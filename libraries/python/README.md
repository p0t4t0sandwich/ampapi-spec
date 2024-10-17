# ampapi-py

[![License](https://img.shields.io/github/license/p0t4t0sandwich/ampapi-py?color=blue)](https://img.shields.io/github/downloads/p0t4t0sandwich/ampapi-py/LICENSE)
[![Github](https://img.shields.io/github/stars/p0t4t0sandwich/ampapi-py)](https://github.com/p0t4t0sandwich/ampapi-py)
[![Github Issues](https://img.shields.io/github/issues/p0t4t0sandwich/ampapi-py?label=Issues)](https://github.com/p0t4t0sandwich/ampapi-py/issues)
[![Discord](https://img.shields.io/discord/1067482396246683708?color=7289da&logo=discord&logoColor=white)](https://discord.neuralnexus.dev)
[![wakatime](https://wakatime.com/badge/github/p0t4t0sandwich/ampapi-py.svg)](https://wakatime.com/badge/github/p0t4t0sandwich/ampapi-py)

[![Github Releases](https://img.shields.io/github/downloads/p0t4t0sandwich/ampapi-py/total?label=Github&logo=github&color=181717)](https://github.com/p0t4t0sandwich/ampapi-py/releases)
[![PyPI](https://img.shields.io/pypi/v/ampapi?label=PyPI&logo=pypi&color=3775A9)](https://pypi.org/project/ampapi/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/ampapi?label=PyPI%20Downloads&logo=pypi&color=3775A9)](https://pypi.org/project/ampapi/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ampapi?label=Python&logo=python&color=3775A9)](https://pypi.org/project/ampapi/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/ampapi?label=Wheel&logo=python&color=3775A9)](https://pypi.org/project/ampapi/)

An API that allows you to communicate with AMP installations from within Python.

Documentation for available API calls can be found by appending /API to the URL of any existing AMP installation.

Support:

- Ping `@thepotatoking3452` in the `#development` channel of the [AMP Discord](https://discord.gg/cubecoders)
- My own [development Discord](https://discord.neuralnexus.dev/)

## Installation

```bash
pip install ampapi
```

or

```bash
pip install 'ampapi @ git+https://github.com/p0t4t0sandwich/ampapi-py.git'
```

You also need the following packages installed:

```bash
pip install requests aiohttp json
```

## Notes

I've redone the return types, most should work, but if you find any that don't, please let me know.

## Examples

### CommonAPI Example

```python
from ampapi.modules.CommonAPI import CommonAPI

def main():
    # If you know the module that the instance is using, specify it instead of CommonAPI
    API = CommonAPI("http://localhost:8080/", "admin", "myfancypassword123")
    API.Login()

    # API call parameters are simply in the same order as shown in the documentation.
    API.Core.SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")

    currentStatus = API.Core.GetStatus()
    CPUUsagePercent = currentStatus.Metrics["CPU Usage"].Percent

    print(f"Current CPU usage is: {CPUUsagePercent}%")

main()
```

### Async CommonAPI Example

```python
import asyncio
from ampapi.modules.CommonAPI import CommonAPI

async def main():
    # If you know the module that the instance is using, specify it instead of CommonAPI
    API = CommonAPI("http://localhost:8080/", "admin", "myfancypassword123")
    await API.LoginAsync()

    # API call parameters are simply in the same order as shown in the documentation.
    await API.Core.SendConsoleMessageAsync("say Hello Everyone, this message was sent from the Python API!")

    currentStatus = await API.Core.GetStatusAsync()
    CPUUsagePercent = currentStatus.Metrics["CPU Usage"].Percent

    print(f"Current CPU usage is: {CPUUsagePercent}%")

asyncio.run(main())
```

### Example using the ADS to manage an instance

```python
from ampapi.modules.ADS import ADS

API = ADS("http://localhost:8080/", "admin", "myfancypassword123")
API.Login()

# Get the available instances
targets = API.ADSModule.GetInstances()

# In this example, my Hub server is on the second target
# If you're running a standalone setup, you can just use targets[1]
target = targets[1]

hub_instance_id = ""

# Get the available instances
instances = target.AvailableInstances
for instance in instances:
    # Find the instance named "Hub"
    if instance.InstanceName == "Hub":
        hub_instance_id = instance.InstanceID
        break

# Use the instance ID to get the API for the instance
Hub = API.InstanceLogin(hub_instance_id, "Minecraft")

# Get the current CPU usage
currentStatus = Hub.Core.GetStatus()
CPUUsagePercent = currentStatus.Metrics["CPU Usage"].Percent

# Send a message to the console
Hub.Core.SendConsoleMessage(f"say Current CPU usage is {CPUUsagePercent}%")
```

### CommonAPI Example, handling the sessionId and rememberMeToken manually (not recommended)

```python
from ampapi.modules.CommonAPI import CommonAPI

try:
    API = CommonAPI("http://localhost:8080/")

    # The third parameter is either used for 2FA logins, or if no password is specified to use a remembered token from a previous login, or a service login token.
    loginResult = API.Core.Login("admin", "myfancypassword123", "", False)

    if loginResult.success:
        print("Login successful")
        API.sessionId = loginResult.sessionID
        API.Core.sessionId = loginResult.sessionID

        # API call parameters are simply in the same order as shown in the documentation.
        API.Core.SendConsoleMessage("say Hello Everyone, this message was sent from the Python API!")
        currentStatus = API.Core.GetStatus()
        CPUUsagePercent = currentStatus.Metrics["CPU Usage"].Percent
        print(f"Current CPU usage is: {CPUUsagePercent}%")

    else:
        print("Login failed")
        print(loginResult)

except Exception as err:
    # In reality, you'd handle this exception better
    raise Exception(err)
```
