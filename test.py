from libraries.python.ampapi.auth import BasicAuthProvider
from libraries.python.ampapi.modules import CommonAPI


authProvider = BasicAuthProvider(
    panelUrl="http://localhost:8080",
    username="api_user",
    password="api_user123!"
)

api = CommonAPI(authProvider)

print(api.Core.GetStatus().Metrics)
