#!/bin/bash

# Function to generate the API Spec files from AMP
function generate_specs() {

    # Get the API Spec
    API_SPEC=$(curl -s -X POST -H "accept: text/javascript" -d "{'SESSIONID':'$AMP_TOKEN'}" $AMP_URL/API/Core/GetAPISpec | jq -r .result)

    # Write the API Spec to a file
    echo "$API_SPEC" | jq . > APISpec.json

    API_SPEC=$(cat APISpec.json)
    > friendlySpec.txt

    # Get the list of modules
    MODULES=$(jq 'keys' APISpec.json | jq -c '.[]')

    # Loop through the modules and methods
    echo "$MODULES" | while read MODULE; do
        # Skip "CommonCorePlugin"
        if [ "$MODULE" == '"CommonCorePlugin"' ]; then
            continue
        fi

        METHODS=$(echo "$API_SPEC" | jq -r ".[$MODULE] | keys[]")

        echo "$METHODS" | while read METHOD; do
        # I want a space after the comma, but I can't figure out how to do that with tr
            PARAMS=$(echo "$API_SPEC" | jq -r ".[$MODULE].$METHOD.Parameters[].Name" | tr '\n' ',' | sed 's/,$//')
            echo "$MODULE.$METHOD($PARAMS)" | sed 's/"//g' >> friendlySpec.txt
        done
    done
}


# Log into AMP
AMP_TOKEN=$(curl -s -X POST -H "accept: text/javascript" -d "{'username':'$AMP_USERNAME', 'password':'$AMP_PASSWORD', 'token':'', 'rememberMe': false}" $AMP_URL/API/Core/Login | jq -r .sessionID)

# Check "Core.GetUpdateInfo" to see if there is an update available
UPDATE_INFO=$(curl -s -X POST -H "accept: text/javascript" -d "{'SESSIONID':'$AMP_TOKEN'}" $AMP_URL/API/Core/GetUpdateInfo)

# Check to see if there is an update available and if so, if it is a patch or full update
UPDATE_AVAILABLE=$(echo "$UPDATE_INFO" | jq -r .result.UpdateAvailable)
PATCH_ONLY=$(echo "$UPDATE_INFO" | jq -r .result.PatchOnly)

if [ "$UPDATE_AVAILABLE" == "true" ]; then
    if [ "$PATCH_ONLY" == "false" ]; then
        echo "AMP_VERSION=$AMP_VERSION" >> $GITHUB_ENV

        # Generate the API Spec
        generate_specs
    fi
fi