import asyncio
import time

from libraries.python.ampapi.auth import BasicAuthProvider, BasicAuthProviderAsync, RefreshingAuthProvider
from libraries.python.ampapi.modules import CommonAPI, CommonAPIAsync
from libraries.python.ampapi.types import MetricInfo

authProvider = RefreshingAuthProvider(
    panelUrl="http://localhost:8080",
    username="api_user",
    password="api_user123!"
)

api = CommonAPI(authProvider)

print(api.Core.GetStatus().State)

# authProvider = BasicAuthProviderAsync(
#     panelUrl="http://localhost:8080",
#     username="api_user",
#     password="api_user123!"
# )

# api = CommonAPIAsync(authProvider)

# async def main():
#     print(await api.Core.GetStatus())

# asyncio.run(main())