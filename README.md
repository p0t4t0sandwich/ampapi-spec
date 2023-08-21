# ampapi-spec

A program that automagically updates a JSON file and a human readable file with the AMP API methods.

## Usage

For the JSON response of `Core.GetAPISpec`:

<https://raw.githubusercontent.com/p0t4t0sandwich/ampapi-spec/main/APISpec.json>

For the human readable response of Core.GetAPISpec (easier to check for differences):

<https://github.com/p0t4t0sandwich/ampapi-spec/blob/main/friendlySpec.txt>

## AMP API and Library Info

### API docs

Go to `http(s)://your.domain.com/API` to see the API docs.

### Libraries

- [C#](https://github.com/cubecoders/amp/wiki/Getting-started-with-AMP-developer-licences)
- [NodeJS](https://github.com/CubeCoders/ampapi-node)
- [Python](https://github.com/p0t4t0sandwich/ampapi-python)
- [Java](https://github.com/p0t4t0sandwich/ampapi-java)

### Work in Progress

- [TypeScript](https://github.com/p0t4t0sandwich/ampapi-typescript)
- [Bash](https://github.com/p0t4t0sandwich/ampapi-bash)
- [Go](https://github.com/p0t4t0sandwich/ampapi-go)
  - Need to port my auto-gen script, and needs someone with proper Go know-how to point out any sore spots.

## TODO

- Add a way to generate a diff file for easier reading
- Get different game module API Specs attached to the ADS, sort into some subdir setup
  - Could rely on this for class inheritance in lib generation
  - Or use per-module selective multi-inheritance, would be weirder to implement but more flexible
