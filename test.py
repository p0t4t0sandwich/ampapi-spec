import asyncio

from libraries.python.ampapi.auth import BasicAuthProvider, BasicAuthProviderAsync
from libraries.python.ampapi.modules import CommonAPI, CommonAPIAsync

authProvider = BasicAuthProvider(
    panelUrl="http://localhost:8080",
    username="api_user",
    password="api_user123!"
)

api = CommonAPI(authProvider)

print(api.Core.GetStatus())

# authProvider = BasicAuthProviderAsync(
#     panelUrl="http://localhost:8080",
#     username="api_user",
#     password="api_user123!"
# )

# api = CommonAPIAsync(authProvider)

# async def main():
#     print(await api.Core.GetStatus())

# asyncio.run(main())