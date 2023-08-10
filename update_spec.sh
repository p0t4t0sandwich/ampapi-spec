#!/bin/bash

# Function to generate the API Spec files from AMP
function generate_specs() {

    # Get the API Spec
    echo "Getting API Spec"

    API_SPEC=$(curl -s -X POST -H "accept: text/javascript" -d "{'SESSIONID':'$AMP_TOKEN'}" $AMP_URL/API/Core/GetAPISpec | jq -r .result)

    # Write the API Spec to a file
    echo "Writing API Spec to file"

    echo "$API_SPEC" | jq . > APISpec.json

    API_SPEC=$(cat APISpec.json)
    > friendlySpec.txt

    # Get the list of modules
    echo "Getting list of modules"

    MODULES=$(jq 'keys' APISpec.json | jq -c '.[]')

    # Loop through the modules and methods
    echo "Looping through modules and methods"

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
echo "Logging into AMP"

AMP_LOGIN=$(curl -s -X POST -H "accept: text/javascript" -d "{'username':'$AMP_USERNAME', 'password':'$AMP_PASSWORD', 'token':'', 'rememberMe': false}" $AMP_URL/API/Core/Login)
LOGIN_SUCCESS=$(echo "$AMP_LOGIN" | jq -r .success)

# Check if login was successful
if [ "$LOGIN_SUCCESS" != "true" ]; then
    echo "Login failed"
    exit 1
fi

AMP_TOKEN=$(echo "$AMP_LOGIN" | jq -r .sessionID)

# TODO: Get the current AMP version via API, then compare with AMP_CURRENT_VERSION in the env file, then send to $GITHUB_OUTPUT

# Generate the API Spec
generate_specs