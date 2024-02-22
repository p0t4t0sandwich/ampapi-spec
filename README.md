# ampapi-spec

[![License](https://img.shields.io/github/license/p0t4t0sandwich/ampapi-spec?color=blue)](https://img.shields.io/github/downloads/p0t4t0sandwich/ampapi-spec/LICENSE)
[![Github](https://img.shields.io/github/stars/p0t4t0sandwich/ampapi-spec)](https://github.com/p0t4t0sandwich/ampapi-spec)
[![Github Issues](https://img.shields.io/github/issues/p0t4t0sandwich/ampapi-spec?label=Issues)](https://github.com/p0t4t0sandwich/ampapi-spec/issues)
[![Discord](https://img.shields.io/discord/1067482396246683708?color=7289da&logo=discord&logoColor=white)](https://discord.neuralnexus.dev)
[![wakatime](https://wakatime.com/badge/github/p0t4t0sandwich/ampapi-spec.svg)](https://wakatime.com/badge/github/p0t4t0sandwich/ampapi-spec)

A program that automagically updates a JSON file and a human readable file with the AMP API methods.

## Usage

For the JSON response of `API.Core.GetAPISpec`:

<https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-spec/main/APISpec.json>

For the human readable response of `API.Core.GetAPISpec` (easier to check for differences):

<https://github.com/p0t4t0sandwich/ampapi-spec/blob/main/FriendlySpec.txt>

API module inheritance for different instance types:

<https://github.com/p0t4t0sandwich/ampapi-spec/blob/main/ModuleInheritance.json>

## AMP API and Library Info

### API docs

Go to `http(s)://your.domain.com/API` to see the API docs.

### Libraries

#### C#
- [Developer Licence Usage](https://github.com/cubecoders/amp/wiki/Getting-started-with-AMP-developer-licences)
- Examples:
  - [SampleAMPModule](https://github.com/CubeCoders/SampleAMPModule) - official code example
  - [AMP-Discord-Bot](https://github.com/winglessraven/AMP-Discord-Bot) - a great community developed Discord bot
#### NodeJS
- [ampapi-node](https://github.com/CubeCoders/ampapi-node) - bare bones, but generates new methods on the fly, not requiring library updates
- [ampapi-js](https://github.com/p0t4t0sandwich/ampapi-js) - auto-generated from the API, includes `d.ts` type definitions and code-completion
  - Examples:
    - [taterland-discord-bot](https://github.com/p0t4t0sandwich/taterland-discord-bot)
#### Python
- [ampapi-py](https://github.com/p0t4t0sandwich/ampapi-py) - auto-generated from the API, though a bit bland in terms of tooling
- [AMPAPI_Python](https://github.com/k8thekat/AMPAPI_Python) - built with developer experiences in mind, with all the bells and whistles you'll need
  - Examples:
    - [GatekeeperV2](https://github.com/k8thekat/GatekeeperV2)
#### Java
- [ampapi-java](https://github.com/p0t4t0sandwich/ampapi-java)
  - Examples:
    - [ServerPanelManager](https://github.com/p0t4t0sandwich/ServerPanelManager)
    - [taterlib-ci](https://github.com/p0t4t0sandwich/taterlib-ci)
    - [CustomServerManager](https://github.com/p0t4t0sandwich/CustomServerManager)
#### Go/Golang
- [ampapi-go](https://github.com/p0t4t0sandwich/ampapi-go)
  - Examples:
    - [ampapi-stats-wrapper](https://github.com/p0t4t0sandwich/ampapi-stats-wrapper)
#### Rust
- [ampapi-rs](https://github.com/p0t4t0sandwich/ampapi-rs)

### Work in Progress

- [C++](https://github.com/p0t4t0sandwich/ampapi-cpp)
- [Bash](https://github.com/p0t4t0sandwich/ampapi-bash)
- [PHP](https://github.com/p0t4t0sandwich/ampapi-php)

### Proxying-instance-auth explanation: [AMP Discord #development](https://discord.com/channels/266012086423912458/266015417842139136/1151622027388657744)
