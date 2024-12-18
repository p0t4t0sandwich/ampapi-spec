import asyncio
import time

from libraries.python.ampapi.auth import BasicAuthProvider, BasicAuthProviderAsync, RefreshingAuthProvider
from libraries.python.ampapi.modules import CommonAPI, CommonAPIAsync, ADSAsync
from libraries.python.ampapi.types import MetricInfo

PANEL_URL = "http://localhost:8080"
USERNAME = "api_user"
PASSWORD = "api_user123!"

def main():
    authProvider = RefreshingAuthProvider(
        panelUrl=PANEL_URL,
        username=USERNAME,
        password=PASSWORD
    )

    api = CommonAPI(authProvider)

    print(authProvider.instanceName)
    print(authProvider.instanceId)

    print(api.Core.GetStatus().State)

async def async_main():
    authProvider = BasicAuthProviderAsync(
        panelUrl=PANEL_URL,
        username=USERNAME,
        password=PASSWORD
    )

    api = ADSAsync(authProvider)

#    print(await authProvider.instanceName)
#    print(await authProvider.instanceId)

#    print((await api.Core.GetStatus()).State)

    instances = await api.ADSModule.GetInstances(ForceIncludeSelf=False)
    print(instances)

now = time.time()
main()
print("Sync time:", time.time() - now)
print("--------------------------------")

now = time.time()
asyncio.run(async_main())
print("Async time:", time.time() - now)
print("--------------------------------")
